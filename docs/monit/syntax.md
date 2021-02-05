# Monit syntax examples

## Service with pid and port
check process nginx with pidfile /var/run/nginx.pid
    start program = "/usr/bin/systemctl start nginx"
    stop program = "/usr/bin/systemctl stop nginx"
    if does not exist then 
        exec /usr/local/bin/slack_alert.sh "monit error: nginx service is not running" repeat every 100 cycles 
        else if succeeded then exec /usr/local/bin/slack_alert.sh "monit recovery: nginx service"
    if failed port 443 then 
        exec /usr/local/bin/slack_alert.sh "monit error: nginx service not listening on 443" repeat every 100 cycles

## Host with SSL
check host somename with address 1.2.3.4
    if failed
            port 443
            protocol https
            http headers [Host: somename.com]
            request '/some/url'
            content == ''
            timeout 20 seconds
            with ssl options {selfsigned: allow}
    then exec /usr/local/bin/slack_alert.sh "monit error: somename site"
    repeat every 100 cycles

## Check program
check program somename path /usr/local/bin/somename.sh
  if status != 0 then 
    exec /usr/local/bin/slack_alert.sh "monit error: Helpful message" repeat every 100 cycles
    else if succeeded then exec /usr/local/bin/slack_alert.sh "monit recovery: Another helpful message"
