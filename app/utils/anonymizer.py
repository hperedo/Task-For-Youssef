import hashlib

def anonymize_patient_id(patient_id: str) -> str:
    return hashlib.sha256(patient_id.encode()).hexdigest()
