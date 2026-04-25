#!/bin/bash
set -a && source .env && set +a
MODEL_NAME="meta-llama/Llama-3.2-1B"
RESULTS_DIR="data/benchmark/${MODEL_NAME//\//_}"
mkdir -p "$RESULTS_DIR"

REVISIONS=("")
# REVISIONS=()
# for x in $(seq 2000 1000 12000); do
#     REVISIONS+=("llama_1b_sft_step_${x}")
# done

BATCH_SIZE=3
WAIT_SECONDS=3600  # 1 hour


for i in "${!REVISIONS[@]}"; do
    REVISION="${REVISIONS[$i]}"

    if [ -z "$REVISION" ] || [ "$REVISION" = "None" ]; then
        REVISION_ARG=""
        OUTFILE="${RESULTS_DIR}/default.json"
    else
        REVISION_ARG="$REVISION"
        OUTFILE="${RESULTS_DIR}/${REVISION}.json"
    fi

    if [ -f "$OUTFILE" ]; then
        echo "Skipping $REVISION (already exists)"
        continue
    fi

    qsub \
        -N "eval_${REVISION}" \
        -l select=1:ncpus=8:mem=40gb:ngpus=1 \
        -l walltime=04:00:00 \
        -P personal-clar0092 \
        -j oe \
        -o "${RESULTS_DIR}/${REVISION}.log" \
        << EOF
#!/bin/bash
module load miniforge3
module load cuda/12.2.1
conda activate persona
cd scratch/acu
export HF_HUB_CACHE=/home/users/ntu/clar0092/scratch
export HF_HOME=/home/users/ntu/clar0092/scratch
export BNB_CUDA_VERSION=122
export LD_PRELOAD=/home/users/ntu/clar0092/scratch/envs/persona/lib/libstdc++.so.6
export PYTHONPATH=\$PWD:\$PYTHONPATH
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
mkdir -p logs
python src/get_model_predictions/eval_benchmark.py '$MODEL_NAME' '$REVISION' '$OUTFILE'
EOF

    # wait after every BATCH_SIZE submissions
    if (( (i + 1) % BATCH_SIZE == 0 )); then
        echo "Submitted batch $((i / BATCH_SIZE + 1)), waiting 1 hour..."
        sleep $WAIT_SECONDS
    fi
done