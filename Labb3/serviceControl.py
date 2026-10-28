

import socket
import DeltaUtilities
from subNetPlanner import isIPnoPrefix



def port_svarar(myHost, port): 
    try: 
        with socket.create_connection((myHost, port), timeout=2): 
            return True 
    except OSError: 
        return False


def checkStatus(serverlist, portlist):
    for ip in serverlist:
        for port in portlist:
            if port_svarar(ip, port):
                print(f"server på IP-adress {ip} svarar på port {port}") 
            else: 
                print(f"Varning: server på IP-adress {ip} svarar INTE på port {port}")


def addServer(serverlist):
    print("skriv in IP-adressen till servern som du vill lägga till")
    run = True
    while run:
        nyIP = input("skriv bara IP-adressen, på formen 192.168.20.32: ")   # för nu så förutsätter vi att den är korrekt 
        if(isIPnoPrefix(nyIP)):
            run = False

    if nyIP in serverlist:
        print("den IP-adressen finns redan i listan")
        return serverlist
    print("lägger till den nya IP-adressen i listan")
    return serverlist.append(nyIP)


def addPort(portlist):
    print("skriv in portnummret som du vill lägga till")
    nyport = DeltaUtilities.las_heltal("skriv bara heltal mellan 0 och 65535: ", 0, 65535)
    if nyport in portlist:
        print("den porten finns redan i listan")
        return portlist
    print("lägger till den nya IP-adressen i listan")
    return portlist.append(nyport)


def serviceMenu():
    print("\n\nService Control – menu")
    print("1. add a server")
    print("2. add a port")
    print("3. check status")
    print("0. Avsluta") 

def ServiceControl():
    servrar = ["127.0.0.1"] 
    portar = [8000, 8001] 
    run = True
    print("välkommen till service kontrollen")
    while (run):
        serviceMenu()
        val = DeltaUtilities.las_heltal("skriv ett heltal motsvarande den funktion du vill använda: ",0, 3)
        match val:
            case 0:
                run = False
            case 1:
                servrar = addServer()
            case 2:
                portar = addPort()
            case 3:
                checkStatus(servrar,portar)
    print("avslutar nu service kontrollen")


