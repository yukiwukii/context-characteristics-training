import os
import torch
import argparse
import random
import numpy as np
import transformers
import pandas as pd
from tqdm import tqdm

from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
from datasets import Dataset
from transformers.pipelines.pt_utils import KeyDataset

from src.get_model_predictions.prompts import PROMPT_DICT

torch.backends.cuda.enable_mem_efficient_sdp(False)
torch.backends.cuda.enable_flash_sdp(False)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def enforce_reproducibility(seed=1000):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    random.seed(seed)
    np.random.seed(seed)

def get_prompt(row, prompt_template, use_evidence):
    prompt = prompt_template.replace("<claim>", row['claim'])
    if "<claimant>" in prompt:
        prompt = prompt.replace("<claimant>", row['claimant'])
    if use_evidence:
        prompt = prompt.replace("<evidence>", row['evidence'])
    return prompt

def predict_veracity(file_path, save_folder, use_evidence, model_code, prompt_name, cache_folder, revision=None, instruct=False):
    tokenizer = AutoTokenizer.from_pretrained(model_code, revision=revision, cache_dir=cache_folder)
    model = AutoModelForCausalLM.from_pretrained(model_code,
            revision=revision,
            device_map="auto",
            trust_remote_code=True,
            cache_dir=cache_folder)
    tokenizer.pad_token = tokenizer.eos_token

    if file_path.endswith(".tsv"):
        data = pd.read_csv(file_path, sep="\t").set_index("id")
    elif file_path.endswith(".csv"):
        data = pd.read_csv(file_path).set_index("id")
        # data = data.head(10)
    else:
        raise ValueError(f"Can only handle .tsv or .csv files, got '{file_path}'.")

    prompt_template = PROMPT_DICT[prompt_name]

    if use_evidence == 'yes':
        assert "<evidence>" in prompt_template
        print("Using evidence")
        use_evidence = True
    else:
        assert "<evidence>" not in prompt_template
        print("Not using evidence")
        use_evidence = False
        data = data.drop_duplicates(subset=["claim_id"])

    data["prompt"] = data.apply(lambda row: get_prompt(row, prompt_template, use_evidence), axis=1)
    if instruct:
        data["prompt"] = data["prompt"].apply(
            lambda p: tokenizer.apply_chat_template(
                [{"role": "user", "content": p}],
                tokenize=False,
                add_generation_prompt=True,
            )
        )
    dataset = Dataset.from_pandas(data[["claim_id", "prompt"]])

    pipe = transformers.pipeline(model=model, tokenizer=tokenizer, task='text-generation')

    config = GenerationConfig(
        max_new_tokens=1024,
        eos_token_id=tokenizer.eos_token_id,
    )

    answers = []
    for out in tqdm(pipe(KeyDataset(dataset, "prompt"),
                         pad_token_id=tokenizer.pad_token_id,
                         return_full_text=False,
                         generation_config=config),
                    total=len(data)):
        answers.append(out[0]["generated_text"].strip())

    suffix = "w_evidence" if use_evidence else "wo_evidence"
    data["generated_answer"] = answers
    data = data.drop(columns=["prompt"])

    MODEL_NICKNAME = model_code.split('/')[1]
    filename = f'{MODEL_NICKNAME}_preds_{revision}_use_evidence_{use_evidence}_prompt_{prompt_name}.csv'
    data.to_csv(os.path.join(save_folder, filename))

if __name__ == '__main__':
    enforce_reproducibility()
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_file", type=str)
    parser.add_argument("--save_folder", type=str)
    parser.add_argument("--use_evidence", type=str, default="no", choices=['yes', 'no'])
    parser.add_argument("--model_name", type=str, default="no")
    parser.add_argument("--prompt_name", type=str, required=True)
    parser.add_argument("--cache_folder", type=str, default=None)
    parser.add_argument("--revision", type=str, default=None)
    parser.add_argument("--instruct", action="store_true")

    args = parser.parse_args()
    os.makedirs(args.save_folder, exist_ok=True)
    print(args)

    predict_veracity(file_path=args.data_file,
                     save_folder=args.save_folder,
                     use_evidence=args.use_evidence,
                     model_code=args.model_name,
                     prompt_name=args.prompt_name,
                     cache_folder=args.cache_folder,
                     revision=args.revision,
                     instruct=args.instruct)