#!/usr/bin/env bash

JSONPATH="/home/pi/OC-DigitalSignage/json"          	    # path for json file from server.
VIDEOPATH="/home/pi/OC-DigitalSignage/video"                  # path for fetch to store video mp4 files
fetchLog="/home/pi/OC-DigitalSignage/fetch.log"               # path for logging
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`               # timestamp formatting for logger
URL="http://34.193.150.151/pi_callHome.php?id="     # url to server for requests
AUTHOR="Eric Bradshaw bradshaw@omnicommander.com"      # author
PI_UID=""   	                    # ID for this PI machine
VERSION=1.6                                        # revision number
