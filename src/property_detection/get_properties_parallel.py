from pathlib import Path
import os
from urllib.parse import urlparse
import pandas as pd
import numpy as np
import spacy
from matplotlib import pyplot as plt
from textstat import flesch_reading_ease
from nltk.metrics.distance import jaccard_distance
from nltk.tokenize import word_tokenize
from string import punctuation
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

from src.property_detection.property_detectors import FactCheckDetector, UnreliableDetector, HedgeDetector
from src.utils import print_data_to_txt_file

SKIPLIST = set(list(punctuation) + ["\u201c", "\u201d", "\u2014", "\u2018", "``", "''"])

def get_unreliable_mbfc(data):
    evidence_sources = data.evidence_source.tolist()
    unreliable_detector = UnreliableDetector()
    mbfc_bias_cat = list(map(unreliable_detector.get_bias_cat, evidence_sources))
    mbfc_fact_cat = list(map(unreliable_detector.get_fact_cat, evidence_sources))

    def get_domain(es): return urlparse(es).netloc
    def is_gov_page(es): d = get_domain(es); return d.endswith(".gov") or ".gov." in d
    def is_edu_page(es): return get_domain(es).endswith(".edu")

    is_gov_pages = list(map(is_gov_page, evidence_sources))
    is_edu_pages = list(map(is_edu_page, evidence_sources))

    def is_unreliable(bc, fc, gov, edu):
        if bc is None and fc is None:
            return False if (gov or edu) else None
        if fc in ["questionable_sources", "conspiracy_pseudoscience", "satire"]:
            return True
        if bc in ["left_bias", "righ_bias"]:
            return True
        return False

    return list(map(is_unreliable, mbfc_bias_cat, mbfc_fact_cat, is_gov_pages, is_edu_pages))

def get_is_factcheck_article(data):
    evidence_sources = data.evidence_source.tolist()
    fact_check_detector = FactCheckDetector()
    is_factcheck_article = list(map(fact_check_detector.is_fact_check_article, evidence_sources))
    url_sites_fact = data[~(np.array(is_factcheck_article))]\
        .evidence_source[data.evidence_source.apply(lambda val: "fact" in val)].unique()
    check_url_sites_fact = list(set([urlparse(url).netloc.replace("www.", "") for url in url_sites_fact]))
    check_url_sites_fact.extend(list(set([url.replace("www.", "") for url in url_sites_fact])))
    print_data_to_txt_file(check_url_sites_fact, "tmp_potentially_missed_fc_sites.txt")
    return is_factcheck_article

def get_claim_entity_overlap(data):
    def get_implicit_level(e1, e2):
        if len(e1) == 0:
            return None
        return len(e1.intersection(e2)) / len(e1)
    ner = spacy.load("en_core_web_trf")
    claim_entities = list(map(lambda val: set([ent.text.lower() for ent in ner(val).ents]), data.claim.tolist()))
    evidence_entities = list(map(lambda val: set([ent.text.lower() for ent in ner(val).ents]), data.evidence.tolist()))
    return list(map(get_implicit_level, claim_entities, evidence_entities))

def get_flesch_reading_ease_score(data):
    return data.evidence.apply(flesch_reading_ease)

def get_uncertain_rate_lexicon(data):
    hedge_detector = HedgeDetector()
    results = data.evidence.apply(hedge_detector.is_hedged_text).tolist()
    dm, ht, bn = zip(*results)
    return {"uncertain_discourse_markers": list(dm),
            "uncertain_hedge_terms": list(ht),
            "uncertain_boosters_preceeded_by_negation": list(bn)}

def get_jaccard_sim(data):
    def get_jaccard_index(s1, s2):
        w1 = set([w.lower() for w in word_tokenize(s1) if w.lower() not in SKIPLIST])
        w2 = set([w.lower() for w in word_tokenize(s2) if w.lower() not in SKIPLIST])
        return 1 - jaccard_distance(w1, w2)
    return list(map(get_jaccard_index, data.claim, data.evidence))

