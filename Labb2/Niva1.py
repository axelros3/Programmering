
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

print("Välkommen till svarstidbedömmaren\njag vill ha svarstiden")
mySvarstid = int(input("Ge mig svarstiden i millisekunder: "))

print(f"bedömmningen av svarstiden är {timeJudge(mySvarstid)}")

