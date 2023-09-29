#!/bin/bash

# Configures a web server for deployment of web_static.

# Nginx configuration file
nginx_conf=$(cat <<'EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
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
EOF
)

# Install Nginx
sudo apt-get install -y nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create index.html for test
echo "Holberton School Puppet" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership
sudo chown -R ubuntu:ubuntu /data/

# Create index.html for default site
echo "Holberton School Nginx" | sudo tee /var/www/html/index.html

# Create 404.html
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html

# Nginx default configuration
sudo bash -c "cat > /etc/nginx/sites-available/default <<EOL
$nginx_conf
EOL"

# Restart Nginx
sudo /etc/init.d/nginx restarts
