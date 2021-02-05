# CertBot by Let's Encrypt

This is a tool to create a free SSL certificate. The only snag is that it lasts just 3 months. The tool can be automated to renew certificates, so long as you can point requests for a (sub)domain to a server where certbot is running or give it write permission to your DNS service.


## Manual renewal

If neither of the above are possible with your security archetecture you can renew the SSL certificates manually by setting up TXT type DNS records manually. Here is my winning command that puts all output in the CWD.

	certbot certonly --manual --preferred-challenges dns --config-dir config --work-dir work --logs-dir logs -d "*.example.com" -d "*.dev.example.com"