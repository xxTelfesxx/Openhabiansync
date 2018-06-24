import sys
import RPi.GPIO as GPIO
import time
import numpy
import os, signal

def killoldeversion(pid_old):
	while True:
		try:
			if pid_old != 0:
				os.kill(pid_old, signal.SIGKILL)
			break
		except ProcessLookupError:
			pid_old = 0

# eingabe: [Name txt Datei] [GPIO Bin Gruen] [GPIO Bin blau] [GPIO Bin rot] [Helligkeit in %] [Gruen in %] [Rot in %] [Blau in %]

GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])
gpio_gruen = int(comand_line_arg[2])
gpio_rot = int(comand_line_arg[3])
gpio_blau = int(comand_line_arg[4])
helligkeit = float(comand_line_arg[4])
gruen_neu = float(comand_line_arg[4])
rot_neu = float(comand_line_arg[4])
blau_neu = float(comand_line_arg[4])

speed = 0.02
keepactive = True

data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + "_colorstate.txt")
wechselprozess = int(data[0])
status_red = int(data[1])
status_green = int(data[2])
status_blue = int(data[3])
status_brightness = int(data[4])
pid_old = int(data[5])

if wechselprozess == 0:
	outputfile = open("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + "_colorstate.txt", "w")
	outputfile.write("1" + "\n")
	outputfile.write(str(status_red) + "\n")
	outputfile.write(str(status_green) + "\n")
	outputfile.write(str(status_blue) + "\n")
	outputfile.write(str(status_brightness) + "\n")
	outputfile.write(str(os.getpid()) + "\n")
	outputfile.close()


	green_diff = (gruen_neu - status_green)/100
	blue_diff = (blau_neu - status_blue)/100
	red_diff = (rot_neu - status_red)/100
	helligkeit_diff = (helligkeit - status_brightness)/100

	killoldeversion(pid_old)

	GPIO.setup(gpio_gruen, GPIO.OUT) #gruen
	GPIO.setup(gpio_rot, GPIO.OUT) #rot
	GPIO.setup(gpio_blau, GPIO.OUT) #blau

	p_red = GPIO.PWM(gpio_rot, 100)
	p_blue = GPIO.PWM(gpio_blau, 100)
	p_green = GPIO.PWM(gpio_gruen, 100)

	p_green.start(status_green)
	p_red.start(status_red)
	p_blue.start(status_blue)

	if brightness == 0:
		for i in range(99):
			helligkeit_now = status_brightness +helligkeit_diff*i
			p_green.ChangeDutyCycle(status_green + green_diff *i)
			p_red.ChangeDutyCycle(status_red + red_diff *i)
			p_blue.ChangeDutyCycle(status_blue + blue_diff *i)
			time.sleep(speed)
	
		p_green.stop()
		p_red.stop()
		p_blue.stop()
		GPIO.cleanup()
		keepactive = False
	else:
		for i in range(99):
			p_green.ChangeDutyCycle(status_green + green_diff *i)
			p_red.ChangeDutyCycle(status_red + red_diff *i)
			p_blue.ChangeDutyCycle(status_blue + blue_diff *i)
			time.sleep(speed)
	
		p_green.ChangeDutyCycle(green)
		p_red.ChangeDutyCycle(red)
		p_blue.ChangeDutyCycle(blue)
		keepactive = True


	print(red,green, blue,brightness)

	outputfile = open("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + "_colorstate.txt", "w")
	outputfile.write("0" + "\n")
	outputfile.write(str(red) + "\n")
	outputfile.write(str(green) + "\n")
	outputfile.write(str(blue) + "\n")
	outputfile.write(str(brightness) + "\n")
	outputfile.write(str(os.getpid()) + "\n")
	outputfile.close()

	
	if keepactive:
		time.sleep(86000)
