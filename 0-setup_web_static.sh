#!/bin/bash

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
sudo sed -i '/^\tlocation \/ {/a\
\t\talias /data/web_static/current/;' "$config_file"

# Restart Nginx
sudo service nginx restart

exit 0
