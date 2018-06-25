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

def hsb_to_rgb(h,s,v):

    i = numpy.floor(h*6)
    f = h*6 -i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)
    x = i%6
    if i == 0:
        red = v
        green = t
        blue = p
    if i == 1:
        red = q
        green = v
        blue = p
    if i == 2:
        red = p
        green = v
        blue = t
    if i == 3:
        red = p
        green = q
        blue = v
    if i == 4:
        red = t
        green = p
        blue = v
    if i == 5:
        red = v
        green = p
        blue = q

    return red*100,green*100, blue*100
			
# eingabe: [Name txt Datei] [GPIO Bin Gruen] [GPIO Bin blau] [GPIO Bin rot] [Helligkeit in %] ["rgb" oder "hsb"][Gruen in % / hue] [Rot in % / saturation] [Blau in % / lightness]

GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])
gpio_gruen = int(comand_line_arg[2])
gpio_rot = int(comand_line_arg[3])
gpio_blau = int(comand_line_arg[4])
helligkeit = int(comand_line_arg[5])
colorsystem = str(comand_line_arg[6])

if colorsystem == "rgb":
	gruen_neu = float(comand_line_arg[7])
	rot_neu = float(comand_line_arg[8])
	blau_neu = float(comand_line_arg[9])
elif colorsystem == "hsb":
	hue = float(comand_line_arg[7])
	saturation = float(comand_line_arg[8])
	lightness = float(comand_line_arg[9])
	
	rot_neu,gruen_neu,blau_neu = hsb_to_rgb(hue/360,saturation/100,lightness/100)

speed = 0.02


data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + "_colorstate.txt")
wechselprozess = int(data[0])
status_red = int(data[1])
status_green = int(data[2])
status_blue = int(data[3])
status_brightness = int(data[4])
pid_old = int(data[5])

if helligkeit == 999:
	helligkeit = status_brightness
if gruen_neu == 999:
	gruen_neu = status_green
if rot_neu == 999:
	rot_neu = status_red
if blau_neu == 999:
	blau_neu = status_blue


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

	if helligkeit == 0:
		for i in range(99):
			helligkeit_now = (status_brightness +helligkeit_diff*i)/100
			p_green.ChangeDutyCycle((status_green + green_diff *i)*helligkeit_now)
			p_red.ChangeDutyCycle((status_red + red_diff *i)*helligkeit_now)
			p_blue.ChangeDutyCycle((status_blue + blue_diff *i)*helligkeit_now)
			time.sleep(speed)
	
		p_green.stop()
		p_red.stop()
		p_blue.stop()
		GPIO.cleanup()
		outputfile = open("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + "_colorstate.txt", "w")
		outputfile.write("0" + "\n")
		outputfile.write(str(rot_neu) + "\n")
		outputfile.write(str(gruen_neu) + "\n")
		outputfile.write(str(blau_neu) + "\n")
		outputfile.write(str(helligkeit) + "\n")
		outputfile.write(str(os.getpid()) + "\n")
		outputfile.close()
		print("Lampen aus")
		exit()

	else:
		for i in range(99):
			helligkeit_now = (status_brightness +helligkeit_diff*i)/100
			p_green.ChangeDutyCycle((status_green + green_diff *i)*helligkeit_now)
			p_red.ChangeDutyCycle((status_red + red_diff *i)*helligkeit_now)
			p_blue.ChangeDutyCycle((status_blue + blue_diff *i)*helligkeit_now)
			time.sleep(speed)
	
		p_green.ChangeDutyCycle(gruen_neu * helligkeit/100)
		p_red.ChangeDutyCycle(rot_neu * helligkeit/100)
		p_blue.ChangeDutyCycle(blau_neu * helligkeit/100)


	print("Rot, gruen, blau, helligkeit")
	print(rot_neu,gruen_neu, blau_neu,helligkeit)

	outputfile = open("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + "_colorstate.txt", "w")
	outputfile.write("0" + "\n")
	outputfile.write(str(rot_neu) + "\n")
	outputfile.write(str(gruen_neu) + "\n")
	outputfile.write(str(blau_neu) + "\n")
	outputfile.write(str(helligkeit) + "\n")
	outputfile.write(str(os.getpid()) + "\n")
	outputfile.close()

	time.sleep(86000)

else:
	print("Eine Instanz läuft bereits")
