#!/usr/bin/python
from __future__ import print_function

import Adafruit_PCA9685
import time
import flask
import yaml

with open("../servos.yml", 'r') as stream:
    try:
		servos = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

pwm = Adafruit_PCA9685.PCA9685()
servoMin = 200  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
servoHalfway = (servoMax + servoMin) / 2

def move(channel, position):
	time.sleep(0.01) # allow for a little delay to prevent heavy power dips
	pwm.set_pwm(channel, 0, position)

def spreadEagle():
	for servo, properties in servos.iteritems():
		print('Moving servo:', servo)
		print(properties['port'])
		time.sleep(0.1)
		move(properties['port'], properties['spreadEaglePosition'])

def crab():
	for servo, properties in servos.iteritems():
		print('Moving servo:', servo)
		print(properties['port'])
		time.sleep(0.1)
		move(properties['port'], properties['crabPosition'])
	
crab()
#spreadEagle()
