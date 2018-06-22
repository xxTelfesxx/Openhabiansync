import RPi.GPIO as GPIO
import time
import os

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

zeitstempel = []
wartezeit = []

for i in range(73):
	info = inputfile.readline()
	zeitstempel.append((float(info[0:7])))

	
for ii in range(72):
	wartezeit.append(zeitstempel[ii+1]-zeitstempel[ii])
	
	

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GOOOOOOOOOOOO")

os.system('mpg321 does_your_mother_knowcut.mp3 &')

time.sleep(0.01)

print(wartezeit)

for iwartezeit in wartezeit:
	time.sleep(iwartezeit-0.02)
		
	blink()
	#print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
	#print(" ")
	

