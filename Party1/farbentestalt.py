import RPi.GPIO as GPIO
import time

def blink():
	p_green.start(100)
	p_red.start(100)
	p_blue.start(100)
	print("Blink")
	time.sleep(0.01)
	
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

inputfile = open("Textspur.txt")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GOOOOOOOOOOOO")

for i in range(77):
	inf = inputfile.readline()
	inf = float(inf[0:7])
	
	while zeitmessung < inf:
		zeitmessung = zeitmessung +0.001
		time.sleep(0.001)
	
	blink()
	zeitmessung = zeitmessung +0.01
	

