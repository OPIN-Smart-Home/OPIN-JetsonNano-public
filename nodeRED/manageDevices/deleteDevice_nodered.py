import sys
import json
import requests
from utils import *

# Device UID
with open('/usr/src/node-red/uid.txt', 'r') as file:
    access_id = file.read().strip()

# User input from mobile app
device_id = (sys.argv[2].split(":")[1]).split("}")[0]

DIR_PATH = "/usr/src/node-red"

flow_id = get_flow_id(device_id)
if not flow_id and flow_id == "error":
	json_msg = {
		"response": "failed",
		"message": "id not found"
	}
	print(json.dumps(json_msg))
	raise ValueError("device_id not found")

device_type = device_id.split("_")[0]
if device_type == "SmartLamp":
    device_type = "01"
elif device_type == "kWhMeter":
    device_type = "02"
elif device_type == "ACControl":
    device_type = "03"
elif device_type == "DoorLock":
    device_type = "04"
elif device_type == "IPCamera":
    device_type = "05"
else:
    json_msg = {
        "response": "failed",
        "message": "invalid id"
    }
    print(json.dumps(json_msg))
    raise ValueError("Invalid device_id")

device_path = access_id + "/devices/" + device_type + "/" + device_id

url = 'http://localhost:1880/flow/' + flow_id
headers = {'Content-Type': 'application/json'}
response = requests.delete(url, headers = {'Content-Type': 'application/json'})
if response.status_code == 204:
	json_msg = {
		"device_path": device_path,
		"response": "success",
		"message": "device has been deleted"
	}
	print(json.dumps(json_msg))
else:
	json_msg = {
		"response": "failed",
		"message": "delete device failed"
	}
	print(json.dumps(json_msg))
