#//
# Lösningsförslag till Problem 1 i programmeringskursens labb 1
# författare Axel Roselius
# /#

print("välkommen till värdnamnsgeneratorn\nge mig din platskod")
platskod = input("endast 3 tecken tack: ")
print("nu vill jag ha din enhetstyp")
enhetstyp = input("även här vill jag bara ha 3 tecken:")
print("och till slut vill jag ha det senast använda datornummret")
lastnumber = int(input("här vill jag ha max 2 st siffror och om värdet är under 10 vill jag endast ha en siffra:"))

platskod = str.lower(platskod)
enhetstyp = str.lower(enhetstyp)

hostnamn = platskod + "-" + enhetstyp + "-"
##kontrollera att siffran är korrekt angiven
if(lastnumber+1 > 99):
    print("numret är för högt")
if(lastnumber+1 <10):
    hostnamn =+ "0" + str(lastnumber+1)
    print("det nya värdnamnet är: " + hostnamn)
else:
    hostnamn =+ str(lastnumber+1)
    print("det nya värdnamnet är: " + hostnamn)

print("hejdå")




