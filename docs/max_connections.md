# Max Connections

Setting that increase the maximum number of concurrent conections a service can take

## CentOS7

the property somaxconn is one limit that affects how many connections a server can handle. You can see the current limit with this command:

    cat /proc/sys/net/core/somaxconn

The default is 128 but you can set it much higher like this:

    sysctl -w net.core.somaxconn=4096

## Docker

Add the following to a docker compose file

    services:

      app:
        image: xyz:latest
        sysctls:
         - net.core.somaxconn=4096

You can confirm it worked like this:

    docker exec -ti container_name cat /proc/sys/net/core/somaxconn

## Uwsgi

Here there is a default setting of 128 also. Change in the ini file like this:

    # uwsgi.ini
    listen = 4096

## Testing

For the queue size (tcp_max_syn_backlog) you can use:

    netstat netstat -ant | grep -c SYN_REC

## Reading list

* https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
* https://blog.cloudflare.com/syn-packet-handling-in-the-wild/
