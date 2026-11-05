##/slutprov OMPROV
# Axel Roselius/#

import ipaddress

##  vår behållare för enheter
theDevices = []


#/
# funktion som läser in och kontrollerar att nätverksadress är korrekt angiven och
# returnerar nätet som en ipadress.ip_network
# /#
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

#/
# funktion som kontrollerar om medskickad IP-adress finns i medskickat nätverk
# /#
def inNet(myNet, myIp = "192.168.10.57"):
    if ipaddress.ip_address(myIp) in myNet:
        return True
    return False


#/
# funktion för att kontrollera om en ip-adress (utan prefix) är korrekt angiven, 
# /#
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


#/
# funkton för att läsa in en nätverksadress (ip-address med prefix) och kontrollera att den är korrekt angiven
# /#
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


#/
# funktion för att läsa in en IP-adress, utan prefix, och kontrollera att den är korrekt angiven
# /#
def getIPnoPrefix(text):
    run = True
    while run:
        myIP = input(text)
        if (isIPnoPrefix(myIP)):
            run = False
    return myIP


#/
# funnktion för att läsa in ett heltal, avslutas först när ett korrekt heltal har angivits
# /#
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





#/
# funktion för att skriva ut menyvalen i huvudmeny i huvudloopen
# /#
def visa_meny(): 
	print("\nAxels – huvudmeny") 
	print("1. lägg till enhet") 
	print("2. visa alla enheter")
	print("3. ändra nätverk")
	print("0. Avsluta") 


#/
# funktion för att lägga till en ny enhet
# /#
def addDevice(myNet):
    description = ""
    newIP = ""
    run = True
    while (run):
        description = input("skriv enhetens namn eller beskrivning: ")
        if (description == ""):
            print("beskrivningen/namnet kan inte vara tomt, försök igen.")
        else:
            run = False

    run = True
    while (run):
        newIP = getIPnoPrefix("skriv in IP-adressen: ")
        if not (inNet(myNet, newIP)):
            print(f"VARNING: {newIP} är inte inom nätverket {myNet}")
        else:
            print(f"IP-adressen {newIP} finns i nätverket {myNet}")
            run = False
    print("sparar enheten i listan....")
    theDevices.append((description, newIP))
    


#/
# funktion för att skriva ut listan med enheter
# /#
def showDevices():
    print("skriver ut listan med enheter")
    index = 0
    for desc, ip in theDevices:
         index += 1
         print(f"enhet {index}, {desc} har IP-adressen {ip}")


#/
# funktion för att byta nätverket
# /#
def changeNet():
    mynet = ipaddress.ip_network(getIPwithPrefix("skriv vilket nät som skall användas: " ))
    return mynet


#/
# Funktion som innehåller huvudloopen
# /#
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


##anropar startpunkten för själva programmet
startpunkt()