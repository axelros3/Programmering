## Labb2 - svar

##  del 1
    ##  planering Nivå 1:
        ##  indata: svarstid
        ##  utdata: bedömning
        ##  regler: svarstid får inte vara negativt (under noll)
            ##      500

        ##  pseudokod:
            ##  definiera funktionen timeJudge(svarstid)
                ##  om svarstid < 0 
                    ##  return "Ogiltigt värde"
                ##  annars om svarstid >= 500
                    ##  return "ingen användbar kontakt"
                ##  annars om svarstid >= 150  
                    ##  return "långsam"
                ##  annars om svarstid >= 50
                    ##  return "bra"
                ##  return "Utmärkt"
            
            ##  läs in svarstiden
            ##  skriv ut bedömningen av svarstiden med hjälp av timejudge()

    ##  testfallstabell Nivå 1
        ##  Svarstid    Förväntat               Faktiskt    OK?
        ##  12          Utmärkt                 Utmärkt
        ##  49          Utmärkt                 Utmärkt
        ##  50          Bra                     Bra
        ##  149         Bra                     Bra
        ##  150         Långsam                 Långsam
        ##  500         Ingen användbar kontakt Ingen användbar kontakt
        ##  -3          Ogiltigt värde          Ogiltigt Värde

    ##  planering Nivå 2:
        ##  indata: gissning
        ##  konstant: HEMLIG_PORT = 443, MAX_ANTAL_GISSNINGAR = 10
        ##  utdata: större mindre eller korrekt som en retursträng

    ##  pseudokod:
        ##definiera funktion myValueCheck(gissning)
            ##  om gissning > HEMLIG_PORT
                ##  return "För högt"
            ##  annars om gissning <HEMLIG_PORT
                ##  return "För lågt"
            return "Korrekt"
        
        myGuessedCorrect = false
        myNRofGuesees = 0
        ##  så länge antalet gissningar < MAX_ANTAL_GISSNINGAR OCH myGuessedCorrect == false
            ##  läs in gissning
            ##  myNrofGuesses incremetera med 1
            ##  response = myValueCheck(gissning)
            ##  om reponse == "Korrekt"
                ##  skriv ut "du har gissat rätt!! du har använt mynrofguesseseseseseesese försök"
                ##  myGuessedeCorrect =true
            ##  annars
                ##  skriv ut response
        ##  om myGuessedCorect == False
            ##  skriv ut "Rätt svar skall vara: HEMLIG_PORT
            
    ##  fråga: Binär sökning, dela alltid kvarvarande intervall på hälften. den fungerad dock bara på 
    ##  sorterade datamängder (listor och liknande)

    ##  Planering Nivå 3:
    ##  def minSumma(lista)
        ##mysum = 0
        ##  för varje element i lista
            ##  mysum += element
        ##  returnera mysum
    
    ##  def mittMedel(lista)
        ##  returnera (minSumma(lista)/längden av lista)

    ##  minStorsta(lista)
        ##  currentBiggest = 0
        ##  för varje element i lista
            ##  if(element > currentbiggest)
                ##  currentBigest = element
        return currentbiggest
    
    ##  varför är tidigare funktionsnamn på svenska....min hjärna är dum..
    ##  myNumbersAbove(lista,minimumLimit)
        ##  nrAboveLimit = 0
        ##  för varje element i lista
            ##  om element > minimumLimit
                ##  nrAboveLimit += 1
        return nrAboveLimit

    ##  nrofFailedLogins = listan från uppgiften...
    ##  skriv ut summan och jämför med pythons inbyggda funktion
    ##  skriv ut medelvärdet och jämför ....
    ##  skriv ut största värdet och jämför .....
    ##  skriv ut antalet på eller över given gräns och jämför...


    ##  fråga 2:
        ##  det tyder på att någon som inte har koll på lösenordet försöker ta sig in, behöver ju inte vara
        ##  fel person så det skall ses som intrångsförsök men det är ju mest troligt att det är det.


