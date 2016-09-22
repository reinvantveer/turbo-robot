#!/usr/bin/python

import Adafruit_PCA9685
import time
import flask

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = Adafruit_PCA9685.PCA9685()
servoMin = 200  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def set_servo_pulse(channel, pulse):
  pulse_length = 1000000                   # 1,000,000 us per second
  pulse_length //= 60                       # 60 Hz
  print "%d us per period" % pulse_length
  pulse_length //= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulse_length
  pulse *= 1000
  pulse /= pulse_length
  pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.set_pwm(0, 0, servoMin)
  pwm.set_pwm(1, 0, servoMin)
  pwm.set_pwm(2, 0, servoMin)
  time.sleep(1)
  pwm.set_pwm(0, 0, servoMax)
  pwm.set_pwm(1, 0, servoMax)
  pwm.set_pwm(2, 0, servoMax)
  time.sleep(1)



