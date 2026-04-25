#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=6:00:00
#PBS -N ins-context-reliance
#PBS -P personal-clar0092

DATA_FILE="data/context_parametric_conflict_removed.csv"
SAVE_FOLDER="data/cr/ins"
USE_EVIDENCE="no"
MODEL_NAME="allenai/OLMo-2-1124-7B-Instruct"
PROMPT_NAME="context_reliance_no_ev"

module load miniforge3
conda activate persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122

hf auth login --token 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

python -m src.get_model_predictions.get_model_predictions --data_file ${DATA_FILE} --save_folder ${SAVE_FOLDER} --use_evidence ${USE_EVIDENCE} --model_name ${MODEL_NAME} --prompt_name ${PROMPT_NAME} --instruct