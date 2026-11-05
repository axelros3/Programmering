#slutprov - ipregister
    gjort av : Axel Roselius

##  Pseudokod

    ##  meny
        ##  så länge 
            ##  skriv ut meny valen
            ##  läs in heltal 
            ##  matcha heltalet
                fall 0
                    avsluta loopen
                fall 1
                    anropa lägg till enhet
                fall 2
                    anropa visa alla enheter
                fall 3
                    anropa ändra nätverk
            
    ##  lägg till enhet
        ##  läs in enhetens beskrivning
        ##  läs in enhetens tilltänkta IP-adress
        ##  kontrollera om den angivna IP-adressen finns i nätet
            ##  om inte skriv ut felmededlande ligger inte i nätet
        ##  spara enheten i lista (dictionary?)

        
##  Redogörelse
    ##  att jag har en funktion för att byta nätverk beror på min bugg som jag trasslade till det med
    ##  som inte tillät mig att sätta nätverket mer än en gång och då började jag skriv den funktionen
    ##  för att komma runt detta.
    
    ##  jag valde att använda mig utav tupplar då det är ett trevligare sätt att hantera objekt i listor.
    ##  det gjorde att jag inte behövde ha flera listor med enheters beskrivningar och ip-adresser utan
    kan då sammla dem som ett objekt i listan som innehåller både beskrivningen och ip-adressen. 

    ##  att dela upp kod i funktioner gör man för att minimera komplexiteten i ett problem så att man
    ##  bryter ned problematiken så "atomärt" som möjligt så att varje delproblem blir enkelt att lösa
    ##  och detta är för mig ett naturligt tillvägagångssätt som jag själv egentligen inte äns tänker
    ##  på annat än vad mer kan vi bryta ut...

##  AI-logg
    ##  INGET

##  Reflektion

##  Testtabell


