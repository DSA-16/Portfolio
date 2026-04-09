import subprocess
import json

# --- Phase 1: Log Interrogation ---

result = subprocess.run(
    ["grep", "Failed password", "/var/log/titan_sim/auth_sim.log"],
    capture_output=True,
    text=True
)

raw_output = result.stdout

# --- Phase 2: Data Parsing ---

lines = raw_output.split('\n')


attacker_ips = []


for line in lines:

    if line:
        # Split the line by spaces. In this specific log format, the IP is the 11th item (index 10)
        ip = line.split(" ")[10]
        attacker_ips.append(ip)

# --- Phase 3: The Export ---

alert_data = {
    "alert_type": "Brute Force",
    "attacker_ips": attacker_ips
}


with open("threat_report.json", "w") as file:
    json.dump(alert_data, file, indent=4)

print("[*] Operation complete. Threat intel saved to threat_report.json")
