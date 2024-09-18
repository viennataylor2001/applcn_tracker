import time
import json
import psutil
import pygetwindow as gw
from datetime import datetime

# Function to track application usage
def track_app_usage(duration=3600):  # Default tracking for 1 hour
    app_usage = {}
    start_time = datetime.now()

    while (datetime.now() - start_time).total_seconds() < duration:
        try:
            # Get active window
            active_window = gw.getActiveWindow()

            if active_window:
                app_name = active_window.title or "Unknown"
                process_name = active_window.getProcessName()

                if process_name not in app_usage:
                    app_usage[process_name] = {"app_name": app_name, "time_spent": 0}

                # Increment time spent on the current active window
                app_usage[process_name]["time_spent"] += 1  # Add 1 second
        except Exception as e:
            print(f"Error tracking window: {e}")

        time.sleep(1)  # Sleep for 1 second between checks

    return app_usage

# Function to save app usage data to a JSON file
def save_usage_data(data, filename="app_usage.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main function to run the tracker
def main():
    print("Tracking applications for 1 hour...")
    usage_data = track_app_usage(3600)  # Track for 1 hour (3600 seconds)
    save_usage_data(usage_data)
    print(f"Data saved to 'app_usage.json'")

if __name__ == "__main__":
    main()
