


INTERFACE = "GigabitEthernet1/0/"

##/
#   funktionen acces_port tar emot fysisk port (RJ45), nummret på VLAN och en beskrivning av vad porten skall användas för
#   och skiver sedan ut kommandon för att konfigurera angiven port så att den blir en accessport som fungerar med det
#   angivna VLANet.
#indata:    port heltal
#           vlan heltal
#           beskrivning textsträng
#/#

import DeltaUtilities

def access_port(port, vlan, beskrivning):
    print("följande skall skrivas/kopieras in i konfigurationsläget dvs efter \"config terminal\":")
    print("interface", INTERFACE + str(port)) 
    print(" description", beskrivning) 
    print(" switchport mode access") 
    print(" switchport access vlan", vlan) 
    print(" end, om du är klar med alla portar eller exit, om du vill konfigurera fler portar ") 


##/
#   startpunkt tillika "huvudloop" för konfigurationsgeneratorn/#
def ConfigGenerator():
    run = True
    while (run):
        print("\n\nmata in portnummer, VLAN och en beskrivning av vad porten skall användas till.\ntex 5, 20, \"skrivare plan 2\"")
    
        myPort = DeltaUtilities.las_heltal("skriv här vilken port på switchen som skall användas: ", 1, 32)
        myVlan = DeltaUtilities.las_heltal("skriv här vilket VLAN som skall användas: ",0 , 4095)
        myDescription = input("skriv här beskrivningen för porten´: ")

        access_port(myPort, myVlan, myDescription)
        print("vill du fortsätta med en ny port?")
        myAnswer = DeltaUtilities.myTryAgain()
        if (not myAnswer):
            run = False
            print("Hej då, välkommen åter")
        
            

