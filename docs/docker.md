# Docker

## Setup a local registery

    docker run -d -p 5000:5000 --restart=always --name registry  -v  ~/registry:/var/lib/registry  registry:2

## Setup a new machine

    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    yum install docker-ce-19.03.5 python3-pip
    pip3 install docker-compose
    systemctl start docker

## Reload daemon.json

	sudo kill -SIGHUP $(pidof dockerd)

This command reloads the config file without restarting the daemon