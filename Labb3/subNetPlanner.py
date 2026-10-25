

import ipaddress



def SubNetPlanner():
    while True: 
        svar = input("Nätverk, till exempel 192.168.10.0/24: ").strip() 
        try: 
            natet = ipaddress.ip_network(svar) 
        except ValueError: 
            print("Fel: skriv ett nätverk som 192.168.10.0/24.") 
        else: 
            break


    print("Nätmask:", natet.netmask) 
    print("Broadcast:", natet.broadcast_address) 
    print("Användbara värdar:", len(list(natet.hosts()))) 
    print("192.168.10.57 finns i nätet:", ipaddress.ip_address("192.168.10.57") in natet) 
    for delnat in natet.subnets(new_prefix=26): 
        print("Delnät:", delnat) 
