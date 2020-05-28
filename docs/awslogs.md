# AWSLogs

Below are some examples I have put together for using this excellent tool for working with AWS CloudWatch Logs:

    https://github.com/jorgebastida/awslogs

Sadly and annoyingly AWS CloudWatch Logs filters do not support case insensitivity

## Syntax

    ? - Shows that the filter value is optional

## Find errors from /var/log/messages
    awslogs get /var/log/messages --start='4 hours' --watch --filter="?ERROR ?Error ?error ?FAIL ?Fail ?fail ?FATAL ?Fatal ?fatal"

## Tail Flow logs ignoring traffic starting from outside and late returning TCP packets

    awslogs get flow-logs --start='1 hours' --watch -f  REJECT | awk '$6 ~ /^10\./ && $8 != 5666 && $8 != 443'
