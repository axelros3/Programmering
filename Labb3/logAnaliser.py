




GRANS = 3


def logAnalyzer():
    ip_lista = [] 
    antal = [] 
    try:
        with open("auth.log", encoding="utf-8") as fil: 
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
            print("Fel: hittar inte filen auth.log.") 

    for index in range(len(ip_lista)): 
        if antal[index] >= GRANS: 
            print("Misstänkt:", ip_lista[index], "–", antal[index], "misslyckade försök") 



