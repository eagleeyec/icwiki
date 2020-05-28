# openresty

Openresty is nginx + lua. This means you can do script processing inside the webserver process. Openresty is faster than calling out to php-fpm or proxying to a backend uwsgi process.

## Install openresty

Setup the yum repo like below and yum install openresty

	$ yum install yum-utils
	$ yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo

See https://openresty.org/en/linux-packages.html

## Reload config inside a running container

    nginx -s reload

## Use a get param

Call this like /echo?code=red and it will print 'red' back

    location /echo {
        content_by_lua_block {
            ngx.say(ngx.var.arg_code)
        }
    }

## Redis in openresty

See https://github.com/openresty/lua-resty-redis
