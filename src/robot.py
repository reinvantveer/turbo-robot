#!/usr/bin/python
from __future__ import print_function

import Adafruit_PCA9685
import time
import yaml

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# Set up servo configuration
with open("../servos.yml", 'r') as stream:
    try:
		servos = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open("../schema.yml", 'r') as stream:
    try:
		schema = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Set frequency to 60 Hz
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

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

actions = {
	'spreadEagle': spreadEagle,
	'crab': crab
}

# set up API error handling 
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# set up web server routes
@app.route("/favicon.ico")
def favicon():
	return app.send_static_file('favicon.ico')

@app.route("/operate", methods=['POST'])
def operate():
	if not request.args.get('action', ''):
		raise InvalidUsage('Missing action parameter')
	
	action = request.args.get('action', '')
	
	if not action in actions:
		raise InvalidUsage('Unknown action "' + action + '"')

	actions[action]()

	return 'Doing ' + action

@app.route("/calibrate")
def calibrate():
	return render_template('index.jade', servos = servos, schema = schema)
	
if __name__ == "__main__":
    app.run(host="0.0.0.0")

