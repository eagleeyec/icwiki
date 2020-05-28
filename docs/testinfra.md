# TestInfra

A collection of tests suitable for various services

## Openresty

    # File: test_openresty.py
    def test_openresty_syntax(host):
        cmd = host.command('/usr/local/openresty/nginx/sbin/nginx -t')
        assert cmd.rc == 0

    def test_openresty_running_and_enabled(host):
        openresty = host.service("openresty")
        assert openresty.is_running
        assert openresty.is_enabled
