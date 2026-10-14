Labb1 - Planering

##Problem 1     ############################################################################################33
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

    ##Platskod  Typ Senaste nr  Förväntat               Faktiskt                                                    OK?
    ##STO       srv     7       sto-srv-08              sto-srv-08                                                  ja
    ##gbg       SW      11      gbg-sw-12               gbg-sw-12                                                   ja
    ##sto       srv     0       sto-srv-01              sto-srv-01                                                  ja
    ##mal       pc      99      "numret är för högt"    "numret är för högt"                                        ja
    ##sto       srv     sju     crash typfel            ValueError: invalid literal for int() with base 10: 'sju'   nej

    ## I 4:e testfallet överstiger "lastnumber+1" max antal enheter som kan hanteras med 2 siffror. för att kunna använda fler
    ## enheter med samma namnstruktur så behöver man utöka antalet siffror som tillåts till 3 vilket skulle ge oss 999 st 
    ## vi skulle då kunna få sto-pc-999
    ## testfall 5 går fel redan vid inmatningen då programmet förväntar sig en text som går att göra om till en siffra men
    ## får en text som inte går att konvertera till ett heltal.


##Problem 2     ##############################################################################################################
    ## börjar med länk till draw.io: https://drive.google.com/file/d/1JFZeRwgHmbvdcMg6pSXdvhfwDE_XsQB9/view?usp=sharing
    ##indata: myFileSize och myBandWidth.
    ##utdata: utskrift på skärmen av beräkningen mtTime = (myFileSize * 1000 *8 ) / (myBandWidth)
    ##variabel som används för att hålla/generera utdata: myTime
    ##regler:   myFileSize är ett flyttal.
        ##      myBandWidth är et heltal.
        ##      myTime är ett heltal (som håller reda på antalet sekunder).
        

    ##risker:   användaren skriver negativa siffror
        ##      användaren skriver siffror med bokstäver.
        ##      användaren skriver med flyttal där det skall vara heltal, och tvärtom.
        ##      användaren skriver fel så att division försöker utföras med noll

    ##förstå-frågor:
        ##  filstorlek kan, rent av skall, vara ett flyttal, då storleken anges i GB så en fil på en halv GB skrivs då som 0.5 GB
        ##  och en fil på 3/4 GB som 0.7 GB (kanske 0.75 GB beroende på hur många decimaler som används...)
        ##  att myFileSize multpliceras med 8 beror på att storleken är i bytes, och varje byte är 8 bitar,
        ##  och multiplicationen med 1000 är för att vi kommer mata in storleken som GB men i beräkningen vill vi ha Bytes
        ##  som i sin tur blir multiplicerat med 8 för att få bitar så att filstorleken och bandbredden är på samma enhet.
        ##  1 GB -> 1 * 1000 * 8 = 8 000 Mbit
        ##  100 MBit/s
        ##  8000 / 100 = 80 sekunder
    ##Planera:

    ##tester
    ##  Storlek (GB)    Bandbredd(Mbit/s)   Förväntat (s)       Förväntat(min)  Faktiskt         OK?
    ##  1               100                 80.0                1.33            1min 20sek
    ##  4.5             250                 144.0               2.4             2min 24sek
    ##  50              1000                400.0               6.67            6min 40sek
    ##  0.5             1000                4.0                 0.07            4sek
    ##  1               0                   division med noll   ininity         ZeroDivisionError: division by zero

    ##  det sista testet ger ett zeroDivisionError pga att vi i detta fallet försöker dela med noll.
    ##  orsak till att det tar längr tid än beräknat, dels att värdena inte är exakt då vi här beräknar en kbyte som 1000 istället för 1024 som
    ##  det egentligen är. men också för att annan trafik och störningar på nätverket, för att inte tala om overhead hanteringen, gör att det
    ##  tar längre tid än vad en sån här beräkning kan ge (därav att jag skriver ut "ca"). 

##Problem 3     ######################################################################################################333
    ##  indata:     prefix, antal använda
    ##  utdata:     antal-totalt/användbara/lediga 
    ##  variabler:  myPrefix,incomingUsedNr, myBits, myTotalNr, myUsableNr, myAvailableNr

    ##  läs in myPrefix.
    ##  läs in incomingUsedNr.
    ##  beräkna hur många bitar som används till host, myBits=32-myPrefix.
    ##  beräkna hur många adresser det ger, myTotalNr = 2**myBits.
    ##  beräkna hur många som är användbara, myUsableNr = myTotalNr - 2.
    ##  beräkna hur många som är lediga, myUsableNr-incomingUsedNr.
    ##  beräkna om det får plats en enhet till.

    ##tesfall
    ##  Test    Prefix  Enheter Förväntat totalt    Förväntat användbara    Förväntat lediga    Faktiskt OK?
    ##  1       24      180     256                 254                     74
    ##  2       26      50      64                  62                      12
    ##  3       30      2       4                   2                       0
    ##  4       16      1000    65536               65534                   64534
    ##  5       27      40      32                  30                      ?
    ##  6       33      0       ?                   ?                       ?

##Del 4: Från källkod till körning
