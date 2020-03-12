# OpenScan

## Overview:
The Raspberry Pi + OpenScan Pi Shield can be used to control two independent stepper motors and a variety of different cameras (Pi Camera, DSLR - via GPhoto and external Cameras like Smartphone and others). The mechanism can be used in various forms (see for example https://www.thingiverse.com/thing:3050437 or https://www.thingiverse.com/thing:2944570 and it could be easily adapted to be used as a camera slider or in other mechanisms.

## Setup
In order to add the OpenScan functionality to an existing raspbian system and understand all the dependencies, here is a full step-by-step list of the setup:

`sudo apt-get update`

`sudo apt-get upgrade`

`mkdir -p /home/pi/shared/ui/data/old_flows && mkdir /home/pi/shared/log`

### PiCamera

`sudo apt-get install python3-picamera && sudo apt-get install python-picamera`

`sudo raspi-config`

--> interface options --> enable camera

### NodeRed
For more details see: https://nodered.org/docs/getting-started/raspberrypi

Install NodeRed:

`bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)`

Set NodeRed to start automatically on boot:

`sudo systemctl enable nodered.service`

Time to restart the pi :)

`sudo reboot -h`

Change the default public folder of NodeRed by running

`sudo nano .node-red/settings.js`

And edit/add the following line:

`httpStatic: '/home/pi/shared/',`

Add the following palettes to NodeRed:

`node-red-stop`

`cd ~/.node-red`

`npm install node-red-dashboard && npm install node-red-contrib-python3-function && npm install node-red-contrib-fs-ops && npm install node-red-contrib-isonline`

Download the OpenScan Flow to node-red:

`sudo wget -O /home/pi/.node-red/flows_raspberrypi.json https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/update.json`

### Samba

### Gphoto2

For more details see: http://www.gphoto.org/doc/


for a list of all supported cameras see: http://www.gphoto.org/doc/remote/
