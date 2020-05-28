# Log Analysis

## Apache

Count discrete status codes:

    cat /var/log/httpd/*log | awk -F '"' '{print $3}' | awk '{print $1}' | sort | uniq -c
