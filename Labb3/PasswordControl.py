



MIN_LANGD = 15 
VANLIGA = ["123456", "password", "qwerty123", "sommar2026", "lösenord"] 
def kontrollera(losenord, anvandarnamn): 
    problem = [] 
    if len(losenord) < MIN_LANGD: 
        problem.append("för kort – minst 15 tecken") 
    if losenord.lower() in VANLIGA: 
        problem.append("finns i listan över vanliga lösenord") 
    if anvandarnamn.lower() in losenord.lower(): 
        problem.append("innehåller användarnamnet") 
        return problem 
print(kontrollera("Sommar2026", "anna")) 
print(kontrollera("anna-gillar-kaffe", "anna")) 
print(kontrollera("blå häst springer i regnet", "anna"))



