#!/bin/python3
# A super simple script to return 200/500 depenging on if anything monit check is in a failed state
# Expected to be consumed by a load balancer
from subprocess import PIPE, run
from flask import Flask, json

api = Flask(__name__)

@api.route('/monit-health', methods=['GET'])
def get_monit_health():
  completed = run('/usr/bin/curl -s -u admin:monit localhost:2812/_report | grep down | grep "0.0%"', stdout=PIPE, shell=True)
  if completed.returncode == 0:
    return 'OK'

  return 'Failed', 500

if __name__ == '__main__':
    api.run()