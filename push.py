from datetime import datetime
import subprocess as sp
import requests
import socket
import psutil
import shutil
import json
import yaml
import os


# Load config
with open('/home/pi/OC-DigitalSignage/config.yaml', 'r') as f:
    signage_config = yaml.safe_load(f)

# Build the object to push
data = {
    'timestamp': datetime.now().__str__(),
    'PI_UID': signage_config['pi_id'],
    'serialId': '', #TODO Get the serial id of the pi
    'environmental': {
        'tempC': round(psutil.sensors_temperatures()['cpu_thermal'][0].current, 2),
        'tempF': round(psutil.sensors_temperatures(fahrenheit=True)['cpu_thermal'][0].current, 2),
        'cpu_percent': psutil.cpu_percent(interval=5),
        'storageUsed': '{}GB'.format(round(shutil.disk_usage('/').used / 1_073_741_824, 2)),
        'storageAvail': '{}GB'.format(round(shutil.disk_usage('/').free / 1_073_741_824, 2))
    },
    'physical': {
        'lsVideo': os.listdir(signage_config['video_directory']),
        'jsonInv': 'Version 1.6 is not storing JSON'
    },
    'pi-config': {
        'host_ip': os.popen('hostname  -I | cut -f1 -d\' \'').read()[:-1],
        'WIFI': '', #TODO Get name of the current wifi network
        'version': signage_config['version']
    },
    'services': {
        'uptime_since': os.popen('uptime -s').read()[:-1],
        'last_cron': open('/home/pi/OC-DigitalSignage/last_cron',
                          'r').readline(),
        'vlc': 'running' if 'mpv' in [x.info['name'] for x in psutil.process_iter(['name'])] else 'stopped'
    }
}

# Push the JSON object
r = requests.post(url='http://34.193.150.151/dat-receive.php',
              headers={'Content-Type': 'application/json'},
              data=json.dumps(data))

print(r.text)

with open('/home/pi/OC-DigitalSignage/last_cron', 'w') as f:
    f.write(str(datetime.now()))
