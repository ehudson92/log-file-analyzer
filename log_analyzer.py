import re
from collections import Counter

# Prompt for log file path
log_file = input("Enter path to your log file (e.g., access.log): ")

top_ips = Counter()

with open(log_file, 'r') as file:
    for line in file:
        # Regex to match standard IPv4 at the start of each line
        match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ip = match.group(1)
            top_ips[ip] += 1

# Print results
if top_ips:
    print("\nTop 5 IP addresses making requests:")
    for ip, count in top_ips.most_common(5):
        print(f"{ip}: {count} requests")
else:
    print("⚠️ No IP addresses found in the log file.")
