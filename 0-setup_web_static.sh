#!/usr/bin/env bash
# Set up server file system for deployment

# Update and install nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Check if nginx is running, and start it if not
if ! sudo service nginx status | grep -q "active (running)"; then
    sudo service nginx start
fi

# Create directories if they don't exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create index.html with content
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Set permissions
sudo chown -R ubuntu:ubuntu /data/

# Check if the symbolic link already exists, and remove it if it does
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Check if the location block already exists in nginx config, and add if it doesn't
if ! sudo grep -q "location /hbnb_static" /etc/nginx/sites-available/default; then
    sudo sed -i '44i \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

# Restart web server
sudo service nginx restart
