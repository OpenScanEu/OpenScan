# OpenScan

## Overview:
The Raspberry Pi + OpenScan Pi Shield can be used to control two independent stepper motors and a variety of different cameras (Pi Camera, DSLR - via GPhoto and external Cameras like Smartphone and others). The mechanism can be used in various forms (see for example https://www.thingiverse.com/thing:3050437 or https://www.thingiverse.com/thing:2944570 and it could be easily adapted to be used as a camera slider or in other mechanisms.

## Setup
In order to add the OpenScan functionality to an existing raspbian system and understand all the dependencies, here is a full step-by-step list of the setup:

```
sudo apt-get update
sudo apt-get upgrade
mkdir -p /home/pi/shared/ui/data/old_flows && mkdir /home/pi/shared/log
```

### Dependencies

```
sudo apt-get install python3-pip && sudo apt-get install python-pip && sudo apt-get install python-pil
```

### PiCamera
```
sudo apt-get install python3-picamera && sudo apt-get install python-picamera
```

```
sudo raspi-config
```
--> interface options --> enable camera

### Samba

Samba is a fileserver, that allows you to access the Pi's filesystem via network folders. This functionality is optional but comes in quite handy.

```
sudo apt-get install samba samba-common-bin
```
```
sudo nano /etc/samba/smb.conf
```

Change the following lines:
```
workgroup = WORKGROUP
wins support = yes  
read only = no
```

Add to the end of the file:
```
[PiShare]
comment=Raspberry Pi Share
path=/home/pi/shared
browseable=Yes
writeable=Yes
only guest=no
create mask=0777
directory mask=0777
public=yes
```

Set a network password:

```
sudo smbpasswd -a pi
```

Now you can access the filesystem of the raspberry pi through your network folder using the username "pi" and the given password.

### Gphoto2

GPhoto2 is used to control DSLR cameras, which can be connected via USB. For a list of all supported cameras that can be used within this project see: https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/supported_cameras

For more details see: http://www.gphoto.org/doc/
```
sudo apt install libgphoto2-dev
sudo apt install gphoto2
```

```
sudo pip3 install -v gphoto2
sudo pip install -v gphoto2
```

for a list of all supported cameras see: http://www.gphoto.org/doc/remote/

### NodeRed

NodeRed offers a great browser interface in order to control the steppers, cameras and accessories.
For more details see: https://nodered.org/docs/getting-started/raspberrypi

Install NodeRed:

```
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

Set NodeRed to start automatically on boot:
```
sudo systemctl enable nodered.service
```

Time to restart the pi :)

```
sudo reboot -h
```

Change the default public folder of NodeRed by running

```
sudo nano /home/pi/.node-red/settings.js
```

And uncomment and change the following line (httpStatic:...):

```
httpStatic: '/home/pi/shared/',
```

Add the some palettes to NodeRed:

```
node-red-stop
cd ~/.node-red
npm install node-red-dashboard && npm install node-red-contrib-python3-function && npm install node-red-contrib-fs-ops && npm install node-red-contrib-isonline
```

Download the OpenScan Flow to node-red:
```
sudo wget -O /home/pi/.node-red/flows_raspberrypi.json https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/update.json
```

Restart and done :))

```
sudo reboot -h
```

After the setup you can access the frontend in your browser by typing: `IP:1880/ui`
The backend can be reached via `IP:1880`

### Optional: Change hostname
```
sudo raspi-config
```

--> Network Options --> Hostname

Change hostname to OpenScanPi

Adjust the NodeRed Settings by opening
```
sudo nano /home/pi/.node-red/settings.js
```

uncomment "flowFile: ..." and change it to:
```
flowFile: 'flows_raspberrypi.json',
```

After the setup you can access the frontend in your browser by typing: `OpenScanPi:1880/ui`  
The backend can be reached via `OpenScanPi:1880`  
This works from any device, which is in the same network as the raspberry pi.

If you are logged in to your pi, you can also enter the user interface directly through `localhost:1880/ui`


# Usage & Manual

For more information on the usage of the OpenScan Interface please consult the manual: https://github.com/OpenScanEu/OpenScan/raw/master/Manual_en.pdf
