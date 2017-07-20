#!/usr/bin/python3

'''
    File name: PiHueDash.py
    Author: Tim Richardson
    Date created: 19/07/2017
    Date last modified: 19/07/2017
    Python Version: 3.4

	Description:
	Control Philips Hue lights using an Amazon dash button

    Requirements:
    * Raspberry Pi (http://raspberrypi.org/)
    * Philips Hue (http://www2.meethue.com)
    * Amazon Dash Buttons

    The Raspberry Pi must be on the same network as the Hue bridge
    You must set the bridgeip to be the IP address of your bridge

    You can edit/expand the colour 'xy' values and the alerts
'''

# Import libraries
# Install phue and touchphat with pip3
# pip3 install phue
from phue import Bridge
from scapy.all import *
import time

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Stuff you need to change!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# The IP address of the Hue bridge and a list of lights you want to use
bridgeip = '192.168.13.178'  # <<<<<<<<<<<
# The 'group' of lights you want to change - i.e. the Room Name in the Hue app
lightname = 'Desk'  # <<<<<<<<<<<

mactohue = {'40:b4:cd:0e:8a:c6': 'Desk'}

# -----------------------------------------------------------------------------------------------
# Do some internal setup
# -----------------------------------------------------------------------------------------------
# Connect to the bridge
#b = Bridge(bridgeip)

# IMPORTANT: If running for the first time:
#    Uncomment the b.connect() line
#    Press button on bridge
#    Run the code
# This will save your connection details in /home/pi/.python_hue
# Delete that file if you change bridges
#b.connect() # <<<<<<<<<<

def handle_buttons(pkt):
    if pkt[ARP].op == 1: #who-has (request) seen
        if pkt[ARP].hwsrc == '40:b4:cd:0e:8a:c6': # Button MAC Address
            print "Listerine Pressed"
            time.sleep(2)

print mactohue['40:b4:cd:0e:8a:c6']
#print mactohue['xxx']

print sniff(prn=handle_buttons, filter="arp", store=0)
