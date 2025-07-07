from runeq import initialize
from runeq.resources.stream_metadata import get_patient_stream_metadata

initialize()
#From Rune Labs API documentation: 
patient_id = "" #PATIENT ID
patient_streams = get_patient_stream_metadata(patient_id)
print(f'Found {len(patient_streams)} streams')