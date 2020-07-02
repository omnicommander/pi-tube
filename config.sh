JSONPATH="/home/pi/OC-DigitalSignage/json"          	    # path for json file from server.
VIDEOPATH="/home/pi/OC-DigitalSignage/videos"                  # path for fetch to store video mp4 files
fetchLog="/home/pi/OC-DigitalSignage/fetch.log"               # path for logging
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`               # timestamp formatting for logger
URL="http://34.193.150.151/pi_callHome.php?id="     # url to server for requests
AUTHOR="Eric Bradshaw bradshaw@omnicommander.com"      # author
PI_UID="TestPi"   	                    # ID for this PI machine
VERSION=1.4                                         # revision number
BUCKETURL="https://digitalsignagebucket.s3.us-east-2.amazonaws.com/" # URL for the bucket