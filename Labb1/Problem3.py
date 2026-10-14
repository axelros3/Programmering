#//
# Lösningsförslag till Problem 3 i programmeringskursens labb 1
# författare Axel Roselius
# /#

print("välkommen till subnätskollen\njag vill ha nätmasken i prefixform")
myPrefix = int(input("skriv siffror mellan 0 och 32, skriv bara värdet: /"))

print("nu vill jag ha antalet använda IP-adresser")
incomingUsedNr = int(input("skriv antalet med siffror : "))


myBits = 32 - myPrefix                      ##  beräkna antalet hostbitar
myTotalNr = 2**myBits                       ##  beräkna totalt antal 
myUsableNr = myTotalNr - 2                  ##  beräkna användbarat antal
myAvailableNr = myUsableNr - incomingUsedNr ##  beräkna tillgängligt antal

##  
if(myAvailableNr > 0):
    print ("det finns platser kvar i subnätet")
else:
    print("Det finns tyvär inte plats i subnätet.")    

print(f"""\ntotalt finns det {myTotalNr} IP-adresser i subnätet
varav {myUsableNr} är användbara för enheter.
av dessa finns det {myAvailableNr } kvar att använda""")

print("Hejdå")





