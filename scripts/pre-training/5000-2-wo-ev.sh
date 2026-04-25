#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=2:00:00
#PBS -N 5000-2-wo-ev
#PBS -P personal-clar0092
set -a && source .env && set +a

DATA_FILE="data/druid-few-shot.csv"
SAVE_FOLDER="data/res"
USE_EVIDENCE="no"
MODEL_NAME="allenai/OLMo-2-1124-7B"
PROMPT_NAME="pythia_claim_prompt_3_shot"
REVISION="stage2-ingredient3-step5000-tokens21B"

module load miniforge3
conda activate scratch/envs/persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122


python -m src.get_model_predictions.get_model_predictions --data_file ${DATA_FILE} --save_folder ${SAVE_FOLDER} --use_evidence ${USE_EVIDENCE} --model_name ${MODEL_NAME} --prompt_name ${PROMPT_NAME} --revision ${REVISION}