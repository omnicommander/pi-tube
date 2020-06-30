#!venv/bin/python3
from os import path
import configparser
import boto3
import json

# Load the config file
configparser = configparser.RawConfigParser()
configparser.read('digitalsignage.conf')

# Assign values from config
PI_ID = configparser.get('Signage Config', 'PI_ID')
video_dir = configparser.get('Signage Config', 'VIDEO_DIR')

def fetch(debug):
    # Read the data from the json file
    with open('videos.json', 'r') as f:
        data = f.read()
        data = json.loads(data)

        video_names = []

        for entry in data:
            video_names.append(data[entry])

    # Download every video file from the json file
    for video in video_names:
        if path.exists(f'{video_dir}/{video}'):
            pass
        else:
            if debug:
                print(f'\nDownloading {video}...\n')

            s3 = boto3.client('s3')
            s3.download_file('digitalsignagebucket', f'{PI_ID}/{video}', f'{video_dir}/{video}')


    # Print debug information
    if debug:
        print('\nFinished!\n')
        print('Files downloaded:')
        for video in video_names:
            print(video)
        print('\n')

if __name__ == '__main__':
    fetch(debug=True)
