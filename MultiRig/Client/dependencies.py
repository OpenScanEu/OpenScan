import os

def installDependencies():
    os.system('sudo apt-get update')
    os.system('sudo raspi-config nonint do_camera 0')
    os.system('sudo raspi-config nonint do_memory_split 256')
    os.system('sudo apt -y install python3-pip python-pip')
    os.system('pip install picamera requests')
    os.system('pip3 install picamera flask requests')
    os.system('sudo apt-get -y install python3-rpi.gpio')
    os.system('sudo apt-get -y install zip unzip')
    
installDependencies()
