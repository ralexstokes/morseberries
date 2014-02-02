import RPi.GPIO as GPIO
import time
import sys

pinNum = 22

# change to alter rate of signal
spacer_time = 2
dash_time = 0.75
dot_time = 0.25
stop_time = 0.25

input_phrase = sys.argv[1:]
morse_array = []

# Dictionary from http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

if len(sys.argv) < 2:
    print "Usage:\tpython morse.py $phrase_to_encode"
    print "\t$phrase_to_encode can be multiple words separated by spaces"
    print "\te.g. python morse.py hello world"
    exit(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.OUT)

def flash(wait_time):
  GPIO.output(pinNum, GPIO.HIGH)
  time.sleep(wait_time)
  GPIO.output(pinNum, GPIO.LOW)
  time.sleep(stop_time)

def blink(signal):
  if signal is '-':
    flash(dash_time)
  elif signal is '.':
    flash(dot_time)
  else:
    time.sleep(spacer_time)

for word in input_phrase:
  for character in word:
    morse_array.append(CODE[character.upper()])
  morse_array.append(CODE[' '])

print morse_array

while True:
  for character in morse_array:
    for signal in character:
      blink(signal)