def get_claim_repeated_in_evidence(data):
    def string_in_doc(s, doc):
        s_w = " ".join([w.lower() for w in word_tokenize(s) if w.lower() not in SKIPLIST])
        d_w = " ".join([w.lower() for w in word_tokenize(doc) if w.lower() not in SKIPLIST])
        return s_w in d_w
    return list(map(string_in_doc, data.claim, data.evidence))

def get_evidence_length(data):
    return data.evidence.apply(len)

def get_claim_length(data):
    return data.claim.apply(len)

PROPERTY_FUNS = {
    "unreliable_mbfc": get_unreliable_mbfc,
    "is_factcheck_article": get_is_factcheck_article,
    "claim_entity_overlap": get_claim_entity_overlap,
    "flesch_reading_ease_score": get_flesch_reading_ease_score,
    "uncertain_rate_lexicon": get_uncertain_rate_lexicon,
    "claim_evidence_jaccard_sim": get_jaccard_sim,
    "claim_repeated_in_evidence": get_claim_repeated_in_evidence,
    "evidence_length": get_evidence_length,
    "claim_length": get_claim_length,
}


def process_chunk(args):
    """Each worker reads only its rows from disk using skiprows+nrows."""
    data_path, start, nrows, prop = args
    # skip rows 1..start (row 0 is header), read only nrows
    skip = range(1, start + 1) if start > 0 else None
    data = pd.read_csv(data_path, skiprows=skip, nrows=nrows).set_index("id")
    res = PROPERTY_FUNS[prop](data)
    if isinstance(res, dict):
        return pd.DataFrame(res, index=data.index)
    else:
        return pd.DataFrame({prop: res}, index=data.index)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str)
    parser.add_argument("--save_folder", type=str)
    parser.add_argument("--properties", type=str)
    parser.add_argument("--num_workers", type=int, default=1)
    args = parser.parse_args()

    Path(args.save_folder).mkdir(exist_ok=True)

    # Read full data once in main process for final assembly/stats
    print("Loading data...")
    data = pd.read_csv(args.data_path).set_index("id")
    n = len(data)
    print(f"{n} samples loaded.")

    properties = list(PROPERTY_FUNS.keys()) if args.properties == "all" else args.properties.split()

    # Compute (start_row, nrows) per worker — no overlap, no full-file loads
    chunk_size = n // args.num_workers
    boundaries = [
        (i * chunk_size, chunk_size if i < args.num_workers - 1 else n - i * chunk_size)
        for i in range(args.num_workers)
    ]

    for prop in properties:
        print(f"\nProcessing property: {prop} ({args.num_workers} workers)...")
        save_file = os.path.join(args.save_folder, f"tmp_{prop}.tsv")

        task_args = [(args.data_path, start, nrows, prop) for start, nrows in boundaries]

        results = []
        with ProcessPoolExecutor(max_workers=args.num_workers) as executor:
            futures = {executor.submit(process_chunk, a): i for i, a in enumerate(task_args)}
            for f in tqdm(as_completed(futures), total=len(futures), desc=prop):
                results.append(f.result())

        result_df = pd.concat(results).sort_index()
        for col in result_df.columns:
            data[col] = result_df[col]
        data[result_df.columns].to_csv(save_file)
        print(f"Saved checkpoint: {save_file}")

        prop_cols = list(result_df.columns)
        if len(prop_cols) > 1 or len(data[prop_cols[0]].unique()) < 5:
            print(data.value_counts(prop_cols, sort=False, dropna=False))
        else:
            data[prop_cols[0]].hist()
            plt.xlabel(prop_cols[0])
            plt.ylabel("Counts")
            filename = os.path.join(args.save_folder, f"{prop}_hist.pdf")
            plt.savefig(filename)
            plt.clf()
            print(f"Histogram saved: {filename}")

    save_file = os.path.join(args.save_folder, "data_with_properties.tsv")
    data.to_csv(save_file, sep="\t")
    print(f"\nDone! Saved to '{save_file}'.")