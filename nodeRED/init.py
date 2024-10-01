import json

# Device UID
with open('/usr/src/node-red/uid.txt', 'r') as file:
    access_id = file.read().strip()

# Open and read flows.json
json_file = "/usr/src/node-red/flows.json"
with open(json_file, 'r') as f:
    json_data = json.load(f)

# Change path
for data in json_data:
    if "path" in data:
        if data["path"] != "payload":
            data["path"] = access_id + data["path"]

# Save changes
with open(json_file, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)