#
from flask import Flask, make_response, jsonify, request, abort, Response, stream_with_context
import os
import shutil
import RPi.GPIO as GPIO


CHUNK_SIZE = 8192
ringlight_pin_1 = 23
ringlight_pin_2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(ringlight_pin_1, GPIO.OUT)
GPIO.setup(ringlight_pin_2, GPIO.OUT)

def read_file_chunks(path):
    with open(path, 'rb') as fd:
        while 1:
            buf = fd.read(CHUNK_SIZE)
            if buf:
                yield buf
            else:
                break

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    return 'hello world :)'

@app.route('/reboot', methods=['post', 'get'])
def reboot():
    os.system('sudo reboot -h now')
    return 'rebooting'

@app.route('/shutdown', methods=['post', 'get'])
def shutdown():
    os.system('sudo shutdown -h now')
    return 'shut down'

############################ RINGLIGHT

@app.route('/ringlight/<number>/<state>', methods=['post', 'get'])

def ringlight(number, state):
    if number == "1":
        if state == "on":
            GPIO.output(ringlight_pin_1, GPIO.HIGH)
        else:
            GPIO.output(ringlight_pin_1, GPIO.LOW)
    elif number == "2":
        if state == "on":
            GPIO.output(ringlight_pin_2, GPIO.HIGH)
        else:
            GPIO.output(ringlight_pin_2, GPIO.LOW)
    else:
        return 'invalid cmd'
    return 'done'

############################ PREVIEW

@app.route('/preview')
def preview():
    path = '/home/pi/preview.jpg'
    name2='preview.jpg'
    return Response(
        stream_with_context(read_file_chunks(path)),
        headers={
            'Content-Disposition': f'attachment; filename={name2}'})

############################# PHOTO SERVICE


@app.route('/photo/<cmd>')
def photo(cmd):
    if cmd=='start':
        os.system('sudo systemctl start photo.service')
        return('photo.service started')
    if cmd=='stop':
        os.system('sudo systemctl stop photo.service')
        return('photo.service stopped')
    abort(404)


################### SETTINGS ########################

@app.route('/getSettings/<setting>', methods=['post','get'])
def getSettings(setting):
    path='/home/pi/settings/'+str(setting)
    if not os.path.isfile(path):
        abort(405, decription="setting does not exist")
    with open(path) as file:
        content=file.read()
    print(content)
    return content

@app.route('/setSettings/<setting>/<value>', methods=['post','get'])
def setSettings(setting,value):
    path='/home/pi/settings/'+str(setting)
    if not os.path.isfile(path):
        abort(405, decription="setting does not exist")
    with open(path, 'w') as file:
        file.write(value)
    return setting

#################### UPDATE ##################################

@app.route('/update/get')
def getUpdate():
    try:
        os.system('wget https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/MultiRig/Client/updater.py -O "/home/pi/updater.py"')
        os.system('wget https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/MultiRig/Client/dependencies.py -O "/home/pi/dependencies.py"')
        return 'downloaded firmware & dependencies'
    except:
        return 'error downloading files'

@app.route('/update/firmware')
def installFirmware():
    os.system('python3 "/home/pi/updater.py"')
    return 'updating firmware'

@app.route('/update/dependencies')
def installDependencies():
    os.system('python3 "/home/pi/dependencies.py"')
    return 'updating dependencies'


    
####################### PROJECT ##############################
@app.route('/project/create/<name>', methods=['post','get'])
def createProject(name):
    path='/home/pi/projects/'+name
    if os.path.isdir(path):
        abort(405, description="project already exists")

    os.mkdir(path)
    os.mkdir(path+"/photos/")
    os.mkdir(path+"/settings/")

    for i in os.listdir('/home/pi/settings/'):
        shutil.copy('/home/pi/settings/'+i, path+'/settings/'+i)
    return ('project created')

@app.route('/project/zip/<name>', methods=['post','get'])
def zipProject(name):
    path='/home/pi/projects/'+name
    if not os.path.isdir(path):
        abort(405, description="project does not exist")
    if os.path.isfile(path+'/settings.zip'):
        abort(405, description="already zipped")

    shutil.make_archive(path+'/photos', 'zip', path+'/photos/')
    shutil.make_archive(path+'/settings', 'zip', path+'/settings/')
    return('project zipped')

@app.route('/project/downloadPhotos/<name>', methods=['post','get'])
def downloadProjectPhotos(name):
    path = '/home/pi/projects/'+name+'/photos.zip'
    name2='photos.zip'
    return Response(
        stream_with_context(read_file_chunks(path)),
        headers={
            'Content-Disposition': f'attachment; filename={name2}'})
          

@app.route('/project/delete/<name>', methods=['post','get'])
def deleteProejct(name):
    path='/home/pi/projects/'+name
    if not os.path.isdir(path):
        abort(405, description="project does not exist")
    shutil.rmtree('/home/pi/projects/'+name)
    return ('project deleted')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





