#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=4:00:00
#PBS -N ppl-5000
#PBS -P personal-clar0092

# ── Config ────────────────────────────────────────────────────────────────────
MODEL_NAME="yukiwuki/open_instruct_dev"
REVISION="llama_1b_sft_step_5000"
DATA_PATH="data/druid.csv"

module load miniforge3
module load cuda/12.2.1
conda activate persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122
export LD_PRELOAD=/home/users/ntu/clar0092/scratch/envs/persona/lib/libstdc++.so.6
export PYTHONPATH=$PWD:$PYTHONPATH
hf auth login --token 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

mkdir -p logs

echo "========================================="
echo "Job:       $PBS_JOBID"
echo "Node:      $HOSTNAME"
echo "Started:   $(date)"
echo "========================================="

# Step 1: Perplexity
echo "[1/3] Running get_perplexity.py (model=$MODEL_NAME, revision=${REVISION:-default})..."
python src/property_detection/get_perplexity.py "$MODEL_NAME" "$DATA_PATH" "$REVISION"
echo "get_perplexity.py done at $(date)"

echo "========================================="
echo "All steps complete: $(date)"
echo "========================================="