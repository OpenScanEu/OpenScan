# run this script to update/install a client

import os
import requests
import shutil
import time

files=('app.service','photo.service','app.py','photo.py','settings')
paths=('/home/pi/settings/','/home/pi/projects/','/home/pi/app/','/home/pi/temp/')

def installDependencies():
    os.system('sudo apt-get update')
    os.system('sudo raspi-config nonint do_camera 0')
    os.system('sudo raspi-config nonint do_memory_split 256')
    os.system('sudo apt install python3-pip python-pip')
    os.system('pip install picamera')
    os.system('pip3 install picamera flask')
    os.system('sudo apt-get -y install python3-rpi.gpio')
    os.system('sudo apt-get -y install zip unzip')


def download(file):
    url='https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/MultiRig/Client/files/'+file
    targetPath='/home/pi/temp/'+file

    data = requests.get(url, stream=True)
    if data.status_code == 200 and data.headers['content-length'] != 0:
        print('received: '+file)
        with open(targetPath,'w+') as file:
            file.write(data.text)
    else:
        print('ERROR - download failed for '+file)
        exit()


def createService(file):
    if 'service' in file:
        print('creating '+file)
        os.system('sudo cp /home/pi/temp/'+file+' /lib/systemd/system/'+file)
        os.system('sudo systemctl enable '+file)
        os.system('sudo systemctl restart '+file)
        os.system('sudo rm /home/pi/temp/'+file)
    os.system('sudo systemctl daemon-reload')
        
def createSettings():
    with open('/home/pi/temp/settings','r') as file:
        settings=file.readlines()
    for line in settings:
        set=line.rstrip('\n').split(';')
        if not os.path.isfile('/home/pi/settings/'+set[0]):
            with open('/home/pi/settings/'+set[0],'w+') as file:
                file.write(set[1])
    os.system('sudo rm /home/pi/temp/settings')

installDependencies()

for path in paths:
    if not os.path.isdir(path):
        os.mkdir(path)

for file in files:
    download(file)
    createService(file)

createSettings()

for file in os.listdir('/home/pi/temp/'):
    os.system('sudo mv /home/pi/temp/'+file+ ' /home/pi/app/'+file)

os.system('rmdir /home/pi/temp/')
