from transformers import AutoModelForCausalLM, AutoConfig
import json
import torch

model_a = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B")
model_b = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B", revision="stage2-ingredient3-step23852-tokens51B")

config_a = AutoConfig.from_pretrained("allenai/OLMo-2-0425-1B")
config_b = AutoConfig.from_pretrained("allenai/OLMo-2-0425-1B", revision="stage2-ingredient3-step23852-tokens51B")

dict_a = config_a.to_dict()
dict_b = config_b.to_dict()

all_keys = set(dict_a) | set(dict_b)
for key in sorted(all_keys):
    a, b = dict_a.get(key, "MISSING"), dict_b.get(key, "MISSING")
    if a != b:
        print(f"{key}:\n  main:     {a}\n  revision: {b}\n")