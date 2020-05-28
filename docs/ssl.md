# SSL

## Self signed setup

### Ubuntu
* apt-get install ca-certificates
* Place the file at /usr/local/share/ca-certificates/name.of.cert.crt
* update-ca-certificates

### CentOS

### RancherOS
* Append the certificate to /etc/ssl/certs/ca-certificates.crt
* restart the service/server

### Docker
* Place the file at /etc/docker/certs.d/name.of.cert[:port]/ca.crt
* No need to restart the service
