# Ngrok

This service allows you to setup a public endpoint and proxy messages sent there to your laptop. You can see the request data. Makes prototyping API interfaces very fast. 

# Setup 

    brew install ngrok

# Usage examples

    # Allow a fellow developer to access a database on your laptop
    ngrok tcp 3306 --cidr-allow 192.168.1.5/32

    # Allow incoming webhooks, pointing to a service on 8001 locally on your laptop
    ngrok tcp 8001
