#!/bin/bash
#
# Uploads latest.jpg from All Sky Camera to SuffolkSky.com
#
# This is run via cron every 5 minutes
# */5 * * * * /home/pi/uploadsuffolksky.sh

# use sftp to copy the latest.jpg to suffolksky.com

sftp -i PATHTOAWS.pem USER@HOST:/home/USER/stack/wordpress/ <<< $'put /var/www/html/allsky/images/latest.jpg'

