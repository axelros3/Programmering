#//
# Lösningsförslag till del 4: refaktorering i programmeringskursens labb 2
# författare Axel Roselius
# /#

TIME_LIMIT = 300

def mySum(responsetimes):
    totsum = 0
    for val in responsetimes:
        totsum += val
    return totsum

def myLongTimeCheck(responses):
    nrLongTime = 0
    for val in responses:
        if (val > TIME_LIMIT):
            nrLongTime += 1
    return nrLongTime

def myMeanValue(responselist):
    return mySum(responselist)/len(responselist)


svarstider_ms=[120,95,310,80,450]

print("Totalsumman är: ",mySum(svarstider_ms))
print("Snittvärdet är: ",myMeanValue(svarstider_ms))
print("Antalet servrar med lång svarstid: ",myLongTimeCheck(svarstider_ms))
