"""Get patients and hospitals, then schedule appointments based on priorities.

url = https://fde-healthcare-production.up.railway.app/
get patient from path = '/patients'
get triage from path = '/triage' data=(patient_id, condition)
get hospitals from path = '/hospitals'
create schedule with schedule_path = '/schedule' data=(patient_id, specialty, hospital_id)
    subject to hospital specialty, utilization, and patient priority
"""

import json
from collections import defaultdict

import requests


class Client:
    """Client for interacting with the healthcare API."""

    url: str
    patients_path = "/patients"
    triage_path = "/triage"
    hospitals_path = "/hospitals"
    schedule_path = "/schedule"

    def __init__(self, url: str) -> None:
        """Initialize client."""
        self.url = url

    def get_patients(self) -> list[dict]:
        """Get patients."""
        response = requests.get(self.url + self.patients_path)
        return response.json()

    def get_triage(self, patient_id: str, condition: str) -> dict:
        """Get diagnosis for a patient."""
        data = {
            "patient_id": patient_id,
            "condition": condition,
        }
        response = requests.post(url=self.url + self.triage_path, json=data)
        return response.json()

    def get_hospitals(self) -> list[dict]:
        """Get hospitals."""
        response = requests.get(self.url + self.hospitals_path)
        return response.json()

    def schedule_appointment(self, patient_id: str, specialty: str, hospital_id: str):
        """Schedule an appointment."""
        data = {
            "patient_id": patient_id,
            "specialty": specialty,
            "hospital_id": hospital_id,
        }
        response = requests.post(self.url + self.schedule_path, json=data)
        return response.json()


# create client
client = Client(url="https://fde-healthcare-production.up.railway.app")

# get patients
patients = client.get_patients()
print(f"Patients:\n{json.dumps(patients, indent=2)}")

# group patients by condition for referrals
referrals = defaultdict(list)
for p in patients:
    triage = client.get_triage(patient_id=p["patient_id"], condition=p["condition"])
    if triage.get("referral"):
        referrals[triage.get("referral")].append({**p, "priority": triage.get("priority")})
    else:
        print(f"No referral for patient {p['patient_id']}")
print(f"Referrals (unsorted):\n{json.dumps(referrals, indent=2)}")

# sort referrals by priority (higher first)
for k, v in referrals.items():
    referrals[k] = sorted(v, key=lambda x: x["priority"], reverse=True)
print(f"Referrals (sorted):\n{json.dumps(referrals, indent=2)}")

# get hospitals
hospitals = client.get_hospitals()
print(f"Hospitals:\n{json.dumps(hospitals, indent=2)}")

# schedule appointments based on hospital capacity and patient referrals
print("Scheduling appointments...")
for h in hospitals:
    specialties = h["specialties"]
    for s in specialties:
        if s in referrals:
            patients = referrals[s]
            while h["utilization"] < 1 and len(patients):
                p = patients.pop()  # get highest priority patient
                response = client.schedule_appointment(
                    patient_id=p["patient_id"],
                    specialty=s,
                    hospital_id=h["hospital_id"],
                )
                print(f"Scheduled: {response}")
