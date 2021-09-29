# Install experimental OpenScanCloud processing feature

##  Prerequisites

You should have installed either the simplified or expert user interface following this instructions (see https://github.com/OpenScanEu/OpenScan) or by using a given SD image (see https://en.openscan.eu/pi-shield).

## Setup

Save the current user interface by opening the command terminal and run:
```
cp /home/pi/.node-red/flows_raspberrypi.json /home/pi/.node-red/backup_flows_raspberrypi.json
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
2.	in order to activate the cloud functionality enter your Token and press enter
3.	Press "REFRESH" and you should be able to see limit_photos, limit_filesize and Credit (in Gigabyte)
4.	Uploading and processing should be as simple as selecting a set in the table and press "Upload"
5.	You can query the status from time to time by pressing "REFRESH"
6.  After some time the status will either change to "processing done" and you should get an email with the download link
7.  Please let me know, if everything works, or if you encounter any errors & error codes.

## Demo video :) (deprecated)

[![OpenScan Cloud Processing](https://i.imgur.com/3m1JBVL.png)](https://youtu.be/EhvFq-OYa1g "OpenScan Cloud Processing")

## Manual Upload via OpenScan User Interface

- deprecated, see https://github.com/OpenScanEu/OpenScanCloud for a standalone upload script (python)

## Changelog

2021-09-29:
  - added a new version to implement the completely overhauled OpenScanCloud engine. Only thing to do is to install the update and re-enter your Token (formerly CloudID). Note that some tokens got lost during the rebuild, so feel free to reach out to cloud@openscan.eu :)

2021-02-18:
  - fixed: filesize limit 200-300mb by dropbox --> splitting file on the client device and uploading several parts of 200mb or less
  - added: previewing part of the cloud id "12asvsa1***"
  - added: support different image formats (jpg/jpeg, png, bmp, tiff , gif)
  - added: more detailed upload status
  - improved: stability and minor displaying issues (showing wrong/no information on errors)

## Next Steps

* Further testing :))
