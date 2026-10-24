


INTERFACE = "GigabitEthernet1/0/" 
def access_port(port, vlan, beskrivning): 
    print("interface", INTERFACE + str(port)) 
    print(" description", beskrivning) 
    print(" switchport mode access") 
    print(" switchport access vlan", vlan) 
    print("!") 
access_port(5, 20, "Skrivare plan 2") 
access_port(6, 30, "Mötesrum Ek") 


