from flask import Flask, make_response, jsonify, request, abort, Response, stream_with_context
import os
import shutil

CHUNK_SIZE = 8192
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
@app.route('/getUpdate')
def getUpdate():
    return('TO DO')
    #to do get update from github


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

    shutil.make_archive(path+'/photos', 'zip', path+'/photos')
    shutil.make_archive(path+'/settings', 'zip', path+'/settings')
    return('project zipped')

@app.route('/project/downloadSettings/<name>', methods=['post','get'])
def downloadProjectSettings(name):
    return('TO DO')
# TO DO

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





