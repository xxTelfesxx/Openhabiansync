import sys
import RPi.GPIO as GPIO
import time

print("TEST")

GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

green = float(comand_line_arg[1])
red = float(comand_line_arg[2])
blue = float(comand_line_arg[3])



GPIO.setup(18, GPIO.OUT) #gruen
GPIO.setup(14, GPIO.OUT) #rot
GPIO.setup(15, GPIO.OUT) #blau



p_red = GPIO.PWM(14, 100)
p_blue = GPIO.PWM(15, 100)
p_green = GPIO.PWM(18, 100)


p_green.start(green)
p_red.start(red)
p_blue.start(blue)