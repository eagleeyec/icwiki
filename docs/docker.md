# Docker

## Setup a local registery

    docker run -d -p 5000:5000 --restart=always --name registry  -v  ~/registry:/var/lib/registry  registry:2

## Setup a new machine

    
	#!/bin/bash
	yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
	yum install -y docker-ce python3-pip
	pip3 install docker-compose
	systemctl enable --now docker

	# Options
    #yum install -y docker-ce-19.03.5 python3-pip
    #groupadd docker # This is so you can add other non-root users to the docker group to allow them to run docker commands
    #usermod -aG docker appuser # This is how you allow appuser to run docker commands
    
