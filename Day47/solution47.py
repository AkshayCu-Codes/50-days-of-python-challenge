import json

# Function to save dictionary to JSON file
def save_json(data, filename="data.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

# Function to read dictionary from JSON file
def read_json(filename="data.json"):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data

# Input dictionary
names = {
    'name': 'Carol',
    'sex': 'female',
    'age': 55
}

# Save dictionary to JSON
save_json(names)

# Read dictionary from JSON
result = read_json()
print(result)