##  del 2:  Feltabell
    ##  Nr  Rad Feltyp              Hur hittade du felet?       Vad var fel?                                    Hur rättade du det?                     Hur kan felet förebyggas?
    ##  1   ?   ?                   det gjorde jag inte         ?                                               har antagligen rättat det under rättningen efter inkopieringen som inte hade någon indentering alls.
    ##  2   6   : tecken saknas     def utan : är syntaxfel     : tecken saknades vid funktiondefiniering       lade till :                             tänka på att alla funktioner avslutar "huvudet" med : i python. inklusive if, elif, while etc.
    ##  3   22  fel datatyp         exekveringsfel              kan inte addera ett värde till en textsträng    konverterar värdet till en tesxtsträng  kunskap & erfarenhet... hade även kunnat byta + mot , så max(...) hade hanterats som ny variabel till print-funktionen
    ##  4   23  index out of range  exekveringsfel              index 4 hamnar räknaren utanför listan          använder längden på listan -1           arbeta in det som rutin att alltid använda längden på listan istället för fasta värden
    ##  5   9   logiskt             utskrift gav fel antal      gränsvärdet räknades inte med                   ändrade > till >=                       var tydlig med vad som skall inkluderas i intervall
    ##  6   15  logiskt             utskrift gav fel medelvärde loopen startade inte på noll                    ändrade i range så första värdet är 0   kunskap & erfarehet....

##  del 3:  Debuggern
    ##  programmet debug.py bör skriva ut:
    ##  Misslyckade totalt: 9
    ##  Timmar med larm: 2

    ##  När programmet pausar   antal   misslyckade timmar_med_larm
    ##  Rad 5, varv 1           3       0           0
    ##  Rad 5, varv 2           0       3           1
    ##  Rad 5, varv 3           5       3           1
    ##  Rad 5, varv 4           1       8           2
    ##  Rad 8, efter loopen     1       9           2

    ##  svar på frågor

    ##  1:  utskrift från programmet
    ##  Misslyckade totalt: 9
    ##  Timmar med larm: 2
    ##  stämmer med min "gissning"

    ##  2:  för att den variabeln bara räknas upp om antal är 3 eller större för varje enskilt varv

    ##  3:  antal har värdet 1 pga att sista varvet i loopen så sattes antal till 1 och då python är
    ##  annurlunda mot många andra språk så finns variabeln kvar, hade det varit tex C# så hade
    ##  variabeln antal upphört att existera när vi lämnar loopen. men python har bara globala
    ##  variabler så även om man deklarerar en variabel i en loop så kan man sedan utanför loopen
    ##  använda variabeln...

    ##  4:  med hjälp av debugger kan man se vad värdena på variablerna är vid specifika tillfällen
    ##  och därmed se om de är som förväntat och kan då också visa resultat av jämförelser
    ##  i if satsernas vilkor.


##  del 4:  Refaktorering
    ##  aha... kom på varför det blev fel med citat tecknen förut.... jag kopierade från googles preview
    ## inte från dokumentet i sig...

    ##  utskrift från rorig
    ##  tot 1055
    ##  snitt 211.0
    ##  hog 2

    ##  frågor
    ##  1: jag skrev en funktion för varje uträkning, jag minskade därmed antalet variabler vi behöver i
    ##  "huvudprogrammet" till en enda som vi har för våra tider. blir lite upprepning men varje funktion
    ##  utför en specifik uppgift istället för att göra både totalsummans uträkning och medelvärdet
    ##  och hur många svarstider som är långa samtidigt, vilket lätt blir rörigt även om det kan anses
    ##  vara tidseffektift.

    ##  sedan har jag förklarande utskrifter så att den som kör/läser inte behöver ha sett koden för att förstå.

    ##  2: jag flyttade egentligen bara den kod som redan fanns till respektive funktion, sedan behöver man
    ##  naturligtvis anpassa sig efter den nya verkligheten med funktioner, men själva beräkningarna ser ut
    ##  på samma sätt minus det som inte längre är av intresse för den enskilda uppgiften.

    ##  3: om man inte använder "läsbar kod" eller ännu värre flera olika namnstandarder samtidigt
    ##  så blir det svårare att utläsa vad koden gör. vilket leder till att det blir ännu svårare att
    ##  underhålla och felsöka koden.


##  Utmaningar
    ##  utmaning 4:
        ##  fråga: varför är det bättre att använda konstanten?
        ##  skulle man ändra värdet för gränsen dvs konstanten GRANS, så slipper man nu byta i textstängen också