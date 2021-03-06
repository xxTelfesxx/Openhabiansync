import sys
import RPi.GPIO as GPIO
import time
import numpy
import os, signal

speed = 0.02

data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/ledstrip1_colorstate.txt")
ein_aus = int(data[0])
status_red = int(data[1])
status_green = int(data[2])
status_blue = int(data[3])
status_brightness = int(data[4])
pidvorgaenger = int(data[5])

while True:
	try:
		if pidvorgaenger != 0:
			os.kill(pidvorgaenger, signal.SIGKILL)
		break
	except ProcessLookupError:
		pidvorgaenger = 0
	
GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

green = float(comand_line_arg[1])
red = float(comand_line_arg[2])
blue = float(comand_line_arg[3])
brightness = float(comand_line_arg[4])


if brightness == 0:
	green = 0
	blue = 0
	red = 0
	
else:
	green = int(green * (brightness/100))
	blue = int(blue * (brightness/100))
	red = int(red * (brightness/100))

green_diff = (green - status_green)/100
blue_diff = (blue - status_blue)/100
red_diff = (red - status_red)/100


GPIO.setup(23, GPIO.OUT) #gruen
GPIO.setup(24, GPIO.OUT) #rot
GPIO.setup(25, GPIO.OUT) #blau

p_red = GPIO.PWM(25, 100)
p_blue = GPIO.PWM(23, 100)
p_green = GPIO.PWM(24, 100)

p_green.start(status_green)
p_red.start(status_red)
p_blue.start(status_blue)

if brightness == 0:
	for i in range(99):
		p_green.ChangeDutyCycle(status_green + green_diff *i)
		p_red.ChangeDutyCycle(status_red + red_diff *i)
		p_blue.ChangeDutyCycle(status_blue + blue_diff *i)
		time.sleep(speed)
	
	p_green.stop()
	p_red.stop()
	p_blue.stop()
	GPIO.cleanup()
	ein_aus = 0
else:
	for i in range(99):
		p_green.ChangeDutyCycle(status_green + green_diff *i)
		p_red.ChangeDutyCycle(status_red + red_diff *i)
		p_blue.ChangeDutyCycle(status_blue + blue_diff *i)
		time.sleep(speed)
	
	p_green.ChangeDutyCycle(green)
	p_red.ChangeDutyCycle(red)
	p_blue.ChangeDutyCycle(blue)


print(red,green, blue,brightness)

outputfile = open("/home/openhabian/gitsync/Openhabiansync/ledstrip1_colorstate.txt", "w")
outputfile.write(str(ein_aus) + "\n")
outputfile.write(str(red) + "\n")
outputfile.write(str(green) + "\n")
outputfile.write(str(blue) + "\n")
outputfile.write(str(brightness) + "\n")
outputfile.write(str(os.getpid()) + "\n")
outputfile.close()

time.sleep(8600)
