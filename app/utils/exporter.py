import csv
import json
from io import StringIO
from typing import List, Dict
from app.db.encryption import decrypt_data

def export_to_csv(data: List[Dict], exclude_phi: bool = True) -> StringIO:
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys() if data else [])
    writer.writeheader()
    
    for row in data:
        if exclude_phi:
            row = {k: v for k, v in row.items() if not k.endswith("_id")}
        writer.writerow(row)
    
    output.seek(0)
    return output

def export_to_json(data: List[Dict], exclude_phi: bool = True) -> str:
    if exclude_phi:
        data = [{k: v for k, v in item.items() if not k.endswith("_id")} for item in data]
    return json.dumps(data)

