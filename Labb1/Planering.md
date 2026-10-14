Labb1 - Planering

##Problem 1
    ##indata: data/information som fås ifrån "användaren",
    ##i detta fall platskod, enhetstyp och senast använt nummer.
    ##utdata: data/information som programmet genererar och på något vis lämnar ut till användaren,
    ##i detta fall utskrift på skärmen av kombinationen platskod-enhetstyp-"senaste nummer".
    ##variabel som används för att hålla/generera utdata: hostnamn
    ##regler:   platskod är text.
        ##      enhetstyp är text.
        ##      senaste nummer är ett heltal.
        ##      bindestrecken hör bara till utskriftsformatet och hanteras inte annat än som mellanrumstecken
        ##      vid själva utskriften.

    ##risker:   användaren blandar stora och små bokstäver vid inmatning.
        ##      användaren skriver siffran med bokstäver.
        ##      användaren skriver med nollan om siffran är under 10 tex 05 vilket inte är ett korrekt angivet heltal.
    ##Planera:
        ##      fråga användaren om platskod
        ##      läs in data från användaren
        ##      fråga användaren om enhetstyp
        ##      läs in data från användaren
        ##      fråga användaren om senast använda nummer
        ##      läs in data från användaren
        ##      kontrollera att platskod är korrekt angiven
            ##      gör texten till gemener 
        ##      kontrollera att enhetstyp är korrekt angiven
            ##      gör texten till gemener
        ##      börja sätt ihop hostnamn som en textsträng innehållande platskod-enhetstyp-
        ##      kontrollera att nummret är korrekt angivet 
            ##      om numret+1 är högre än 99
                ##      skriv felmeddelande "värdet för högt"
            ##      om numret+1 är under 10
                ##      lägg till en nolla innan siffran i hostnamn utan mellanrum till siffran
                ##      skriv ut nästa hostnamn+1
                
            ##      annars 
                        ##      skriv ut nästa hostnamn+1
        ##säj adjö


    ##felmeddelandet:
    ## här vill jag ha max 2 st siffror och om värdet är under 10 vill jag endast ha en siffra:3
    ##Traceback (most recent call last):
    ##  File "/home/delta/Pictures/LabbProgtrammeringskursen/Programmering/Labb1/Problem1.py", line 18, in <module>
    ##    if(lastnumber+1 > 99):
    ##       ~~~~~~~~~~^~
    ##TypeError: can only concatenate str (not "int") to str

    ##eftersom lastnumber fortfarande är/var en textsträng så går det inte att lägga till heltalet 1 då de är olika typer.

    ##Platskod  Typ Senaste nr  Förväntat           Faktiskt    OK?
    ##STO       srv     7       sto-srv-08
    ##gbg       SW      11      gbg-sw-12
    ##sto       srv     0       sto-srv-01
    ##mal       pc      99      "numret är för högt"
    ##sto       srv     sju     crash typfel

##Problem 2
##Problem 3
##Del 4: Från källkod till körning
