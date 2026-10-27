##/
#hjälpfunktioner som läsheltal
#
#/#

import os

# Frågar tills användaren skriver ett heltal mellan minsta och största
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


def myFilePath():
	## hämta sökvägen till mappen som programmet arbetar i
	full_path = os.path.realpath(__file__)
	filePath = os.path.dirname(full_path) + "/"
	return filePath


def myTryAgain():
	runAgain = True
	while (runAgain):
            myAnswer = input("endast svar innehållande j, ja, n eller nej kommer accepteras: ")
            if (myAnswer == "n" or myAnswer == "nej"):
                return False
            elif (myAnswer == "j" or myAnswer == "ja"):
                return True
            else:
                print("du har svarat fel på en ja eller nej fråga...\nVänligen svara bara ja eller nej")
    

