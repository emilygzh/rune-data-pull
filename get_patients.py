

from runeq import initialize
from runeq.resources.patient import get_all_patients

initialize()

patients = get_all_patients()

for patient in patients:
    print(f"Patient ID: {patient.id}")
    if patient.devices:
        device = patient.devices[0]
        print(f"Patient Device: {device.id}") #fix thissssss
