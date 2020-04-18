# Diagnostics

## Scripts for analysing CentOS 7 servers

### Assess RAM hungry processes
Got OOM errors but not sure why? Setup this script to capture extra info:

    #!/bin/bash
    # filename=pmem.sh
    #
    # Script to capture memory hungry processes when system memory is low
    # Run the script like this to put into the background
    # ./pmem.sh &
    # disown

    # Create logs if the system has less than this value of free memory
    # Integer value in MegaBytes
    low_memory_threshold=100

    function capture() {
        free=$(free -m | awk '/Mem/{print $4}')

        if [[ $free -lt $low_memory_threshold ]]; then
           echo "$(date) - Free=${free}M"
           ps -o pid,user,%mem,command ax | sort -b -k3 -r | head -n 15
        fi
    }

    function loop() {
        while true; do
            capture
            sleep 30
        done
    }

    loop >> /var/log/pmem.log
