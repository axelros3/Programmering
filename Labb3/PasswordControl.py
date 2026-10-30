

import getpass
import DeltaUtilities

MIN_LANGD = 15 
VANLIGA = ["123456", "password", "qwerty123", "sommar2026", "lösenord"]


def kontrollera(losenord, anvandarnamn): 
    problem = [] 
    if len(losenord) < MIN_LANGD: 
        problem.append("det angivna lösenordet är för kort – minst 15 tecken krävs") 
    if losenord.lower() in VANLIGA: 
        problem.append("det angivna lösenordet finns i listan över vanliga lösenord") 
    if anvandarnamn.lower() in losenord.lower(): 
        problem.append("det angivna lösenordet innehåller användarnamnet") 
        return problem 


def PasswordControl():
    print("välkommen till lösenordskontrollen")
    print("här skall du skriva ditt användarnamn och det lössenord du tänkt sätta på ditt konto\n")
    run = True
    while (run):
        myUsername = input("vad är ditt anvädarnamn? ")
        myPassword = getpass.getpass("skriv ditt lösenord: ")

        print(kontrollera(myUsername, myPassword))

        print("vill du prova igen?")
        if not (DeltaUtilities.myTryAgain()):
            run = False
            print("Hej då, välkommen åter")

    



