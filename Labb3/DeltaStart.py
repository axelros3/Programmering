#//
# Lösningsförslag till i programmeringskursens labb 3
# författare Axel Roselius
# /#


#/
#import os, sys
#FILELOCATION = os.path.abspath(os.path.dirname(sys.argv[0]))
#pathParts = FILELOCATION.split("\\")
#index = 0
#for part in pathParts:
#	print(f"part{index}: {part}")
#
#/


import ConfigGenerator
import ChecksumReader
import serviceControl
import subNetPlanner
import PasswordControl
import logAnaliser





# Frågar tills användaren skriver ett heltal mellan minsta och storsta 
def las_heltal(fraga, minsta, storsta): 
	while True: 
		try:
			tal = int(input(fraga)) 
		except ValueError: 
			print("Fel: skriv ett heltal, till exempel", minsta) 
		else: 
			if minsta <= tal <= storsta: 
				return tal 
		print("Fel: talet måste vara", minsta, "till", storsta) 


def visa_meny(): 
	print("\n\n[Programmets namn] – huvudmeny") 
	print("1. Service Control") 
	print("2. Log analyzer")
	print("3. Checksum control")
	print("4. Subnet Planner")
	print("5. Config Generator")
	print("6. Password Control")
	print("0. Avsluta") 



def deltaStartPoint(): # Huvudloop
	run = True
	while (run): 
		visa_meny() 
		val = las_heltal("Välj 0, 1, 2 ... 6: ", 0, 6)

		match val:
			case 0:
				run = False
			case 1:
				serviceControl.ServiceControl()
			case 2:
				logAnaliser.logAnalyzer()
			case 3:
				ChecksumReader.CheckSumReader()
			case 4:
				subNetPlanner.SubNetPlanner()
			case 5:
				ConfigGenerator.ConfigGenerator()
			case 6:
				PasswordControl.PasswordControl()
			
		
		

deltaStartPoint()
