#!/bin/bash
set -a && source .env && set +a
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=4:00:00
#PBS -N sft-cqa-0
#PBS -P personal-clar0092

DATA_FILE="data/cqa.csv"
SAVE_FOLDER="data/sft/conflict_qa"
USE_EVIDENCE="yes"
MODEL_NAME="meta-llama/Llama-3.2-1B"
PROMPT_NAME="context_reliance_w_ev_acc"

module load miniforge3
conda activate persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122


python -m src.get_model_predictions.get_full_predictions --data_file ${DATA_FILE} --save_folder ${SAVE_FOLDER} --use_evidence ${USE_EVIDENCE} --model_name ${MODEL_NAME} --prompt_name ${PROMPT_NAME}