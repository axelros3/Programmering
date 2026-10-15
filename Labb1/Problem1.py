#//
# Lösningsförslag till Problem 1 i programmeringskursens labb 1
# med tillägget för domännamn
# författare Axel Roselius
# /#

print("välkommen till värdnamnsgeneratorn\nge mig din platskod")
platskod = input("endast 3 tecken tack: ")
print("nu vill jag ha din enhetstyp")
enhetstyp = input("även här vill jag bara ha 3 tecken:")
print("och till slut vill jag ha det senast använda datornummret")
lastnumber = int(input("här vill jag ha max 2 st siffror och om värdet är under 10 vill jag endast ha en siffra:"))

print("och avslutningsvis vill jag ha ditt domännamn")
myDomainName = input("använd bara små tecken, tack : ")

platskod = str.lower(platskod)
enhetstyp = str.lower(enhetstyp)

hostnamn = platskod + "-" + enhetstyp + "-"
##kontrollera att siffran är korrekt angiven
if(lastnumber+1 > 99):
    print("numret är för högt")
elif(lastnumber+1 <10):
    hostnamn = hostnamn + "0" + str(lastnumber+1)
    print("det nya värdnamnet är: " + hostnamn)
else:
    hostnamn = hostnamn + str(lastnumber+1)
    print(f"det nya värdnamnet är: {hostnamn}.{myDomainName}")

print("hejdå")




