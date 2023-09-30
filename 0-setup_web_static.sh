#!/bin/bash

# Update and install nginx if not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link (remove if it already exists)
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
config_path="/etc/nginx/sites-available/default"
config_content="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/server_name _;/a $config_content" $config_path

# Restart nginx
sudo service nginx restart

# Exit with success status
exit 0
