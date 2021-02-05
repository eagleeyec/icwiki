#!/bin/bash
# A simple script to push to slack

text=$1
host=$(hostname -I|xargs)

curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"${host}: ${1}\"}" https://hooks.slack.com/services/secret/api/token
