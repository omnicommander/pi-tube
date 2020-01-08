#!/usr/bin/env bash
TITLE=""                       # displays on lower right corner (empty for blank)
LOGOPATH=""            # omnicommander logo image (empty for blank or none)
JSONPATH="/home/pi/pi-tube/json"          	    # path for json file from server.
VIDEOPATH="/home/pi/pi-tube/video"                  # path for fetch to store video mp4 files
fetchLog="/home/pi/pi-tube/fetch.log"               # path for logging 
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`               # timestamp formatting for logger
URL="http://34.193.150.151/pi_callHome.php?id="     # url to server for requests
AUTHOR="Scott Fleming scott@omnicommander.com"      # author
PI_UID="OC_OMNITUBE_1"   	                    # ID for this PI machine
VERSION=1.3                                         # revision number
