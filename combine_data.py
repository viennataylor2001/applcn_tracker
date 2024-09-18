import json

# Define the paths to your data files
app_usage_file = 'app_usage.json'
website_usage_file = 'website_usage.json'
combined_file = 'combined_usage.json'

# Function to load JSON data from a file
def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if not content:
                print(f"Warning: {file_path} is empty.")
                return {}
            return json.loads(content)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON.")
        return {}

# Load application usage data
app_usage_data = load_json(app_usage_file)

# Load website usage data
website_usage_data = load_json(website_usage_file)

# Combine the data
combined_data = {
    "applications": app_usage_data,
    "websites": website_usage_data
}

# Save the combined data to a new JSON file
with open(combined_file, 'w') as combined_file:
    json.dump(combined_data, combined_file, indent=4)

print(f"Combined data saved to {combined_file}")
