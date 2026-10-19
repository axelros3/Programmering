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
##  del 3:  Debuggern
##  del 4:  Refaktorering