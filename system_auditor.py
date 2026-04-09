import subprocess
import json


process_list = subprocess.run(["ps", "aux"], capture_output=True, text=True)


if "unauthorized_cryptominer" in process_list.stdout:
    print("[!] THREAT DETECTED: unauthorized_cryptominer found running in memory.")
    
    
    alert_data = {
        "event": "Unauthorized Process", 
        "severity": "High", 
        "process": "unauthorized_cryptominer"
    }

   
    with open("security_alert.json", "w") as file:
        json.dump(alert_data, file, indent=4)
        
    print("[*] Alert data successfully written to security_alert.json")

else:
    print("[*] System clean. No unauthorized processes detected.")
