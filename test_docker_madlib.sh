#!/bin/sh
#
# Requirements:
#       - You must have docker and have docker container ('madlib') running
#
# REMARKS:
#       - Adjust HOST or/and PORT or SLEEP_TIME if necessary, but for this demo you don't need to change them
#
HOST="127.0.0.1"
PORT=9000
SLEEP_TIME=20

while true
do 
    echo
    curl http://$HOST:$PORT/madlib
    echo
    echo "Get MADLIB again in $SLEEP_TIME secs, pls. wait ... (or use Control-c to exit)"
    sleep $SLEEP_TIME
done