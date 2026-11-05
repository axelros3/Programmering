##/slutprov OMPROV
# Axel Roselius/#

import ipaddress

theDevices = []

def getNet():
    run = True
    myNet 
    while run: 
        svar = getIPwithPrefix("skriv nätverkets IP med prefix, till exempel 192.168.10.0/24: ")
        try: 
            myNet = ipaddress.ip_network(svar) 
        except ValueError: 
            print("Fel: skriv en IPv4-adress med 4 st oktetter mellan 0 och 255\noch ett prefix mellan 1 och 32 tex 192.168.10.0/24.") 
        else: 
            run = False
    return myNet


def inNet(myNet, myIp = "192.168.10.57"):
    if ipaddress.ip_address(myIp) in myNet:
        return True
    return False


##  en liten kontrollfunktion för ip-adress är plannerad utan prefix
def isIPnoPrefix(myAdress):
    try:
        myoktetts = myAdress.split(".")         #   sära på okteterna
            
        for index in range(len(myoktetts)):
            myoktetts[index] = int(myoktetts[index])
    except ValueError:
        print("det blev tyvär fel, en av oktetterna gick inte att konvertera till heltal, vänligen försök igen.\n")
        return False
    for oktet in myoktetts:
        if (not (0 <= oktet <=255)):
            print(f"oktett {myoktetts.index(oktet)+1} är inte korrekt angiven: {oktet}")
            return False
    return True


##  en liten kontrollfunktion för ip-adress är plannerad med prefix
def getIPwithPrefix(text):
    run = True
    while run:
        myIP = input(text).strip()
        try:
            myAdress, myprefix = myIP.split("/")    #   sära på prefix och ip-adresesn
            
            myprefix = int(myprefix)
            if  (1 <= myprefix <= 32):
                run = False
            else:
                 print("Prefixet är inte i intervallet 1 till 32. försök igen")
        except ValueError:
            print("det blev tyvär fel vid konvertering till heltal av prefixet, vänligen dubbelkolla att du skriver rätt och försök igen.\n")
        else:
            run = not isIPnoPrefix(myAdress)
    return myIP


def getIPnoPrefix(text):
    run = True
    while run:
        myIP = input(text)
        if (isIPnoPrefix(myIP)):
            run = False
    return myIP


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
	print("\nAxels – huvudmeny") 
	print("1. lägg till enhet") 
	print("2. visa alla enheter")
	print("3. ändra nätverk")
	print("0. Avsluta") 



def addDevice(myNet):
    description = input("skriv enhetens namn eller beskrivning: ")
    newIP = getIPnoPrefix("skriv in IP-adressen: ")
    if not (inNet(myNet, newIP)):
        print(f"VARNING: {newIP} är inte inom nätverket {myNet}")
    else:
         print(f"IP-adressen {newIP} finns i nätverket {myNet}")
    print("sparar enheten i listan....")
    theDevices.append((description, newIP))
    



def showDevices():
    print("skriver ut listan med enheter")
    for desc, ip in theDevices:
         print(f"enheten {desc} har IP-adressen {ip}")



def changeNet():
    mynet = ipaddress.ip_network(getIPwithPrefix("skriv vilket nät som skall användas: " ))
    return mynet



def startpunkt():
    run = True
    
    print("vi behöver ha ett huvud nätverk, anges på formatet 192.168.10.0/24.")
    theNet = changeNet()
    while run:
        visa_meny()
        menyval = las_heltal("skriv endast heltal för att välja alternativen i menyn: ", 0, 3)
        match menyval:
            case 0:
                run = False
            case 1:
                addDevice(theNet)
            case 2:
                showDevices()
            case 3:
                theNet = changeNet()


startpunkt()