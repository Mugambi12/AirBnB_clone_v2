#!/usr/bin/env bash

# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

# Create necessary directories if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link (remove if it already exists)
rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Configure Nginx
printf %s "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;

    location /404 {
      root /var/www/html;
      internal;
    }
}
" > /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

# Exit with success status
exit 0
