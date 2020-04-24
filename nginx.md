# Nginx

## Nginx return string internally

	location = /ping {
        access_log off;
        add_header Content-Type "text/plain";
        return 200 "pong\n";
    }
