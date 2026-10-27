


import hashlib
import os


def berakna_sha256(filnamn): 
    with open(filnamn, "rb") as fil: 
        return hashlib.file_digest(fil, "sha256").hexdigest()



def CheckSumReader():
    filnamn = input("Ange namn på fil i mappen Labb3 att kontrollera: ").strip() 
    summa=0
    forvantad = 1
    full_path = os.path.realpath(__file__)
    filePath = os.path.dirname(full_path) + "/"
    try: 
        summa = berakna_sha256(filePath + filnamn) 
    except FileNotFoundError: 
        print("FilFel: filen", filePath + filnamn, "går tyvär inte att hitta i mappen Labb3.") 
    else: 
        forvantad = input("kopiera in Checksumma från tillverkaren\ntänk på att den skall vara 64 tecken lång: ").strip().lower() 
    
        if summa == forvantad: 
            print("Filen är OK att använda: checksumman stämmer.") 
        else: 
            print("VARNING: checksumman stämmer inte. Använd inte filen.")



