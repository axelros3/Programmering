
#//
# Lösningsförslag till Problem 1 i programmeringskursens labb 2
# författare Axel Roselius
# /#

##Konstanter
HEMLIG_PORT = 443
MAX_ANTAL_GISSNINGAR = 10

def myValueCheck(gissning):
    if(gissning > HEMLIG_PORT):
        return "För högt"
    elif(gissning < HEMLIG_PORT):
        return "För lågt"
    return "Korrekt"

myGuessedCorrect = False
myNrofGuesses = 0

print("Välkommen till gissningsleken")
while(myNrofGuesses < MAX_ANTAL_GISSNINGAR and (not myGuessedCorrect)):
    myGuess = int(input("Skriv in din gissning med siffror: "))
    myNrofGuesses += 1
    response = myValueCheck(myGuess)
    if(response == "Korrekt"):
        print(f"du har gissat rätt!!\ndu har använt {myNrofGuesses} försök")
        myGuessedCorrect = True
    else:
        print(response)

if(not myGuessedCorrect):
   print(f"Du har gissat fel 10 gånger\nRätt svar skall vara: {HEMLIG_PORT}")





