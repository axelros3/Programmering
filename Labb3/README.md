# Lab 3 – [namnet på ditt program]
    ##  Gjort av: Axel Roselius (i sammarbete med mig själv då min stationära dator är uppsatt för att fungera med mitt privata githubkonto via visual studio)
## Del 1: Projektbeskrivning

    




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
                    ##  anropa passwordController

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
## Del 5: Förbättringar och reflektion