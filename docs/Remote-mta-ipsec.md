# Notes for setting up IPSEC to make a mail appear from a remote servers public address

## Ipsec config on the mta origin server end:
cat /etc/ipsec.d/mta-to-remote.conf

    config setup
        plutodebug=all
        plutostderrlog=/var/log/pluto.log
        protostack=netkey
        nat_traversal=yes
        virtual_private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:!172.16.0.0/12
        oe=off

    conn vmta1-to-remote-ip1
        authby=secret
        auto=start
        type=tunnel
        left=10.1.2.3 # Primary IP of eth0, which has an EIP attached
        leftid=54.55.56.57 # EIP public address attached to eth0 primary IP
        leftsubnet=10.1.2.4/32 # Secondary IP attached to eth0

        right=5.6.7.8 # Remote server public IP
        rightsubnet=0.0.0.0/0 # Not sure why


## IPSec config on remote mta server end:

cat /etc/ipsec.d/remote-to-mta.conf

    config setup
        plutodebug=all
        plutostderrlog=/var/log/pluto.log
        protostack=netkey
        nat_traversal=yes
        # Note that this is turned off on the remote server
        #	virtual_private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:!172.16.0.0/12
        oe=off

    conn remote-ip1-to-vmta1
        authby=secret
        auto=start
        type=tunnel
        left=5.6.7.8 # Remote server public IP
        leftid=5.6.7.8 # Remote server public IP
        leftsubnet=0.0.0.0/0 # Not sure why

        right=54.55.56.57 # EIP public address attached to mta eth0 primary IP
        rightsubnet=10.1.2.4/32 # Secondary IP attached to eth0
