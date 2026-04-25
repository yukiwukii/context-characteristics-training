#!/bin/bash
set -a && source .env && set +a
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=4:00:00
#PBS -N property-detection
#PBS -P personal-clar0092

# ── Config ────────────────────────────────────────────────────────────────────
MODEL_NAME="meta-llama/Llama-3.1-8B-Instruct"                   # e.g. meta-llama/Llama-3.1-8B-Instruct
HF_DATASET="allenai/tulu-3-sft-mixture"                   # e.g. "username/dataset-name"
HF_SPLIT="train"                    # dataset split to use
DATA_PATH="data/tulu-3-sft-mixture.csv"  # auto-derived from HF dataset name
SAVE_FOLDER="data/tulu"                  # output folder
# PROPERTIES="claim_entity_overlap flesch_reading_ease_score uncertain_rate_lexicon claim_evidence_jaccard_sim claim_repeated_in_evidence evidence_length claim_length"  # excluded: unreliable_mbfc, is_factcheck_article (require evidence_source)
PROPERTIES="flesch_reading_ease_score uncertain_rate_lexicon claim_evidence_jaccard_sim evidence_length claim_length"

module load miniforge3
module load cuda/12.2.1
conda activate persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122
export LD_PRELOAD=/home/users/ntu/clar0092/scratch/envs/persona/lib/libstdc++.so.6
export PYTHONPATH=$PWD:$PYTHONPATH

mkdir -p logs

echo "========================================="
echo "Job:       $PBS_JOBID"
echo "Node:      $HOSTNAME"
echo "Started:   $(date)"
echo "========================================="

# # Step 0: Download HF dataset to temp TSV
# echo "[0/3] Downloading HF dataset '$HF_DATASET' (split=$HF_SPLIT)..."
# python -c "
# import pandas as pd
# from datasets import load_dataset

# df = load_dataset('allenai/tulu-3-sft-mixture', split='train').to_pandas()

# def extract_turn(messages, role):
#     for m in messages:
#         if m['role'] == role:
#             return m['content']
#     return None

# df['claim'] = df['messages'].apply(lambda x: extract_turn(x, 'user'))
# df['evidence'] = df['messages'].apply(lambda x: extract_turn(x, 'assistant'))
# df = df.dropna(subset=['claim', 'evidence'])
# df = df.rename(columns={'id': 'claim_id'})
# df = df.reset_index().rename(columns={'index': 'id'})
# df.to_csv('$DATA_PATH', index=False)
# print(f'Saved {len(df)} rows to $DATA_PATH')
# "
# echo "Dataset download done at $(date)"

# Step 1: Perplexity
# echo "[1/3] Running get_perplexity.py (model=$MODEL_NAME)..."
# python src/property_detection/get_perplexity.py "$MODEL_NAME" "$DATA_PATH"
# echo "get_perplexity.py done at $(date)"

# # Step 2: Heuristic properties
echo "[2/3] Running get_properties.py (properties=$PROPERTIES)..."
python src/property_detection/get_properties.py \
    --data_path "$DATA_PATH" \
    --save_folder "$SAVE_FOLDER" \
    --properties "$PROPERTIES"
echo "get_properties.py done at $(date)"

# Step 3: Cohere properties
# echo "[3/3] Running get_properties_cohere.py (properties=$COHERE_PROPERTIES)..."
# python src/property_detection/get_properties_cohere.py \
#     --data_path "$DATA_PATH" \
#     --save_folder "$SAVE_FOLDER" \
#     --properties "$COHERE_PROPERTIES"
# echo "get_properties_cohere.py done at $(date)"

echo "========================================="
echo "All steps complete: $(date)"
echo "========================================="