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


##  del 3:  Debuggern
##  del 4:  Refaktorering