#!/bin/bash
#PBS -q normal
#PBS -N prop-chunk_aa
#PBS -l select=1:ncpus=4:mem=64gb
#PBS -l walltime=24:00:00
#PBS -j oe
#PBS -P personal-clar0092

cd scratch/acu
module load miniforge3
module load cuda/12.2.1
conda activate persona
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122
export LD_PRELOAD=/home/users/ntu/clar0092/scratch/envs/persona/lib/libstdc++.so.6
export PYTHONPATH=$PWD:$PYTHONPATH
hf auth login --token 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

python src/property_detection/get_properties.py --data_path "data/tulu/chunks/chunk_aa.csv" --save_folder "data/tulu/results/chunk_aa" --properties "flesch_reading_ease_score uncertain_rate_lexicon claim_evidence_jaccard_sim evidence_length claim_length"
