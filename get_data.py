import os
import json
import pandas as pd
from runeq import initialize
from runeq.resources.stream_metadata import get_patient_stream_metadata
import time 

#init
initialize()

patient_id = "6KOZ" #insert rune labs patient ID

#try to only pull 1 patient at a time, for limited time
patient_streams = get_patient_stream_metadata(patient_id)

#filter by device ID
device_id = " "
 #where to find this deviceID?  extract this from get_patient
#helper to filter by time

def most_recent_two_weeks(stream) -> bool: 
    two_weeks = time.time() - 14*24*60*60 #14 days, 24 hours, 60 minutes, 60 seconds
    return stream.max_time > two_weeks


device_streams = patient_streams.filter(
    device_id=device_id, 
    filter_function=most_recent_two_weeks
)

# recent_lfp_streams = patient_streams.filter(
#     category = "neural",
#     device_id=device_id,
#     filter_function = most_recent_two_weeks
# )

#define time window:
end_time = int(time.time())
start_time = end_time - 14*24*60*60 #current time minus 14 days (*24 hours * 60 minutes * 60 seconds)

stream_df = device_streams.get_stream_dataframe(
    start_time=start_time,
    end_time=end_time
)

#export
output_dir = "/Volumes/Study Files/emily_analysis/RuneWatch" #path to folder on VPN
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "testneural.json")
stream_df.to_json(output_path, orient="records", indent=2)
print(f"patient data exported to: {output_path}")