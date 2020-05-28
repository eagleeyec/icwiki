# NTP

## See the peers

    ntpq -nc peers

## Detect offset
ntpq -p shows the status of the ntp times. To get a delay of over 1 second do

    ntpq -p | awk '{print $8}' | grep '\.' | grep -v '0\.'

## Set NTP

    systemctl stop ntpd.service; ntpdate north-america.pool.ntp.org; ntpdate north-america.pool.ntp.org; systemctl start ntpd.service
