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
	print("\n\nDeltas Multilösning – huvudmeny") 
	print("1. Service Kontroll") 
	print("2. Log kontroll")
	print("3. fil kontrol /(hashsumma/)")
	print("4. Subnäts planerare")
	print("5. Swich konfigurations Generator")
	print("6. lösenordsKontrol")
	print("0. Avsluta") 



def deltaStartPoint(): # Huvudloop
	run = True
	while (run): 
		visa_meny() 
		val = DeltaUtilities.las_heltal("skriv ett heltal motsvarande det program du vill köra\nendast sifror mellan 0 och 6 kommer godkännas: ", 0, 6)

		match val:
			case 0:
				run = False
			case 1:
				serviceControl.ServiceControl()
			case 2:
				logAnaliser.startLogAnalyzer()
			case 3:
				ChecksumReader.CheckSumReader()
			case 4:
				subNetPlanner.SubNetPlanner()
			case 5:
				ConfigGenerator.ConfigGenerator()
			case 6:
				PasswordControl.PasswordControl()
			
		
		

deltaStartPoint()
