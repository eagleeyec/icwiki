#!/usr/bin/env python3
""" Monit health check module

This is a python flask API app that turns the output from monit into something
a load balancer health check can consume by returning a 200 or 500 HTTP status
code depending on the output which is a feature missing from the monit web 
console afaict
"""

from subprocess import PIPE, run

import requests
from flask import Flask


app = Flask(__name__)


class Monit:
    """ Class Monit

    Monit outputs either text from the command line or a choice of text or XML
    from the web console.

    However neither the command line nor the web console output a return code 
    / http status code other than 0 / 200. That means that the output must be 
    parsed to determine if the node is in a healthy or unhealthy state.

    This class parses output from monit and returns json

    The class can be told to use either the monit web console or the command
    line to get the status which is then parsed by a common function
    """

    user = 'admin'
    password = 'monit'
    host = '127.0.0.1'
    port = 2812
    message = ''
    method = 'ui'

    def _get_report_from_ui(self):
        """ Get report frum UI

        This function calls on the monit web interface which listens by default with the class attruibutes stated above

        The return from this method is either boolean False or a multi line string as expected by parse_report_to_dict.
        """

        try:
            result = requests.get(f'http://{self.host}:{self.port}/_report', auth=(self.user, self.password))
        except:
            self.message = 'Unable to connect to moint UI'
            return False

        if result.status_code != 200:
            self.message = 'Unexpected http response code'
            return False

        return result.text
    
    def _get_report_from_command(self):
        """ Get report from command

        This functin calls the 'monit report' command to get the text based report that monit provides

        The return from this method is either boolean False or a multi line string as expected by parse_report_to_dict.
        """

        report_as_bytestring = run('monit report', stdout=PIPE, shell=True)

        if report_as_bytestring.returncode != 0:
            self.message = 'Failed response calling monit report command. Does this user have permission?'
            return False

        return report_as_bytestring.stdout.decode('utf8')

    def _parse_report_to_dict(self, report):
        """ Parse Monit report to dict

        Monit outputs a report in a text format with three columns:
        1. a status name
        2. a count of checks in that status
        3. a % of checks in that state

        Exmaple output:
        up:             9 (90.0%)
        down:           1 (10.0%)
        initialising:   0 (0.0%)
        unmonitored:    0 (0.0%)
        total:          10 services

        These reports have an empty trailing line

        This function returns a dict of status name to count, like this:
        {
            "down:":"1",
            "initialising:":"0",
            "total:":"10",
            "unmonitored:":"0",
            "up:":"9"
        }
        """ 

        report_dict = {}
        for line in report.split("\n"):
            fields = line.split()
            if len(fields) > 1:
                report_dict[fields[0].rstrip(':')] = fields[1]

        return report_dict

    def get_report_as_dict(self):
        """ Get report as dict

        This function is a wrapper for the private functions in this class.

        It returns a dict on success or boolean False on failure
        """

        report_as_dict = False

        if self.method == 'ui':
            report_as_string = self._get_report_from_ui()
        else:
            report_as_string = self._get_report_from_command()

        if report_as_string:
            report_as_dict = self._parse_report_to_dict(report_as_string)

        return report_as_dict



@app.route('/monit-report')
def monit_report():
    """ Monit report

    A json endpoint designed to be consumed by a health check.

    HTTP status code is 200 if the check successfully talked to monit and 
    found 0 services in the down state else HTTP status code is 500

    """
    monit = Monit()
    report = monit.get_report_as_dict()

    if type(report) is dict:
        if int(report['down']) == 0:
            return report
        else:
            return report, 500

    return {'Error': monit.message}, 500
