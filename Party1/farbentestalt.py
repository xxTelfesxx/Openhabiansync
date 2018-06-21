import RPi.GPIO as GPIO
import time

def blink(zeit):
	p_green.start(100)
	p_red.start(100)
	p_blue.start(100)
	
	time.sleep(zeit)
	
	p_green.stop()
	p_red.stop()
	p_blue.stop()


GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.OUT) #gruen
GPIO.setup(14, GPIO.OUT) #rot
GPIO.setup(15, GPIO.OUT) #blau


p_red = GPIO.PWM(14, 100)
p_blue = GPIO.PWM(15, 100)
p_green = GPIO.PWM(18, 100)

zeitmessung = 0

inputfile = open(Textspur.txt)

for i in range(77):
	inf = inputfile.readline()
	inf = float(inf[0:7])
	
	if zeitmessung < inf:
		zeitmessung = zeitmessung +0.001
		time.sleep(1)
	else:
		blink(10)
		zeitmessung = zeitmessung +0.01
	

