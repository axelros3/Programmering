#//
# Lösningsförslag till del 4: refaktorering i programmeringskursens labb 2
# författare Axel Roselius
# /#

TIME_LIMIT = 300

##/
# räknar ut den totala summan av värdena i listan
# indata : responsetimes innehållande en lista med svarstider
# utdata : returnerar totsum som är totalsumman
# /#
def mySum(responsetimes):
    totsum = 0
    for val in responsetimes:
        totsum += val
    return totsum

##/
# räknar ut hur många av värdena i listan som överstiger gränsen,
# och därför anses ha lång svarstid.
# indata : responses innehållande en lista med svarstider
# utdata : returnerar nrLongTime som är antalet som överstiger gränsen
# /#
def myLongTimeCheck(responses):
    nrLongTime = 0
    for val in responses:
        if (val > TIME_LIMIT):
            nrLongTime += 1
    return nrLongTime

##/
# räknar ut medelvärdet av värdena i listan
# indata : responselist innehållande en lista med svarstider
# utdata : returnerar totalsumman / antalet värden
# /#
def myMeanValue(responselist):
    return mySum(responselist)/len(responselist)


svarstider_ms=[120,95,310,80,450]

print("Totalsumman är: ",mySum(svarstider_ms))
print("Snittvärdet är: ",myMeanValue(svarstider_ms))
print("Antalet servrar med lång svarstid: ",myLongTimeCheck(svarstider_ms))
