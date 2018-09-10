import numpy
			
# eingabe: [Name txt Datei] [Stunden] [Minuten]

comand_line_arg = sys.argv

nametxt = str(comand_line_arg[1])
stunden = int(comand_line_arg[2])
minuten = int(comand_line_arg[3])


outputfile = open("/etc/openhab2/rules/" + nametxt + ".rules", "w")
		

outputfile.write('Rule "Abendallarm"' + "\n")
outputfile.write('when Time cron 0 ' +minuten +" " + stunden + "* * ? *" + "\n")
outputfile.write("then Blinds_controll=2" + "\n")
outputfile.write("end")
outputfile.close()














                
