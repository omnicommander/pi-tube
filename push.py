from datetime import datetime
import requests
import psutil
import json
import yaml
import os


with open('/home/pi/OC-DigitalSignage/config.yaml', 'r') as f:
    signage_config = yaml.safe_load(f)


data = {
    'timestamp': datetime.now().__str__()
}


print(json.dumps(data))
