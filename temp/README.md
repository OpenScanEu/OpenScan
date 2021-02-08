# Install experimental OpenScanCloud processing feature

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
2.	in order to activate the cloud functionality enter your CLOUD ID at the bottom right and press "SAVE CLOUD ID" 
3.	Press "REFRESH" and you should be able to see limit_photos, limit_filesize and Credit (in Gigabyte)
4.	Uploading and processing should be as simple as selecting a set in the table and press "Upload and compute …"
5.	You can query the status from time to time by pressing "REFRESH", but do not spam, as this will crash/reboot your device (known issue)
6.  After some time the status will either change to "done" or some error message. In the first case a download link will be generated (valid for 14 days)
7.	Please let me know, if everything works, or if you encounter any errors & error codes.

