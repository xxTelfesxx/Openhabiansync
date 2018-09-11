import sys
import numpy
import math

			
# eingabe: [Name txt Datei] [Mode,0 = Aus, 1 = Color static, 2 = colorfading, 999 = unveraendert] [Helligkeit in %] [Gruen in %] [Rot in %] [Blau in %]

GPIO.setmode(GPIO.BCM)

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])
mode = int(comand_line_arg[2]) #mode 0 = ausschalten
helligkeit = int(comand_line_arg[3])
gruen_neu = float(comand_line_arg[4])
rot_neu = float(comand_line_arg[5])
blau_neu = float(comand_line_arg[6])



data = numpy.genfromtxt("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + ".txt")
mode_old = int(data[0])
red_old = int(data[1])
green_old = int(data[2])
blue_old = int(data[3]) 
brightness_old = int(data[4])
spped_old= int(data[5])
gpio_gruen = int(data[6])
gpio_rot = int(data[7])
gpio_blau = int(data[8])
update = int(data[9])

#unveraendert - daten aus datei fuer werte setzen
if helligkeit == 999:
        helligkeit = brightness_old
if gruen_neu == 999:
        gruen_neu = green_old
if rot_neu == 999:
        rot_neu = red_old
if blau_neu == 999:
        blau_neu = blue_old
if mode == 999:
        mode = mode_old
if speed == 999:
        speed = speed_old


outputfile = open("/home/openhabian/gitsync/Openhabiansync/Openhab-lightcontrol/" + nametxt + ".txt", "w")
outputfile.write(mode + "\n")
outputfile.write(str(rot_neu) + "\n")
outputfile.write(str(gruen_neu) + "\n") 
outputfile.write(str(blau_neu) + "\n")
outputfile.write(str(helligkeit/100) + "\n")
outputfile.write(str(speed) + "\n")
outputfile.write(str(gpio_gruen) + "\n")
outputfile.write(str(gpio_rot) + "\n")
outputfile.write(str(gpio_blau) + "\n")
outputfile.write("1" + "\n")
outputfile.close()















                
