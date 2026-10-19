#//
# Lösningsförslag till Nivå 3 i programmeringskursens labb 2
# författare Axel Roselius
# /#


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
        if(val > minimumLimit):
            nrAboveLimit += 1
    return nrAboveLimit

nrfailedLogins = [0, 2, 1, 7, 0, 12, 3,0]






