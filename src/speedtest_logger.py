import speedtest
import pandas as pd
import os
#import sqlite3
from datetime import datetime

# Test to see if cron is running script
log_path = "/home/donpi/projects/network_speed_logger/logs/debug.log"
with open(log_path, "a") as f:
    f.write(f"{datetime.now()} - Script started\n")

# Find project root
# Script is found in src/, project root is one level ip
script_dir = os.path.dirname(os.path.abspath(__file__))
#project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ensure data folder exists
data_folder = os.path.join(script_dir, "..", "data")
data_folder = os.path.abspath(data_folder)
os.makedirs(data_folder, exist_ok=True)

# CSV file path
csv_file = os.path.join(data_folder, "speed_data.csv")

# Ensure CSV exists with headers
'''if not os.path.isfile(csv_file):
    with open(csv_file, "w") as f:
        f.write("timestamp,download_mbps,upload_mbps,ping_ms\n")
'''
if not os.path.isfile(csv_file):
    df = pd.DataFrame(columns=["timestamp", "download_mbps", "upload_mbps", "ping_ms"])
    df.to_csv(csv_file, index=False)

#initialize
s = speedtest.Speedtest()
s.get_best_server()

# Run Test
download_speed = round(s.download() / 1_000_000, 2) # Mbps
upload_speed = round(s.upload() / 1_000_000, 2) # Mbps
ping = s.results.ping
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Test output
# print(download_speed, upload_speed, ping, timestamp)

# Create record
record = {
    'timestamp': timestamp,
    'download_mbps': download_speed,
    'upload_mbps': upload_speed,
    'ping_ms': ping
}

# Check if file exists to write header or not
file_exists = os.path.isfile(csv_file)

# Test if script reaches this point
with open(log_path, "a") as f:
    f.write(f"{datetime.now()} - Code reaches to_csv\n")

# Append to CSV
df = pd.DataFrame([record])
#df.to_csv(csv_file, mode='a', header=not file_exists, index=False)
df.to_csv(csv_file, mode="a", header=False, index=False)

print(f"Logged to CSV: ↓ {download_speed} Mbps | ↑ {upload_speed} Mbps | 🕒 {ping} ms")
