#!/bin/bash

# Define the host you are testing
HOST_URL="http://192.168.49.2:30001/"

# Define the path to your Locust file
LOCUST_FILE_PATH="/home/ayyzenn/Desktop/fyp_work/sock_shop/load/main.py"

# Enter an endless loop
while true; do
    # Get the current minute
    CURRENT_MINUTE=$(date +%M)

    # Calculate minutes until the next hour
    MINUTES_UNTIL_NEXT_HOUR=$((60 - 10#$CURRENT_MINUTE))

    # Calculate minutes until the next 30 minutes
    MINUTES_UNTIL_NEXT_30_MIN=$((30 - (10#$CURRENT_MINUTE % 30)))

    # Calculate minutes until the next 15 minutes
    MINUTES_UNTIL_NEXT_15_MIN=$((15 - (10#$CURRENT_MINUTE % 15)))

    # Check if exactly 5 minutes are left in the current hour or it's a 30 or 15-minute interval
    if [ "$MINUTES_UNTIL_NEXT_HOUR" -eq 1 ] || [ "$MINUTES_UNTIL_NEXT_30_MIN" -eq 0 ] || [ "$MINUTES_UNTIL_NEXT_15_MIN" -eq 0 ]; then
        # Set specific values for the peak traffic time
        USERS=500  # Example specific number of users for peak times
        HATCH_RATE=500  # Example specific hatch rate for peak times
        RUN_TIME="5m"  # Run for 5 minutes, ensuring it doesn't overflow into the next hour
        echo "Running Locust for peak traffic simulation with $USERS users at a hatch rate of $HATCH_RATE for $RUN_TIME..."
        sleep 1
    else
        # Generate random values for users, hatch rate, and run time for normal traffic time
        USERS=$((RANDOM % 30 + 60))  # Random between 60 and 89
        HATCH_RATE=$((RANDOM % 5 + 4))  # Random between 4 and 8
        RUN_TIME="$((RANDOM % 5 + 1))m"  # Random between 1 and 5 minutes
        echo "Running Locust with $USERS users at a hatch rate of $HATCH_RATE for $RUN_TIME..."
    fi

    # Run Locust with the generated or set parameters
    locust --host $HOST_URL -f $LOCUST_FILE_PATH --headless --users $USERS --spawn-rate $HATCH_RATE --run-time $RUN_TIME
done
