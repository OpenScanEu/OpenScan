# Install experimental OpenScanCloud processing feature

##  Prerequisites

You should have installed either the simplified or expert user interface following this instructions (see https://github.com/OpenScanEu/OpenScan) or by using a given SD image (see https://en.openscan.eu/pi-shield).

## Setup

Save the current user interface by opening the command terminal and run:
```
cp /home/pi/.node-red/flows_raspberrypi.json /home/pi/.node-red/backup_flows_raspberrypi.json
```

Install requests module for python
```
pip install requests
```


Install the modified User Interface:
```
sudo wget -O /home/pi/.node-red/flows_raspberrypi.json https://raw.githubusercontent.com/OpenScanEu/OpenScan/master/temp/2020-06-02_OSC.json
```
  
and restart node-red:
```
node-red-restart
```

(If you want to restore your previous user interface:
```
cp /home/pi/.node-red/backup_flows_raspberrypi.json /home/pi/.node-red/flows_raspberrypi.json
```

## Usage

You should be ready to access the new functions via the userinterface at openscanpi:1880/ui and submenu "files"

![User Interface](https://i.imgur.com/LKgPVJb.png)

Follow these steps to upload and process your existing photoset:
1.	you will be able to see your existing files and download the image sets from the pi to your computer via "ZIP" link (similar to before)
2.	in order to activate the cloud functionality enter your CLOUD ID at the bottom right and press "SAVE CLOUD ID". You can either use your personal Cloud ID (which can be obtained via email to info@openscan.eu or use this public-test-ID: ```59521b73198a43bcb9ed8f8e67d12b3XXf56X49Xcbe14677e5```
(Important note: the public ID will be removed at some point in the future)
3.	Press "REFRESH" and you should be able to see limit_photos, limit_filesize and Credit (in Gigabyte)
4.	Uploading and processing should be as simple as selecting a set in the table and press "Upload and compute …"
5.	You can query the status from time to time by pressing "REFRESH", but do not spam, as this will crash/reboot your device (known issue)
6.  After some time the status will either change to "done" or some error message. In the first case a download link will be generated (valid for 14 days)
7.	Please let me know, if everything works, or if you encounter any errors & error codes.

## Demo video :)

[![OpenScan Cloud Processing](https://i.imgur.com/3m1JBVL.png)](https://youtu.be/EhvFq-OYa1g "OpenScan Cloud Processing")

## More Details

### Possible Status Message:

#### created:
  file has been uploaded

#### file received:
  file has been received and downloaded to the OpenScan Server

#### start processing:
  processing has been started

#### alignment failed:
  If x or less percent of the images get aligned, the processing will be aborted, as the results will not be acceptable (There are various reasons for a set to fail, usually      it has to do with the lack of features (https://en.openscan.eu/photogrammetry and https://en.openscan.eu/scan-gallery for some more background and good examples). I am still   determining the threshold percentage x, but currently it is set to 50%

### zip error
  Indicating that the zip file or its content is broken

#### done:
    The set has been processed and the result.zip should be accessible within the next minute

## Manual Upload via OpenScan User Interface

You can upload your own image set by copying a zip file to /home/pi/shared/ui/data/zip/ and upload this file via the user interface

Note, that the easiest way to copy a file to the pi is adding the device as network drive: \\\openscanpi\pi (user: pi, password: raspberry)

Important:
* do not use any sub-folders in the zip-file
* only use the following image-filetypes: jpg/jpeg, png, bmp, tiff , gif
* stay within the given limits (filesize and image-count)

## Changelog

2021-02-18:
  - fixed: filesize limit 200-300mb by dropbox --> splitting file on the client device and uploading several parts of 200mb or less
  - added: previewing part of the cloud id "12asvsa1***"
  - added: support different image formats (jpg/jpeg, png, bmp, tiff , gif)
  - added: more detailed upload status
  - improved: stability and minor displaying issues (showing wrong/no information on errors)

## Next Steps

* Further testing :))
* install missing requests module automatically
* Create a desktop upload tool (I would love to see a standalone uploader, where you can enter&save your cloud Id and upload a zip file from your PC or maybe even smartphone?!)
