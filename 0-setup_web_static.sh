#!/usr/bin/env bash
# Deploy for web server

sudo apt-get -y update
sudo apt-get -y install nginx

# Creating the folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creating a fake HTML file
echo -e "
<html>
    <head></head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html

# symbolic link current linked to the test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of web_static/current/ to hbnb_static
sudo sed -i "/# Only/ i location /hbnb_static {\nalias /data/web_static/current;\n}"

# Restart the service
sudo service nginx restart
