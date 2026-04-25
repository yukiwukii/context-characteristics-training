#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=2:00:00
#PBS -N test
#PBS -P personal-clar0092

module load miniforge3
conda activate scratch/envs/persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122

hf auth login --token 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

python test_models.py