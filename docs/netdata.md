# Netdata

## Install

	curl -s https://packagecloud.io/install/repositories/netdata/netdata/script.rpm.sh | sudo bash
	yum install netdata
	systemctl enable --now netdata

## Troubleshooting

### dbengine_global_errors

This has to do with netdata's database, not mysql. The solution is to add these lines to the global section of /etc/netdata/netdata.conf:

	page cache size = 128
    dbengine disk space = 512
