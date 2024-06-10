#!/bin/bash

# Define the host you are testing
HOST_URL="http://192.168.49.2:30001/"

# Define the path to your Locust file
LOCUST_FILE_PATH="/home/rimsha/Desktop/fyp/final_submission/test_files/maintest_try.py"


# Enter an endless loop
while true
do
        
        echo "test running"
    
        # Generate random values for users, hatch rate, and run time for normal traffic time
        USERS=$((RANDOM % 30 + 60))  # Random between 20 and 69
        HATCH_RATE=$((RANDOM % 5 + 4))  # Random between 1 and 10
        # Random run time, for example, or set as needed
        RUN_TIME="$((RANDOM % 3 + 1))m"

        

        echo "Running Locust with $USERS users at a hatch rate of $HATCH_RATE for $RUN_TIME..."
    

        # Run Locust with the generated or set parameters
        locust --host $HOST_URL -f $LOCUST_FILE_PATH  --users $USERS --spawn-rate $HATCH_RATE --run-time $RUN_TIME

done