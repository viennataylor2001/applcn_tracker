import psutil
import json
import time
from collections import defaultdict

# Store application usage data
app_usage_data = defaultdict(int)

# Track running applications every 5 seconds
def track_app_usage():
    try:
        while True:
            for proc in psutil.process_iter(['name']):
                app_name = proc.info['name']
                app_usage_data[app_name] += 5  # Assuming tracking every 5 seconds
            time.sleep(5)
    except KeyboardInterrupt:
        # When you stop the script, save the data to a JSON file
        save_app_usage()

def save_app_usage():
    with open("app_usage.json", "w") as f:
        json.dump(app_usage_data, f)
    print("Application usage data saved to app_usage.json")

# Run the app tracking
track_app_usage()
