import RPi.GPIO as GPIO  # import RPi.GPIO module
from picamera import PiCamera
import time
import zipfile


counter = 0
quality = 100
preview_filepath = '/home/pi/preview.jpg'
GPIO.setmode(GPIO.BCM)

def load(setting):
    with open('/home/pi/settings/' + setting, 'r') as file:
        value = file.readline().rstrip('\n')
    if setting != 'status':
        print(setting+' : '+str(value))
    return value

def set(setting, content):
    with open('/home/pi/settings/' + setting, 'w') as file:
        file.write(str(content))

inputPin = int(load('input_pin'))
counter_threshold = int(load('counter_threshold'))

cam_resx = int(load('cam_resx'))
cam_resy = int(load('cam_resy'))

x = cam_resx
y = cam_resy
downsize_preview = 1

camera = PiCamera(resolution=(cam_resx, cam_resy))
GPIO.setup(inputPin, GPIO.IN)
time.sleep(1)

def load_cam_settings():
    global x, y, quality, cam_resx, cam_resy, downsize_preview
    print('cam_settings_loaded')
    camera.iso = int(load('cam_iso'))
    camera.meter_mode = load('cam_meter_mode')
    camera.shutter_speed = int(load('cam_shutterspeed'))
    camera.exposure_mode = load('cam_exposure_mode')
    camera.awb_mode = load('cam_awb_mode')
    camera.awb_gains = (float(load('cam_awb_red')), float(load('cam_awb_blue')))
    camera.brightness = int(load('cam_brightness'))
    camera.contrast = int(load('cam_contrast'))
    camera.exposure_compensation = int(load('cam_exposure_compensation'))
    quality = int(load('cam_quality'))


    cropx = float(load('cam_cropx'))
    cropy = float(load('cam_cropy'))
    downsize_preview = float(load('cam_downsize_preview'))
    zoom_x_center = cropx / 200
    zoom_y_center = cropy / 200
    zoom_x_width = 1 - cropx / 100
    zoom_y_height = 1 - cropy / 100
    x = int(cam_resx * zoom_x_width)
    y = int(cam_resy * zoom_y_height)
    camera.zoom = (zoom_x_center, zoom_y_center, zoom_x_width, zoom_y_height)


load_cam_settings()

while True:
    status = load("status")
    if status == 'take_preview':
        load_cam_settings()
        camera.capture(preview_filepath, quality=quality, resize=(int(x*downsize_preview),int(y*downsize_preview)))
        set('status', 'preview_done')
        print('preview done')
    if status == 'load_cam_settings':
        load_cam_settings()
        set('status', 'cam_settings_loaded')
    if status == 'take_photo':
        current_project = load('current_project')
        filepath = '/home/pi/projects/'+current_project+'/photos/'
        z = zipfile.ZipFile('/home/pi/projects/'+current_project+'/photos.zip', 'a')
        print('taking photo')
        while load('status') == 'take_photo':
            if counter != 0:
                print(counter)
            if GPIO.input(inputPin):
                counter = counter + 1
            if not GPIO.input(inputPin):
                counter = 0
            if counter == counter_threshold:
                t=str(time.time())
                camera.capture(filepath+t+'.jpg', quality=quality, resize=(x, y))
                z.write(filepath+t+'.jpg')
                print('photo taken')
                counter = 0
        z.close()
        print('done')

