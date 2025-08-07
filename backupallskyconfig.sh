#!/bin/bash
cd /home/pi/Projects/allskycamera-config-backup 

# dump the config to allskyconfig.bak
/home/pi/indi-allsky/config.py dump > /home/pi/Projects/allskycamera-config-backup/allskyconfiguration.bak

git add .
git commit -m "Backup"
git push origin main
