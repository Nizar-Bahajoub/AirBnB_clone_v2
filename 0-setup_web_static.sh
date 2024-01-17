#!/usr/bin/env bash
# Set up web server

sudo apt-get -y update > /dev/null 2>&1
sudo apt-get -y install nginx > /dev/null 2>&1
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
echo "Hello world" | sudo tee /data/web_static/releases/test/index.html > /dev/null 2>&1
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '0i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
