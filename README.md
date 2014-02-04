# Morseberries

Send Morse code signals from an LED controlled by the GPIO pins on a Raspberry Pi.  Adapted from [http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/](http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/)

![photo of breadboard](http://alex.stokes.io/media/photo.jpg)
![photo of other side of breakout board](http://alex.stokes.io/media/photo2.jpg)

## Usage
    sudo python morse.py $hello_world

where `$hello_world` can be a multi-word phrase consisting of alphanumeric characters and spaces.  Use of `sudo` is needed for the Raspberry Pi as the GPIO pins are not accessible from user space.

## Examples
    sudo python morse.py sos
    sudo python morse.py buy milk

-- todo: add videos showing LED output of above commands.


## Requirements
Requires the RPi.GPIO library found here:  [http://sourceforge.net/projects/raspberry-gpio-python/](http://sourceforge.net/projects/raspberry-gpio-python/)

