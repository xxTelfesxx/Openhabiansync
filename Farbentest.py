import sys
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

wartezeit = float(comand_line_arg[1])/1000
green = float(comand_line_arg[2])
red = float(comand_line_arg[3])
blue = float(comand_line_arg[4])



GPIO.setup(18, GPIO.OUT) #gruen
GPIO.setup(14, GPIO.OUT) #rot
GPIO.setup(15, GPIO.OUT) #blau



p_red = GPIO.PWM(14, 100)
p_blue = GPIO.PWM(15, 100)
p_green = GPIO.PWM(18, 100)


p_green.start(green)
p_red.start(red)
p_blue.start(blue)

time.sleep(wartezeit)

p_green.stop()
p_red.stop()
p_blue.stop()