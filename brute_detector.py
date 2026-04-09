# Initialize the Counter
attack_count = 0

# The Double-Door Logic: Open the dirty log (read) and the clean report (write)
with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:
        
        # The Conveyor Belt: Read the log line by line
        for line in log_file:
            
            # The Signature Search: Looking for exact case matches
            if "Failed password" in line:
                
                # The Save: Write that specific line to our new report
                report_file.write(line)
                
                # Increment the counter
                attack_count = attack_count + 1

# The Final Report (Must be flush left so it only prints once at the very end)
print(f"[*] Audit Complete. Extracted {attack_count} threat signatures to brute_report.txt")
