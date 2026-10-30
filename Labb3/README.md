# Lab 3 – MultiSolver
    ##  Gjort av: Axel Roselius (i sammarbete med mig själv då min stationära dator är uppsatt för att
    ##  fungera med mitt privata githubkonto via visual studio)
## Del 1: Projektbeskrivning
    ##  ett program som anropar de olika modulerna från en meny. modulerna utför varsin uppgift som tex att
    ##  kontrollera att service på angiven IP-adress och port är online.
    ##  utifrån en huvudmeny väljer användaren en modul att gå till och där utför användaren sedan den uppgift
    ##  som modulen hjälper/löser.
    ##  de olika modulerna är:
        ##  Service Control
	    ##  Log analyzer
	    ##  Checksum control
	    ##  Subnet Planner
	    ##  Config Generator
	    ##  Password Control

    ##  Service Control:
        ##  kontrollerar om service på angiven IP-adress och port svarar
	##  Log analyzer:
        ##  öppnar en logfil och kontrollerar hur många gånger inloggningsförsök skett och från vilken IP-adress
	##  Checksum control:
        ##  räknar ut hashen för en given fil och kontrollerar mot en angiven hash
	##  Subnet Planner:
        ##  räknar ut om angiven ip-adress till nätverk är korrekt angiven och när nätverket väl är angivet kan
        ##  den kontrollera att en viss ip-adress ingår i det angivna nätverket
	##  Config Generator:
        ##  "räknar" ut vilka kommandon som skall köras på en switch för att konfigurera ett interface som
        ##  accessport för ett angivet VLAN
	##  Password Control
        ##  kontrollerar ett lösenord mot lista med vanliga/blockade ord/innehåll och talar om vad eventuella
        ##  problem är med lösenordet


## Del 2: Pseudokod och flödesschema

    ##  pseudokod 
        ##  "huvudprogram" DeltaStart.py
        ##  sätt en boolean-variabel för att kunna avbryta loop på ett snyggt sätt
        ##  så länge variabeln är sann
            ## "rita" ut menyn
            ##  läs in ett heltal
            ##  switch case sats
                ##  om 0
                    ##  sätt bool-variabel till false för att avsluta loopen
                ##  om 1
                    ##  anropa service control
                ##  om 2
                    ##  anropa log analyzer
                ##  om 3
                    ### anropa checksum control
                ##  om 4
                    ##  anropa subnet planner
                ##  om 5
                    ##  anropa coonfig generator
                ##  om 6
                    ##  anropa password Controller

        ##  visa meny deltastart.py
            skriv ut en "snygg" meny

        ##  läs heltal deltastart.py
            ##  fortsätt i oändlighet
                ##  försök
                    ##  läs in "värde" från användaren och gör om till heltal och spara i variabel
                ##  fånga in fel av typen värdefel (value error)
                    ##  skriv ut felmeddelande om att denvill ha heltal i siffror
                ##  annars
                    ##  om minsta tillåtna är mindre än variabeln och största tillåtna är större än variabeln
                        ##  returnera variabeln
                ##  skriv ut felmeddelande heltalet måste vara inomintervallet minsta till största

        ##  ServiceControl servicecontrol.py
            ##  enlista med servrars IP-adresser
            ##  enlista med portar att kontrollera
            ##  för varje index i intervallet(0-serverlistans längd)
                ##  om anrop till port_svarar ger ett sant värde
                    ##  skriv ut adressen och porten och att den svarar
                ##  annars
                    ##  skriv ut adress och port och att den inte svarar
        ##  port_svarar servicecontrol.py
            ##  försök
                ##  öppna en socket med medskickad värdadress och portnummer
                    ##  returnera sant
                ##  fånga oserror
                    ##  retunera falskt
            ##  returnera falskt om vi ändå kommer hit för snyggare avslut

## Del 4: Användartest
    ##  testfil för checksumman 
        ##  namn: testfil_frameBIOS.bin
        ##  hash: E7A088E2D22015659A49F02660E71E05ECF74BC9B9273F3164B2F5D8311BA397

    ##  respons från testaren:
        ##  inkonsekventa menyer del-meny vs huvud-meny
        ##  byter mellan språk svenska och engelska 
        ##  vissa moduler har dåligt med info till användaren om vad som förväntas i form av indata.
        ##  dåligt med assertions på input
        ##  subnet planner ...
        ##  checkumman behöver mer info och en lista på tillgängliga filer att testa  

## Del 5: Förbättringar och reflektion
    ##  jag har valt att bara laga input hanteringen och att skriva om menyerna
    ##  så samtliga är på svenska, detta mest på grund av tidsbrist.
    ##  jag hade även tänkt redan från början att service kontrollen skall spara
    ##  ip-adresser och portnummer i en fil som sedan skall läsas in vid start
    ##  nästa gång (del)programmet körs, detta har jag dock inte hunnit med ännu.