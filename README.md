
# Omnitube for Raspberry PI 
Feb 2020 -- OMNICOMMANDER bradshaw@omnicommander.com

## Download NOObs for new PI Raspian
https://www.raspberrypi.org/downloads/

## Installation process instructions for Raspian OS Installation
https://www.raspberrypi.org/documentation/installation/noobs.md


## Clone script from repo ( this ) 

Change to pi's home directory

`cd ~` 

Clone this code

`git clone https://github.com/omnicommander/pi-tube`

## Run Omnitube install script
`cd /home/pi/pi-tube`

Must be sudo to run install 

`sudo ./install`

During the install, you will be prompted to enter the machine's ID. Be SURE you have it written down, so that you know it matches the one your customer has in TubeCommander. 

### The install script makes the following changes to the internal files within the Raspberry OS:
### DO NOT RUN THESE COMMANDS 

The following happens on install: 

* performs a core self-update, `apt-get upgrade -y`
* performs installation of jq `apt-get install jq`
* performs installation of bc `apt-get install bc`
* performs installation of youtube-dl 

### extracts /home/pi/pi-tar/config.tar to respective directories
* `home/pi/.config/lxsession/LXDE-pi/autostart`
* `home/pi/.config/pcmanfm/LXDE-pi/desktop-items-0.conf`
* `home/pi/.config/lxpanel/LXDE-pi/config`

### extracts /home/pi/pi-tube/booter.tar as follows
* `etc/lightdm/lightdm.conf`
* `etc/rc.local`
* `boot/cmdline.txt`

### Edits /home/pi/pi-tube/config.sh for PI_UID
* User directly edits the config.sh file to set PI_UID in `nano`


### WIFI Configuration
* SSID of Wifi router
* Password of WIFI connection


### Crontab configuration and installation
* backs up current crontab to mycron_old (if cron exists)
* Sets @reboot values to execute `fetch` on boot
* Sets q6h `fetch` to execute (refresh videos or update deletes)
* Sets q15m `push` to execute (sends data to server for heartbeat)


### Code Logic PSUEDO:
* ON BOOT `fetch` is executed, and `looper` daemon mode is run
* Cron job runs `/home/pi/pi-tube/fetch` every X hours 
 
 `fetch` then peforms the following actions:

 1. Build inventory of existing videos in `\video` directory/
 2. Request payload from server and build array of videos in campaign.
 3. Compares existing inventory to array of response videos.
 4. Downloads videos not in inventory to /videos directory.
 5. Deletes videos from inventory not in response videos.
 6. Stops vlc service ( if currently running ).
 7. Restarts vlc as service to loop videos in daemon mode.
 8. Exits gracefully until next cron call.

 ### Sample fetch.log entry
 `fetch` records to a logfile, for troubleshooting:  

 ```
 2019-12-26 15:45:01 Running Fetch Application - v1.3 by Scott Fleming
2019-12-26 15:45:01 Current inventory IDs: uzQ9kxs6RL8 M69uwmXb6GM X675jPEP9Fw 68cGgU2pSE0 dGStpJuIReM
2019-12-26 15:45:01 IDs from host: uzQ9kxs6RL8 M69uwmXb6GM X675jPEP9Fw 68cGgU2pSE0 dGStpJuIReM
2019-12-26 15:45:01 Found differences: 
2019-12-26 15:45:01 count of inventory: 0 1 2 3 4
2019-12-26 15:45:01 Starting at 6
2019-12-26 15:45:01 killing VLC
2019-12-26 15:45:01 run vlc
2019-12-26 15:45:01 Running cvlc /home/pi/pi-tube/video OmniTube
```

### New in 1.3 -- Push function

`push` peforms the following functions/actions

* obtain CPU temperature (C/F)
* obtain CPU ultilization in percentile (3.43%)
* obtain SD Card storage used in MB
* obtain SD Card storage available in GB
* obtain listing of mp4 files in video directory
* obtain listing of values in json file 
* obtain own ip address (future reference)
* obtain SSID/Password for Wifi connection (future reference)
* obtain VLC status (running/stopped)
* obtain machine uptime (timestamp) -- since last reboot.

`push` issues a POST command to server with json payload of data and PI_UID identifier.
Server captures POST and stores in PUSH Mysql table, using UPDATE ON DUPLICATE KEY to preserve record.


### TODO:
* youtube-dl update script and cron configuration
* Raspian update script and cron configuration
* Analytics build of reporting for billing/review purposes.
* Asset notification functions, consider email, text-messaging or through server dashboard.
* Whatever else this mad scientist can think up while pondering the madness.

