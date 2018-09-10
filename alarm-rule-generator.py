import numpy
import sys
			
# eingabe: [Name txt Datei] [Stunden] [Minuten]

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])
stunden = str(comand_line_arg[2])
minuten = str(comand_line_arg[3])


outputfile = open("/etc/openhab2/rules/" + nametxt + ".rules", "w")
		

outputfile.write('rule "Abendallarm"' + "\n")
outputfile.write('when Time cron "0 ' + minuten +" " + stunden + ' 1/1 * ? *"' + "\n")
outputfile.write("then sendCommand(Blinds_controll, 2)" + "\n")
outputfile.write("end")
outputfile.close()














                
