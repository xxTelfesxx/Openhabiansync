import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

wartezeit = float(comand_line_arg[1])


GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

time.sleep(wartezeit)

GPIO.output(18, GPIO.LOW)

print("gloffen", wartezeit)