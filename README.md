# turbo-robot

## Requirements
### Hardware
A [raspberry pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
[Raspberry pi 16 channel PWM/servo HAT](https://www.adafruit.com/product/2327)
(see also a [detailed tutorial](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/)
8 micro servos, to be found for silly money on [Ebay](http://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.X9g+servo.TRS0&_nkw=9g+servo&_sacat=0)

### Python packages
pyyaml (sudo pip install pyyaml)
flask (sudo pip install flask)
pyjade (sudo pip install pyjade)
[Adafruit_PCA9685](https://pypi.python.org/pypi/Adafruit-PCA9685/1.0.0) (sudo pip install adafruit-pca9685) 

### Other software requirements
python-smbus (sudo apt-get install python-smbus)
i2c-tools (sudo apt-get install i2c-tools)
(check for [correct workings of the setup](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/attach-and-test-the-hat)
