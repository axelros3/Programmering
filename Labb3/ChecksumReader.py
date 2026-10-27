


import hashlib
import DeltaUtilities


def berakna_sha256(filnamn): 
    with open(filnamn, "rb") as fil: 
        return hashlib.file_digest(fil, "sha256").hexdigest()



def CheckSumReader():
    summa=0
    forvantad = 1

    ## hämta sökvägen till mappen som programmet arbetar i
    filePath = DeltaUtilities.myFilePath()

    filnamn = input("Ange namn på fil i mappen Labb3 att kontrollera: ").strip() 
    
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



