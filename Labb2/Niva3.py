#//
# Lösningsförslag till Nivå 3 i programmeringskursens labb 2
# författare Axel Roselius
# /#

import statistics

def mySum(mylist):
    myTempSum = 0
    for sum in mylist:
        myTempSum += sum
    return myTempSum

def myMiddleValue(mylist):
    return (mySum(mylist)/len(mylist))

def myBiggestValue(mylist):
    myCurrentBiggest = 0
    for val in mylist:
        if(val > myCurrentBiggest):
            myCurrentBiggest = val
    return myCurrentBiggest

def myNumbersAbove(mylist, minimumLimit):
    nrAboveLimit = 0
    for val in mylist:
        if(val >= minimumLimit):
            nrAboveLimit += 1
    return nrAboveLimit

nrfailedLogins = [0, 2, 1, 7, 0, 12, 3,0]

print(f"summan är: {mySum(nrfailedLogins)}\noch pytons inbyggda säger: {sum(nrfailedLogins)}\n\n")
print(f"medelvärdet är: {myMiddleValue(nrfailedLogins)}\noch pytons inbyggda säger: {statistics.mean(nrfailedLogins)}\n\n")
print(f"största värdet är: {myBiggestValue(nrfailedLogins)}\noch pytons inbyggda säger: {max(nrfailedLogins)}\n\n")
print(f"antalet på gränsen eller högre är: {myNumbersAbove(nrfailedLogins)}\noch pyton verkar inte inbyggd funktion för detta")


