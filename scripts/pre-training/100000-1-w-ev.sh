#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=2:00:00
#PBS -N 100000-1-w-ev
#PBS -P personal-clar0092

DATA_FILE="data/druid-few-shot.csv"
SAVE_FOLDER="data/res"
USE_EVIDENCE="yes"
MODEL_NAME="allenai/OLMo-2-1124-7B"
PROMPT_NAME="pythia_evidence_prompt_3_shot_alt_4"
REVISION="stage1-step101000-tokens424B"

module load miniforge3
conda activate scratch/envs/persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122

hf auth login --token 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

python -m src.get_model_predictions.get_model_predictions --data_file ${DATA_FILE} --save_folder ${SAVE_FOLDER} --use_evidence ${USE_EVIDENCE} --model_name ${MODEL_NAME} --prompt_name ${PROMPT_NAME} --revision ${REVISION}