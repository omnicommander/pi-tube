#!/usr/bin/python3

# ================================= #
# sudo python3 install.py           #
# ================================= #
import os
import subprocess as sp

# Check if user is root --------------------------------------------- #
if os.geteuid() != 0:
    exit('Please run install with sudo! sudo ./install ')

# Go to root directory ---------------------------------------------- #
os.chdir('/')

# Self-update ------------------------------------------------------- #
while True:
    yn = input('Can I please run my self-update? (y/n)')[0]

    if yn == 'y' or 'Y':
        sp.call(['apt', 'update', '&', 'apt', 'dist-upgrade'])

        break

    elif yn == 'n' or 'N':
        print('''\n Hey! I may not run correctly, so you had your
        chance and you blew it.\n''')

        break

    else:
        print('''Please answer y or n or I will ask you again, and you
        don\'t want me wasting your time.\n''')

# Test for jq ------------------------------------------------------- #
try:
    sp.call(['jq'])

except:
    print('''I require jq but it\'s not installed, so I am installing
    it now.\n''')

    sp.call(['apt-get', 'install', 'jq', '-y'])

# Test for youtube-dl ----------------------------------------------- #
try:
    sp.call('youtube-dl')

except:
    print('''I require youtube-dl but it\'s not installed, so I am
    installing it now.\n''')

    sp.call([
    'curl',
    '-L',
    'https://yt-dl.org/downloads/latest/youtube-dl',
    '-o',
    '/usr/local/bin/youtube-dl'
    ])

# Test for bc ------------------------------------------------------- #
try:
    sp.call(['bc'])

except:
    print('''I require bc, but it\'s not installed, so I am installing
    it now. \n''')

    sp.call(['apt-get', 'install', 'bc', '-y'])

print('''*** Dependencies successfully installed. Now installing
configuration files ***\n''')

print('Installing desktop configuration files...\n')
sp.call(['tar', '-xvf' '/home/pi/OC-DigitalSignage/config.tar'])

print('Installing Raspian boot configuration files... \n')
sp.call(['tar', '-xvf', '/home/pi/OC-DigitalSignage/booter.tar'])

# User configuration ------------------------------------------------ #
while True:
    yn = input('Do you wish to set the PI_UID now? (y/n)')[0]

    if yn == 'y' or 'Y':
        sp.call(['nano', '/home/pi/OC-DigitalSignage/config.sh'])
    elif yn == 'n' or 'N':
        print('You can edit the config.sh at any time.\n Bye for now!')
    else:
        print('Please answer yes or no or I will ask you again.\n')

ssid = input('')