
#//
# Lösningsförslag till Nivå 1 i programmeringskursens labb 2
# författare Axel Roselius
# /#

def timeJudge(svarstid):
    if (svarstid < 0):
        return "Ogiltigt Värde"
    elif(svarstid >= 500):
        return "Ingen användbar kontakt"
    elif(svarstid >= 150):
        return "Långsam"
    elif(svarstid >= 50):
        return "Bra"
    return "Utmärkt" 


run = True
print("Välkommen till svarstidbedömmaren\njag vill ha svarstiden")
while(run):
    mySvarstid = int(input("Ge mig svarstiden i millisekunder: "))
    myJudgedTime = timeJudge(mySvarstid)

    if(myJudgedTime != "Ogiltigt Värde"):
        run = False
    else:
        print(f"{myJudgedTime} försök igen")



print(f"bedömmningen av svarstiden är {myJudgedTime}")

