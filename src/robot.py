#!/usr/bin/python
from __future__ import print_function

import Adafruit_PCA9685
import time
from flask import Flask
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# Set up servo configuration
with open("../servos.yml", 'r') as stream:
    try:
		servos = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

pwm.set_pwm_freq(60)                        # Set frequency to 60 Hz

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

# set up web server routes
@app.route("/favicon.ico")
def favicon():
	return app.send_static_file('favicon.ico')

@app.route("/calibrate")
def calibrate():
	return render_template('index.jade', )
	
if __name__ == "__main__":
    app.run(host="0.0.0.0")

