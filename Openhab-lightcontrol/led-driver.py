import sys
import RPi.GPIO as GPIO
import time
import numpy
import math
import os, signal

def waitinput():
        for x in range (10800):
                data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + ".txt")
                update = int(data[9])
                if update==1:
                        break
                time.sleep(1)

def sinus(x):
    a = 100* math.sin(math.radians(x))
    if a < 0:
        a=0
    return int(a)

def sinus2(x):
    a = 50* (math.sin(math.radians(x))+1)
    if a < 0:
        a=0
    return int(a)


			
# eingabe: [Name txt Datei]

GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])

red = 100
blue = 100
green = 100
brightness = 0


data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + ".txt")
mode = int(data[0])
red_new = int(data[1])
green_new = int(data[2])
blue_new = int(data[3]) 
brightness_new = float(data[4])
spped_new = int(data[5])
gpio_gruen = int(data[6])
gpio_rot = int(data[7])
gpio_blau = int(data[8])
update = 1

GPIO.setup(gpio_gruen, GPIO.OUT) #gruen
GPIO.setup(gpio_rot, GPIO.OUT) #rot
GPIO.setup(gpio_blau, GPIO.OUT) #blau

p_red = GPIO.PWM(gpio_rot, 100)
p_blue = GPIO.PWM(gpio_blau, 100)
p_green = GPIO.PWM(gpio_gruen, 100)


if mode == 1:
        speed = spped_new
else:
        mode = 1
        red_new = 100
        green_new = 100
        blue_new = 100
        brightness_new = 1
        speed = 3


p_green.start(green *brightness)
p_red.start(red*brightness)
p_blue.start(blue*brightness)


while mode=!0:
        

        if mode == 1:

        
                green_diff = (green_new - green)/100
                blue_diff = (blue_new - blue)/100
                red_diff = (red_new - red)/100
                helligkeit_diff = (brightness_new - brightness)/100

                for i in range(99):
                	brightness = brightness + helligkeit_diff
                        blue = blue + blue_diff
                        green = green + green_diff
                        red = red + red_diff

                	
                	p_green.ChangeDutyCycle(green * brightness)
                	p_red.ChangeDutyCycle(red * brightness)
                	p_blue.ChangeDutyCycle(blue * brightness)
                	time.sleep(speed)

                green = green_new
                red = red_new
                blue = blue_new
                brightness = brightness_new
	
                p_green.ChangeDutyCycle(green * brightness)
                p_red.ChangeDutyCycle(red * brightness)
                p_blue.ChangeDutyCycle(blue * brightness)



                print("Rot, gruen, blau, helligkeit")
                print(red ,green, blue ,brightness)

                outputfile = open("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + .txt", "w")
                outputfile.write(mode + "\n")
                outputfile.write(str(red_new) + "\n")
                outputfile.write(str(green_new) + "\n")
                outputfile.write(str(blue_new) + "\n")
                outputfile.write(str(brightness_new) + "\n")
                outputfile.write(str(spped_new()) + "\n")
                outputfile.write(str(gpio_gruen) + "\n")
                outputfile.write(str(gpio_rot) + "\n")
                outputfile.write(str(gpio_blau) + "\n")
                outputfile.write("0" + "\n")
                outputfile.close()

                waitinput()

                data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + ".txt")
                mode_new = int(data[0])
                red_new = int(data[1])
                green_new = int(data[2])
                blue_new = int(data[3])
                brightness_new = int(data[4])/100
                spped_new = int(data[5])/100
                gpio_gruen = int(data[6])
                gpio_rot = int(data[7])
                gpio_blau = int(data[8])
                update = int(data[9])


        elif mode == 2:



                counter = 0
        
                while True:
                        p_green.ChangeDutyCycle(sinus(counter) * helligkeit/100)
                        p_red.ChangeDutyCycle(sinus(counter+120) * helligkeit/100)
                        p_blue.ChangeDutyCycle(sinus(counter+240) * helligkeit/100)

                        time.sleep(0.002)
                        counter = counter +1
                
p_green.stop()
p_red.stop()
p_blue.stop()
GPIO.cleanup()












                
