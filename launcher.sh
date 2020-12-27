#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/Documents/gitFromSelf/bellController
sleep 20
python3 server.py
cd /