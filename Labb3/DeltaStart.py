#//
# Lösningsförslag till i programmeringskursens labb 3
# författare Axel Roselius
# /#





import ConfigGenerator
import ChecksumReader
import serviceControl
import subNetPlanner
import PasswordControl
import logAnaliser
import DeltaUtilities



def visa_meny(): 
	print("\n\nDeltas Multisolver – huvudmeny") 
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
		val = DeltaUtilities.las_heltal("skriv ett heltal motsvarande det program du vill köra\nendast sifror mellan 0 och 6 3 kommer godkännas: ", 0, 6)

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
