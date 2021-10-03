from spillbrett import Spillbrett
    
def hovedprogram():
    #Bruker kan bestemme størrelse på brettet
    brettStorrelse = input("Hvor mange stort skal brettet være? (eks: '10 10' gir et brett på 10x10 ruter) ").split()

    #Gjør tester for at brukerinput er logisk (todimensjonalt brett / mindre enn 30 * 30-brett)
    if len(brettStorrelse) > 2 or int(brettStorrelse[0]) > 30 and int(brettStorrelse[1]) > 30 or int(brettStorrelse[0]) < 3 or int(brettStorrelse[1]) < 3:
        print("Ugyldig input")
    
    else:
        #Dersom brukerinput er lovlig lages et nytt brett
        nyttSpill = Spillbrett(brettStorrelse[0], brettStorrelse[1])

        nesteGen = True
    
        #Sjekker videre dirigering av bruker (q for å avslutte / enter for å fortsette)
        while nesteGen:
            
            #Tegner opp brettet
            nyttSpill.tegnBrett()
            #Får inn brukerinput
            nyGen = input("\nTrykk 'Enter' å gå til neste generasjon eller 'Q' for å avslutte ").lower()

            #Avslutter programmet dersom bruker taster inn 'q' eller alle cellene er døde
            if nyGen == "q" or nyttSpill.antallLevendeCeller() == 0:
                print("Program avsluttes...")
                nesteGen = False
            else:
                nyttSpill.oppdatering()


hovedprogram()