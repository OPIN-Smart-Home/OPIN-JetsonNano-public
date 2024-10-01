import json
import requests

def is_ip_assigned(device_ip):
    url = 'http://localhost:1880/flows'
    response = requests.get(url)
    assigned = False
    if response.status_code == 200:
        flows = response.json()
        for flow in flows:
            if 'broker' in flow and flow['broker'] == device_ip:
                assigned = True
                break
    else:
        return "error"
    return assigned
        
def generate_config_json(json_file, device_id, device_ip):
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    for data in json_data:
        if data["type"] == "mqtt-broker":
            data["id"] += device_id
            data["broker"] =  device_ip
    return json_data

def generate_flow_json(json_file, access_id, device_type, device_id, device_ip, rtsp = None, customer_id = None, name = None, cost = 0):
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    for data in json_data:
        data["id"] += device_id
        if "g" in data:
            data["g"] += device_id
        if "nodes" in data:
            new_nodes = []
            for node in data["nodes"]:
                node += device_id
                new_nodes.append(node)
            data["nodes"] = new_nodes
        if "scope" in data:
            new_scope = []
            for scope in data["scope"]:
                scope += device_id
                new_scope.append(scope)
            data["scope"] = new_scope
        if "wires" in data and data["wires"]:
            if len(data["wires"]) > 1:
                new_wire = []
                for wire in data["wires"]:
                    for i in range(len(wire)):
                        wire[i] += device_id
            else:
                new_wire = []
                for w in data["wires"][0]:
                    w += device_id
                    new_wire.append(w)
                data["wires"][0] = new_wire
        if data["type"] == "change" and data["name"] == "id":
            for rule in data["rules"]:
                if rule["p"] == "device_id":
                    rule["to"] = device_id
                elif rule["p"] == "device_ip":
                    rule["to"] = device_ip
                elif rule["p"] == "rtsp":
                    rule["to"] = rtsp
        if data["type"] == "ping":
            data["host"] = device_ip
        if data["type"] == "change" and data["name"] == "info" and device_type == "02":
            for rule in data["rules"]:
                if rule["p"] == "customer_id":
                    rule["to"] = customer_id
                elif rule["p"] == "name":
                    rule["to"] = name
                elif rule["p"] == "cost":
                    rule["to"] = cost
        if data["type"] == "change" and data["name"] == "arguments" and device_type == "05":
            for rule in data["rules"]:
                if rule["p"] == "path":
                    rule["to"] = access_id + "/devices/" + device_type + "/" + device_id + rule["to"]
        if data["type"] == "firebase-in" or data["type"] == "firebase-out" or data["type"] == "firebase-get":
            if data["name"] == "auto off ON" or data["name"] == "auto off OFF":
                data["path"] = access_id + "/add_on"
            else:
                data["path"] = access_id + "/devices/" + device_type + "/" + device_id + data["path"]
        if data["type"] == "mqtt in" or data["type"] == "mqtt out":
            data["topic"] = "opin/" + device_id + data["topic"]
            data["broker"] += device_id
    return json_data

def get_flow_id(label):
    url = 'http://localhost:1880/flows'
    response = requests.get(url)
    if response.status_code == 200:
        flows = response.json()
        for flow in flows:
            if 'label' in flow and flow['label'] == label:
                return flow["id"]
    else:
        return "error"

def get_nodes(flow_id):
    url = 'http://localhost:1880/flow/' + flow_id
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "error"
