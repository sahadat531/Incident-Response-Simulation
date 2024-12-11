
import re
from datetime import datetime

def analyze_logs(log_file):
    with open(log_file, "r") as file:
        logs = file.readlines()

    incidents = []
    for log in logs:
        match = re.search(r"File (\w+): (.+) at (.+)", log)
        if match:
            action, file_path, timestamp = match.groups()
            incidents.append({
                "action": action,
                "file_path": file_path,
                "timestamp": datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
            })

    print("\n=== Incident Report ===")
    for incident in incidents:
        print(f"{incident['timestamp']} - {incident['action']} detected on {incident['file_path']}")
    print("\nTotal Incidents:", len(incidents))

if __name__ == "__main__":
    analyze_logs("incident_logs.txt")
