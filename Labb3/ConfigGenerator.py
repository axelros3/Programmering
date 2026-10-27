


INTERFACE = "GigabitEthernet1/0/"

##/
#   funktionen acces_port tar emot fysisk port (RJ45), nummret på VLAN och en beskrivning av vad porten skall användas för
#   och skiver sedan ut kommandon för att konfigurera angiven port så att den blir en accessport som fungerar med det
#   angivna VLANet.
#indata:    port heltal
#           vlan heltal
#           beskrivning textsträng
#/#
def access_port(port, vlan, beskrivning):
    print("följande skall skrivas/kopieras in i konfigurationsläget dvs efter \"config terminal\":")
    print("interface", INTERFACE + str(port)) 
    print(" description", beskrivning) 
    print(" switchport mode access") 
    print(" switchport access vlan", vlan) 
    print("!") 


##/
#   startpunkt tillika "huvudloop" för konfigurationsgeneratorn/#
def ConfigGenerator():
    print("mata in portnummer, VLAN och en beskrivning av vad porten skall användas till.\ntex 5, 20, \"skrivare plan 2\"")
    myPort = las_heltal("", 0, 4095)
    myVlan
    myDescription =
    access_port(5, 20, "Skrivare plan 2") 
    access_port(6, 30, "Mötesrum Ek") 


