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








