import sys
import RPi.GPIO as GPIO
import time
import numpy

data = numpy.genfromtxt("colorstate.txt")
ein_aus = int(data[0])
status_red = int(data[1])
status_green = int(data[2])
status_blue = int(data[3])
status_brightness = int(data[4])

outputfile = open("colorstate.txt", "w")


GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

green = float(comand_line_arg[1])
red = float(comand_line_arg[2])
blue = float(comand_line_arg[3])
brightness = float(comand_line_arg[4])

if green != 999 and red != 999 and blue != 999:
	green = status_green/(status_brightness/100)
	blue = status_blue/(status_brightness/100)
	red = status_red/(status_brightness/100)




green = int(green * (brightness/100))
blue = int(blue * (brightness/100))
red = int(red * (brightness/100))

green_diff = green - status_green
blue_diff = blue - status_blue
red_diff = red - status_red


GPIO.setup(18, GPIO.OUT) #gruen
GPIO.setup(14, GPIO.OUT) #rot
GPIO.setup(15, GPIO.OUT) #blau

p_red = GPIO.PWM(14, 100)
p_blue = GPIO.PWM(15, 100)
p_green = GPIO.PWM(18, 100)

if brightness == 0:
	p_green.stop()
	p_red.stop()
	p_blue.stop()
	GPIO.cleanup()
	ein_aus = 0
else:
	for i in Range(99):
		p_green.start(status_green + green_diff *i)
		p_red.start(status_red + red_diff *i)
		p_blue.start(status_blue + blue_diff *i)
		time.wait(0.01)
	
	p_green.start(green)
	p_red.start(red)
	p_blue.start(blue)





outputfile.write(ein_aus + "\n")
outputfile.write(red + "\n")
outputfile.write(green + "\n")
outputfile.write(blue + "\n")
outputfile.write(brightness + "\n")

outputfile.close()