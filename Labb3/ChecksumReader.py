


import hashlib


def berakna_sha256(filnamn): 
    with open(filnamn, "rb") as fil: 
        return hashlib.file_digest(fil, "sha256").hexdigest()



def CheckSumReader():
    filnamn = input("Fil att kontrollera: ").strip() 

    try: 
        summa = berakna_sha256(filnamn) 
    except FileNotFoundError: 
        print("Fel: filen", filnamn, "finns inte.") 
    else: 
        forvantad = input("Checksumma från tillverkaren: ").strip().lower() 
    if summa == forvantad: 
        print("OK: checksumman stämmer.") 
    else: 
        print("VARNING: checksumman stämmer inte. Använd inte filen.")



