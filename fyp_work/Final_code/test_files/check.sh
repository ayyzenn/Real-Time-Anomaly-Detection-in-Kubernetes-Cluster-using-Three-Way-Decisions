#!/bin/bash

# Define the host you are testing
HOST_URL="http://192.168.49.2:30001/"

# Define the path to your Locust file
LOCUST_FILE_PATH="/home/rimsha/Desktop/fyp/Test_files/main_test5.py"

# Enter an endless loop
while true
do
    # Get the current minute
    CURRENT_MINUTE=$(date +%M)

    # Calculate minutes until the next hour
    MINUTES_UNTIL_NEXT_HOUR=$((60 - 10#$CURRENT_MINUTE))
    echo "$MINUTES_UNTIL_NEXT_HOUR"

    # Check if exactly 5 minutes are left in the current hour
    if [ "$CURRENT_MINUTE" -eq 7 ]; then
        echo "in if block"
        sleep 5
    else
       
        echo "in else block"
    fi
done