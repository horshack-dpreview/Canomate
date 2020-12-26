# canomate - Automation Utility for Canon cameras

This uses Canon's Canon Control API (CCAPI), with is a REST API that canomate
query status information, set/set operating systems, and perform actions via
http-based GET and POST/PUT commands.

## Online Manual

http://www.testcams.com/canomate

## Requirements

1. A Canon camera that supports the Canon Control API. As of 8/2020
   this includes: R5, R6, T8i, 1DX Mark III, M200, M6 Mark II,
   90D, SL3, RP, SX70 HS, G5 X Mark II, G5 X Mark III    
2. Python 3.5 or later
3. "requests" library (https://requests.readthedocs.io/en/master/)

## Python Setup

1. Install the latest Python 3.x from https://www.python.org/downloads/
2. This module uses the 'requests' module, which can be installed via
   the command line by running "pip install requests"

For OSX/Mac, Python 2.7x comes included. You need to install the latest 3.x
Python for this script to work. The newer version will be installed at
/usr/local/bin/. The 'requests' module can then be installed by opening a
terminal window and running "pip3 install requests". After that you can
run this script by placing the files somewhere in your home directory and
running "python3 canomate.py"

## Camera Setup

Enabling the Control API requires a one-time activation using Canon's
CCAPI activation tool, which is distributed on Canon's developer
website at https://developercommunity.usa.canon.com/canon?id=sdk_download.


1. Connect the camera via USB to computer and run the CCAPI activation tool.
   Disconnect the camera from the computer when complete.
2. Go to "Wireless communication settings" in the camera, select "Wi-Fi
   settings", then "Camera Control API". You'll need to provide the info for
   your local wireless network if you haven't already done so - you can use
   WPS if your router supports it to get through the setup faster. You can
   optionally specify a static IP address, which may make it easier to use
   this utility since you'll always know the camera's IP address rather than
   having to check the camera (although most routers will reuse the same IP
   address for a given MAC address).. At the last step of the process the
   camera will display a URL you can access; enter that URL on your computer
   to finalize the setup and verify everything is working.
3. When done you'll also want to enable "Auto connect" in the same Camera
   Control API menu of the camera; that way the camera will automatically
   connect to your network and enable the CCAPI whenever you turn the camera
   on. You may need to temporarily disconnect from CCAPI in the camera in
   order to turn "Auto connect" on.
