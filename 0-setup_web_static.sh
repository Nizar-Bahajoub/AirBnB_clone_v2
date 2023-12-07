#!/usr/bin/env bash
# Set up web server

sudo apt-get -y update > /dev/null 2>&1
sudo apt-get -y install nginx > /dev/null 2>&1
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "Hello world" > /data/web_static/releases/test/index.html
CURRENT="/data/web_static/current"
if [ -L "$CURRENT" ]; then
    sudo rm "$CURRENT"
fi
sudo ln -s /data/web_static/releases/test/ "$CURRENT"
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "40i location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
