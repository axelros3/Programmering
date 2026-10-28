

from ast import Try
import ipaddress
import DeltaUtilities


def getNet():
    run = True
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
        except ValueError:
            print("det blev tyvär fel någonstans vänligen dubbelkolla att du skriver rätt och försök igen.\n")
        else:
            run = not isIPnoPrefix(myAdress)
    return myIP


def SubNetPlanner():
    
    natet = getNet()
    print("här kommer egenskaperna hos det angivna nätet:")
    print("Nätmask:", natet.netmask) 
    print("Broadcast:", natet.broadcast_address) 
    print("Användbara värdar:", len(list(natet.hosts())))

    print(f"\nfinns 192.168.10.57  i nätet: {inNet(natet)}\n")

    print("ange prefix att använda för subnät")
    myPrefix = DeltaUtilities.las_heltal("skriv prefixet som ett heltal: ", 1, 32)

    print("dessa subnät finns för prefixet")
    for delnat in natet.subnets(new_prefix = myPrefix): 
        print("Delnät:", delnat) 
