## Labb2 - svar

##  del 1
    ##  planering
        ##  indata: svarstid
        ##  utdata: bedömning
        ##  regler: svarstid får inte vara negativt (under noll)
            ##      500

        ##pseudokod
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

##  del 2:  Feltabell
    ##  Svarstid    Förväntat               Faktiskt    OK?
    ##  12          Utmärkt                 Utmärkt
    ##  49          Utmärkt                 
    ##  50          Bra                     
    ##  149         Bra                     
    ##  150         Långsam                 
    ##  500         Ingen användbar kontakt 
-3 Ogiltigt värde
##  del 3:  Debuggern
##  del 4:  Refaktorering