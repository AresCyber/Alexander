# HomeSecurity 

This home security system is for residential access control. 
The system is designed to authenticate entities at a door 
via voice and facial recognition. 

## Hardware Requirements

- 2 Raspberry Pi 3 or 4's. It is highly recommended to use 4's because of the increased computing power (more ram, cpu)
- Raspberry Pi Camera
- Compact USB Microphone
- Compact analog speaker
- 1 Cat 5/6 ethernet cable
- August Door lock with Wifi connectivity, other options are available and it is trivial to integrate within main.py

### Optional
- GSM/3G module for backup internet
- 2 battery packs for backup power to the RPi's

## Network Diagram

The first Raspberry Pi will act as a gateway/firewall/dns/dhcp server for the security network. Other devices can easily be added to the network for future expansion. 

![network diagram](https://github.com/AresCyber/Alexander/blob/main/images/network.png)

## Program Flow

The current prototype will contain the following program design flow

![program flow](https://github.com/AresCyber/Alexander/blob/main/images/flow.png)

## Software Requirements 

### Raspberry Pi containing voice and face recognition
1. Raspian OS
2. Python 3.6+ (usually already on the Pi)
3. Install OpenCV. Follow [this](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)  guide steps 2-4a. Step 3 is optional if you don't want to use a virtual python environment
4. Install espeak `sudo apt-get install espeak`
5. Install pyaudio `sudo apt-get install python-pyaudio python3-pyaudio`
6. Clone this github repository `git clone https://github.com/arescyber/alexander.git`
7. Install requirements `pip3 install -r requirements.txt`

## Setup (RPi #1)
This Raspberry will act as the gateway and firewall. This guide is inspired from [this](https://https://www.maketecheasier.com/how-to-turn-raspberry-pi-into-wireless-access-point/) blog post

Setup commands can be found in "router.txt"

## Setup (RPi #2)

1. The first step is to insert the camera, speaker, and usb microphone
2. Set the microphone gain slightly above halfway
3. Gather data for the facial recognition algorithm. To do this, place your face in a well lit area and run 1_collector.py. This will take 30 photos of your face for use in the training portion. Take more photos of other users you would like to be authorized. 
4. Train the algorithm. Simply run `python3 1_trainer.py`. That's it! That's all you need to train the model. 
5. Set custom voice passwords on lines 18,21,24, and 35. 
6. Create an August account and use "augusttest.py" 
    1. enter email and password into the `email@email.com` and `password` fields
    1. an email with a verification code will be sent. 
    1. uncomment line 16 and proceed to enter code in the parenthesis. A new cached credentials file should have been created
    1. enter email and password into the "augustlock.py" file
7. Create a twilio account and acquire a free api key. In mms.py enter your account sid, api key, and target phone number for notifications. 

8. Configure IP tables to block all incoming traffic. A template is provided for blocking it all or allowing SSH and VNC. 
    a. Block all incoming. 
    `sudo iptables -A INPUT -i wlan0 -j DROP`
    `sudo iptables save`
    b. Block all except for port 22 && 5800
    `sudo iptables -A INPUT -i wlan0 -p tcp --dport 22 -j ACCEPT`
    `sudo iptables -A INPUT -i wlan0 -p tcp --dport 5800 -j ACCEPT`
    `sudo iptables -A INPUT -i wlan0 -j DROP`
    `sudo iptables save`

