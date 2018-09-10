import numpy
import sys
			
# eingabe: [Name txt Datei] [Stunden] [Minuten] [auf ab? 0= auf, 2 = ab] [Evening_alarm, Morning_alarm]

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])
stunden = str(comand_line_arg[2])
minuten = str(comand_line_arg[3])
mode = str(comand_line_arg[4])
vergleich =str(comand_line_arg[5])

outputfile = open("/etc/openhab2/rules/" + nametxt + ".rules", "w")
		

outputfile.write('rule "Abendallarm"' + "\n")
outputfile.write('when Time cron "0 ' + minuten +" " + stunden + ' 1/1 * ? *"' + "\n")
outputfile.write("then" + "\n")
outputfile.write("if (" + vergleich + ".state==1){" + "\n")
outputfile.write("sendCommand(Blinds_controll, " + mode + ")}" + "\n")
outputfile.write("end")
outputfile.close()














                
