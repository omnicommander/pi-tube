from pytube import YouTube
import logging as log
import requests
import yaml
import os

# Get the base directory of this file
BASEDIR = os.path.dirname(os.path.realpath(__file__))

# Load the necessary variables
with open('/home/pi/OC-DigitalSignage/config.yaml', 'r') as f:
    signage_config = yaml.safe_load(f)

pi_id = signage_config['pi_id']
json_directory = signage_config['json_directory']
log_directory = signage_config['log_directory']
video_directory = signage_config['video_directory']
server_url = signage_config['server_url']

# Set up logger
log.basicConfig(filename=os.path.join(log_directory, 'fetch.log'),
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=log.INFO)

# Create json and video dirs if they don't already exist
if not os.path.exists(video_directory):
    os.mkdir(video_directory)
    log.info('Created video directory')

# Get JSON data from server
try:
    response = requests.get(f'{server_url}{pi_id}')
    data = response.json()
except:
    log.error('Request failed, status {}'.format(response.status))
    log.info('Exiting')
    exit()

# Determine which videos are already downloaded
videos_to_download = []
for video in data:
    if not os.path.exists(os.path.join(video_directory, '{}.mp4'.format(video['video_title']))):
        videos_to_download.append(video)
    else:
        log.info('{}.mp4 is already downloaded'.format(video['video_title']))

# Download every video in list
for video in videos_to_download:
    # Connect to youtube
    try:
        yt = YouTube('https://youtube.com/watch?v={}'.format(video['youtube_id']))
    except:
        log.error('Failed to connect to \
                  https://youtube.com/watch?v={}'.format(video['youtube_id']))
        exit()


    # Download the video
    try:
        if yt.streams.filter(file_extension='mp4', res='1080p'):
            yt.streams.filter(file_extension='mp4',
                    res='1080p').first().download(output_path=video_directory,
                            filename=video['video_title'])
        elif yt.streams.filter(file_extension='mp4', res='720p'):
            yt.streams.filter(file_extension='mp4',
                    res='720p').first().download(output_path=video_directory,
                            filename=video['video_title'])
        else:
            raise
        log.info('Downloading {}.mp4'.format(video['video_title']))
    except:
        log.error('Failed to download https://youtube.com/watch?v={},\
                  {}').format(video['youtube_id'], video['video_title'])

# Delete videos 
for video in os.listdir(video_directory):
    if video not in [x['video_title'] + '.mp4' for x in data]:
        os.remove(os.path.join(video_directory, video))
        log.info(f'Removed {video}')

# Log inventory of videos
video_id_inventory = [x['youtube_id'] for x in data]
log.info('Current video ids: {}'.format(', '.join(video_id_inventory)))


# Run the looper
log.info('Running mpv')
os.system('killall mpv')
os.system('/home/pi/OC-DigitalSignage/looper')
