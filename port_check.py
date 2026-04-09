import socket

# A list of our server IPs, now including your specific gateway
targets = ["127.0.0.1", "8.8.8.8", "1.1.1.1", "10.0.0.1", "192.168.1.1"]

# The Efficiency Engine: Loop through each IP in the list
for ip in targets:
    print(f"\n--- Checking Server: {ip} ---")
    
    # Create the socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a 1-second timeout so the script doesn't hang on dead IPs
    s.settimeout(1)
    
    # Knock on Port 22 (SSH)
    result = s.connect_ex((ip, 22))
    
    # The Decision Gate
    if result == 0:
        print(f"SUCCESS: Port 22 is OPEN on {ip}")
    else:
        print(f"FAILED: Port 22 is CLOSED on {ip}")
        
    # Close the socket to clean up resources
    s.close()
