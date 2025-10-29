import re
from collections import Counter

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            log_data = file.readlines()
        
        print("✅ File loaded. First line preview:", log_data[0] if log_data else "Empty file")
        
        # ✅ Updated regex to catch IPs at the start of the line
        ip_pattern = re.compile(r'(\d{1,3}(?:\.\d{1,3}){3})')
        ips = []

        for line in log_data:
            match = ip_pattern.search(line)
            if match:
                ips.append(match.group(1))

        if ips:
            ip_counts = Counter(ips)
            print("\nTop 5 IP addresses making requests:")
            for ip, count in ip_counts.most_common(5):
                print(f"🔹 {ip}: {count} requests")
        else:
            print("⚠️ No IP addresses found in the log file.")

    except FileNotFoundError:
        print("❌ File not found. Please check your path.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# 🧪 Main program
if __name__ == "__main__":
    file_path = input("Enter path to your log file (e.g., access.log): ").strip()
    analyze_log(file_path)
