#!/bin/bash
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=1
#PBS -l walltime=4:00:00
#PBS -N ipynb
#PBS -P personal-clar0092