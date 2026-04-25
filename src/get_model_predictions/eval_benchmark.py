import json
import csv
import sys
import lm_eval

MODEL_NAME = sys.argv[1]
REVISION = sys.argv[2] if len(sys.argv) > 2 else None
OUTPUT     = sys.argv[3]
TASKS = ["gsm8k", "mmlu", "arc_challenge"]

TASK_METRICS = {
    "gsm8k":         ("gsm8k",        "exact_match,strict-match"),
    "mmlu":          ("mmlu",          "acc,none"),
    "arc_challenge": ("arc_challenge", "acc_norm,none"),
}

model_args = f"pretrained={MODEL_NAME},dtype=bfloat16"

if REVISION:
    model_args += f",revision={REVISION}"

results = lm_eval.simple_evaluate(
    model="hf",
    model_args=model_args,
    tasks=TASKS,
    batch_size="auto",
    log_samples=False,
)["results"]

scores = {}
for task, (key, metric) in TASK_METRICS.items():
    scores[task] = results[key][metric]
scores["avg"] = sum(scores.values()) / len(scores)
scores["revision"] = REVISION

with open(OUTPUT, "w") as f:
    json.dump(scores, f, indent=2)

print(f"Done: {scores}")