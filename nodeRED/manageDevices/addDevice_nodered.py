import sys
import json
import requests
from utils import *

# Device UID
with open('/usr/src/node-red/uid.txt', 'r') as file:
    access_id = file.read().strip()

# User input from mobile app
device_id = sys.argv[2].split(":")[1]
device_ip = sys.argv[3].split(":")[1]

url = 'http://localhost:1880/flow'
headers = {'Content-Type': 'application/json'}

DIR_PATH = "/usr/src/node-red"

if is_ip_assigned(device_ip) == True:
    json_msg = {
        "response": "failed",
        "message": "duplicate ip"
    }
    print(json.dumps(json_msg))
    raise ValueError("duplicate device_ip")

device_type = device_id.split("_")[0]
if device_type == "IPCamera":
    device_type = "05"
    flow_file = DIR_PATH + "/template/ipCamera.json"
    rtsp = sys.argv[4].split(":")[1]
    flow = generate_flow_json(flow_file, access_id, device_type, device_id, device_ip, rtsp)
    flow_payload = {
        "label": device_id,
        "nodes": flow
    }
else:
    if device_type == "SmartLamp":
        device_type = "01"
        flow_file = DIR_PATH + "/template/smartLamp.json"
        flow = generate_flow_json(flow_file, access_id, device_type, device_id, device_ip)
    elif device_type == "kWhMeter":
        device_type = "02"
        flow_file = DIR_PATH + "/template/kwhMeter.json"
        customer_id = sys.argv[4].split(":")[1]
        name = sys.argv[5].split(":")[1]
        cost = sys.argv[6].split(":")[1]
        flow = generate_flow_json(flow_file, access_id, device_type, device_id, device_ip, customer_id, name, cost)
    elif device_type == "ACControl":
        device_type = "03"
        flow_file = DIR_PATH + "/template/acControl.json"
        flow = generate_flow_json(flow_file, access_id, device_type, device_id, device_ip)
    elif device_type == "DoorLock":
        device_type = "04"
        flow_file = DIR_PATH + "/template/doorLock.json"
        flow = generate_flow_json(flow_file, access_id, device_type, device_id, device_ip)
    else:
        json_msg = {
            "response": "failed",
            "message": "invalid id"
        }
        print(json.dumps(json_msg))
        raise ValueError("Invalid device_id")

    config_file = DIR_PATH + "/template/config.json"
    config = generate_config_json(config_file, device_id, device_ip)
    flow_payload = {
        "label": device_id,
        "nodes": flow,
        "configs": config
    }

response = requests.post(url, json= flow_payload, headers = {'Content-Type': 'application/json'})
if response.status_code == 200:
    json_msg = {
        "response": "success",
        "message": "new device added successfully"
    }
    print(json.dumps(json_msg))
else:
    json_msg = {
        "response": "failed",
        "message": response.json()["message"]
    }
    print(json.dumps(json_msg))
