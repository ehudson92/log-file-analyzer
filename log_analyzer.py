import re
from collections import Counter

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()

        ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
        failed_logins = []
        ip_addresses = []

        for line in logs:
            ip_match = ip_pattern.search(line)
            if ip_match:
                ip = ip_match.group()
                ip_addresses.append(ip)
                if "failed" in line.lower() or "unauthorized" in line.lower():
                    failed_logins.append(ip)

        print("\n===== LOG ANALYSIS REPORT =====")
        print(f"Total log entries: {len(logs)}")
        print(f"Unique IPs detected: {len(set(ip_addresses))}")
        print(f"Failed login attempts: {len(failed_logins)}")

        if failed_logins:
            print("\nTop 5 IPs with failed attempts:")
            for ip, count in Counter(failed_logins).most_common(5):
                print(f" - {ip}: {count} times")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    log_file = input("Enter path to log file (e.g., system.log): ").strip()
    analyze_log(log_file)
