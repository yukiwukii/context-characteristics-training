#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=6:00:00
#PBS -N sft-cfcqa 
#PBS -P personal-clar0092
set -a && source .env && set +a

DATA_FILE="data/cf-cqa-few-shot.csv"
SAVE_FOLDER="data/res/sft"
USE_EVIDENCE="yes"
MODEL_NAME="allenai/OLMo-2-0425-1B-SFT"
PROMPT_NAME="pythia_evidence_prompt_3_shot_alt_4_no_claimant"

module load miniforge3
conda activate scratch/envs/persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122


python -m src.get_model_predictions.get_model_predictions --data_file ${DATA_FILE} --save_folder ${SAVE_FOLDER} --use_evidence ${USE_EVIDENCE} --model_name ${MODEL_NAME} --prompt_name ${PROMPT_NAME}