import os
import json
import pandas as pd
from runeq import initialize
from runeq.resources.patient import get_all_patients

#try to only pull 1 patient at a time, for limited time

initialize()

patients = get_all_patients()

df = pd.DataFrame(patients.to_list())

output_dir = "/Volumes/Study Files/emily_analysis/RuneWatch" #path to folder on VPN
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "test.json")
df.to_json(output_path, orient="records", indent=2)
print(f"patient data exported to: {output_path}")
