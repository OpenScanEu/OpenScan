# OpenScan - Photogrammetry Torture Test

## Overview:

For a very long time, i wanted to publish several  image sets containing various challenging features. I will host the image sets and resulting meshes on [Google Drive](https://drive.google.com/drive/folders/17gwZCjs7iHAg9MYrOH1vxBhsXcBB6EWp?usp=sharing)
This is a public project, so you can use the files as you wish. I would love to see more people contributing and giving the image set a run on there photogrammetry pipeline + sharing the result.
If you know a better hosting solution, please let me know.



## Dataset - Overview:

|Image Set|Details|Filesize (MB)|Photos|Captured with|Link|
|:---:|:---:|:---:|:---:|:---:|:---:|
|01|complex object form<br />many surface features<br />blurry foreground and background|644|200|OpenScan Mini<br />Pi Camera V2.1|[Drive](https://drive.google.com/drive/folders/15zAvuZRO3YX1WXOl7bdb167kNNcqVpso?usp=sharing)|
|02|many surface features<br />many background features<br />turntable setup |59 |16 |OpenScan Classic |[Drive](https://drive.google.com/drive/folders/1JXyPk63VRlB-vjvUpUhovFFDtgqv-QMe?usp=sharing) |
| | | | | | |

## Dataset - Details
### (01) Prusa SL1 Test print
![Prusa SL1 test](https://i.imgur.com/IFdjokH.jpg)
This is a 3d printed miniature used to test the accuracy of DLP/SLA printers. The original model can be downloaded on [PrusaPrinters](https://www.prusaprinters.org/prints/5375). I have scaled the object to 150% for better printability. I used Anycubic grey + black resin to print this 30x95x56mm object on my Anycubic Mono. If you want to scan this object, you can either download and print it yourself, or if you are in the EU or US, just reach out and I will send you a 3d printed copy!

### (02) Aphrodite
![Aphrodite](https://i.imgur.com/HCBBw2i.jpg)
This small gypsum figurine was covered in black chalk spray in order to create enough surface features for the software to recognize. I also added the same pattern to the background and even focused the camera (Iphone XS) on the background to maximize the issue...


## Reconstruction

|Image Set|OpenScanCloud|RealityCapture|3DF Zephyr|Agisoft Metashape|Meshroom|VisualSFM|Regard3D|Autodesk Recap|MicMac|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|01 |✔ |✔ |   |   |   |   |   |   |✔ |
|02 |✔ |   |✖ |   |   |   |✖  |✖  |✔ |

## Contribution & Attribution
### 02
Thanks [Luc Girod](https://github.com/luc-girod) for contributing the MicMac results. Check-out his GitHub page for more details and his custom MicMac workflow.
