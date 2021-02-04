# Monit syntax examples

## Service with pid and port
check process nginx with pidfile /var/run/nginx.pid
    if does not exist then 
        exec /usr/local/bin/slack_alert.sh "monit error: nginx service is not running" repeat every 100 cycles 
        else if succeeded then exec /usr/local/bin/slack_alert.sh "monit recovery: nginx service"
    if failed port 443 then 
        exec /usr/local/bin/slack_alert.sh "monit error: nginx service not listening on 443" repeat every 100 cycles
