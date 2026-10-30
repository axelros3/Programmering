


from math import log

import DeltaUtilities

GRANS = 3


def logAnalyzer(logfil):
    ip_lista = [] 
    antal = []

    ## hämta sökvägen till mappen som programmet arbetar i
    filePath = DeltaUtilities.myFilePath()
    print(f"\n\nangiven loggfil: {filePath + logfil}:")
    try:
        with open(filePath + logfil, encoding="utf-8") as fil: 
            for rad in fil: 
                if "Failed password" in rad: 
                    delar = rad.split() 
                    ip = delar[delar.index("from") + 1] 
                    if ip in ip_lista: 
                        i = ip_lista.index(ip) 
                        antal[i] = antal[i] + 1 
                    else: 
                        ip_lista.append(ip)
                        antal.append(1) 
    except FileNotFoundError: 
            print("fil Fel: hittar tyvär inte filen auth.log.") 

    for index in range(len(ip_lista)): 
        if antal[index] >= GRANS: 
            print(f"Misstänkt aktivitet: från IP {ip_lista[index]} har vi {antal[index]} misslyckade inloggningsförsök") 


def startLogAnalyzer():
    print("vilken logfil vill du kontrollera?")
    logfil = input("hela filnamnet inklusive filändelsen tack: ")
    logAnalyzer(logfil)
