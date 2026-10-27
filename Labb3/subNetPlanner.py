

import ipaddress
import DeltaUtilities


def getNet():
    run = True
    while run: 
        svar = input("skriv nätverkets IP med prefix, till exempel 192.168.10.0/24: ").strip() 
        try: 
            myNet = ipaddress.ip_network(svar) 
        except ValueError: 
            print("Fel: skriv ett nätverk som 192.168.10.0/24.") 
        else: 
            run = False
    return myNet


def inNet(myNet, myIp = "192.168.10.57"):
    if ipaddress.ip_address(myIp) in myNet:
        return True
    return False


##  en liten kontrollfunktion för ip-adress är plannerad utan prefix
##  en liten kontrollfunktion för ip-adress är plannerad med prefix


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
