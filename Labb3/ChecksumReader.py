


import hashlib
import os


def berakna_sha256(filnamn): 
    with open(filnamn, "rb") as fil: 
        return hashlib.file_digest(fil, "sha256").hexdigest()



def CheckSumReader():
    filnamn = input("Fil att kontrollera: ").strip() 
    summa=0
    forvantad = 1
    full_path = os.path.realpath(__file__)
    filePath = os.path.dirname(full_path) + "/"
    try: 
        summa = berakna_sha256(filePath + filnamn) 
    except FileNotFoundError: 
        print("Fel: filen", filePath + filnamn, "finns inte.") 
    else: 
        forvantad = input("Checksumma från tillverkaren: ").strip().lower() 
    
        if summa == forvantad: 
            print("OK: checksumman stämmer.") 
        else: 
            print("VARNING: checksumman stämmer inte. Använd inte filen.")



