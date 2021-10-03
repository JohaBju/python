'''
Oppgave 5: Egen oppgave. Program som henter inn data om kvadratmeterpris fra ulike steder i landet
'''

#Programmet henter inn tekstfilen 
kvdFil = open("kvadratpris.txt", "r")

#Lager en liste med byer, pris og utvikling i %
kvdList = {}

#Henter inn data fra filen og legger det i en ordbok
for linjer in kvdFil:
    (nokkel, verd1, verd2) = linjer.split()
    
    #Legger inn byen som nokkel og verdi en som kvmpris og verdi to som prosent
    kvdList[str(nokkel)] = [int(verd1), float(verd2)]

print(kvdList)

#Lager en prosedyre som er hovedprogram
def hovedprogram():

    #Lager en liten meny
    print (lin)
    print ("      H O V E D   M E N Y      \n\n Skriv inn folgende bokstav:\n\n L. Oversikt over alle steder i database\n S. Velge sted du onsker mer informasjon om\n B. Aapne boligkalkulatoren\n A. Avslutte programmet")
    #Henter inn et svar om hvor bruker vil hen
    direktBrukerInp = input("\n Svar:  ").lower()
    print(lin)

    #Sjekker svar
    #Sender bruker til byoversikt
    if direktBrukerInp == "l":
        print(" Overfores til oversikt...")
        print(utskriftDictFunk())
        hovedprogram()
    #Sender bruker til byvalg
    elif direktBrukerInp == "s":
        sjekkSvarFunk()
    #Sender bruker til boligkalkulatoren
    elif direktBrukerInp == "b":
        boligKalkFunk()
    #Avslutter program
    elif direktBrukerInp == "a":
        print(avslSet)

    else:
        print(ugyldigSvarFunk(direktBrukerInp))
        hovedprogram()
    
    

#Prosedyre for aa skrive ut liste over byer
def utskriftDictFunk():

    #Printer ut en liste til bruker
    for byer in kvdList:
        byliste = " Liste over byer i database: " + ", ".join(kvdList)
    
    return byliste



#Prosedyre som gir svar til bruker
def sjekkSvarFunk():

    brukerInp = input("\n Skriv inn hvilket sted du onsker aa se statistikk over: ")

    #Sjekker om brukers svar ligger i ordboken
    if brukerInp in kvdList.keys():
        print(lin + "    \n {0}\n\n Gjennomsnittspris per kvm: {1},-\n Okning sist aar: {2}%".format(brukerInp.upper(), kvdList[brukerInp][0], kvdList[brukerInp][1]))
        hovedprogram()
        
    #Gir en feilkode dersom svar ikke gjor det
    else:
        boolTestInp = input(" '{0}' ligger ikke i listen. Vil du faa en oversikt over stedene som ligger i programmet? (ja/nei): ".format(brukerInp)).lower()
        
        if boolTestInp == "ja":
            print(utskriftDictFunk())
            sjekkSvarFunk()

        elif boolTestInp == "nei":
            byValgInp = input("\n Skriv inn hvilket sted du onsker aa se statistikk over: ")
            sjekkSvarFunk()

        else:
            hovedprogram()



#Boligkalkulator##Boligkalkulator##Boligkalkulator##Boligkalkulator##Boligkalkulator#



#Boligkalkulator
def boligKalkFunk():
    print(lin)
    print("\n     B O L I G K A L K U L A T O R\n\n Skriv inn folgende bokstav:\n R. Regn ut hvor mye en eiendom vil koste\n K. Sjekk om du har nok egenkapital\n H. Hovedmeny\n A. Avslutt")

    #Sjekker hvor bruker skal videresendes
    brukerInp = input("\n Svar: ").lower()

    if brukerInp == "r":
        kostnadEiendom()
    elif brukerInp == "k":
        egenKapitalFunk()
    elif brukerInp == "h":
        hovedprogram()
    elif brukerInp == "a":
        avslSet
    else:
        print(ugyldigSvarFunk(brukerInp))
        boligKalkFunk()

    #boligKalkDirectFunk(brukerInp)



#Kostnadsutregning utifra beliggehet 
def kostnadEiendom():
    storrelse = int(input(" Hvor mange kvm er eiendommen?: "))

    byValgInp = input(" Hvor ligger eiendommen? ({0})\n Svar: ".format(utskriftDictFunk()))
    if byValgInp in kvdList:

        totPrisUtregn = kvdList[byValgInp][0] * storrelse

        print(lin + "\n Sted:{0}\n BRA:{1}kvm\n Estimert pris:{2},-\n".format(byValgInp.rjust(21, " "), str(storrelse).rjust(20, " ") ,str(totPrisUtregn).rjust(13, " ")) + lin)

        brukerValg = input(" Onsker du aa faa en forventet avkastning av denne eiendommen?(ja/nei)\n Svar: ").lower()

        if brukerValg == "ja":
            avkastningsKalkFunk(totPrisUtregn, byValgInp)

        else:
            boligKalkFunk()

    else:
        print(ugyldigSvarFunk(byValgInp))
        kostnadEiendom()



def egenKapitalFunk():
    #Faar inn egenkapital og eiendomkostnad
    egenKapInp = int(input(" Hva har du i egenkapital?\n Svar: "))
    boligKostInp = int(input(" Hva koster eiendommen du onsker aa kjope?\n Svar: "))

    #Regner ut prosenten bruker har
    egenKapPros = round((egenKapInp / boligKostInp)*100)

    #Sjekker om bruker har nok i egenkapital
    if egenKapPros < 15:

        #Regner min-egenkapital + hvor mye bruker mangler
        egenKapProsMin = round(boligKostInp * 0.15)
        egenKapMangl = (egenKapProsMin - egenKapInp)

        print("\n Din egenkapital er under 15% ({0}%)\n Du mangler {1},-\n Minimum egenkapital er {2},-".format(egenKapPros, egenKapMangl, egenKapProsMin))
        hovedprogram()

    else:
        print("\n Din egenandel er paa {0}%\n Du kan faa laan hos banken til ditt drommested!".format(egenKapPros))
        hovedprogram()



#Avkastningskalkulator
def avkastningsKalkFunk(pris, sted):
    antallAarInp = int(input(" Hvor mange aar forventer du aa eie eiendommen? \n Svar: "))

    #Regner ut prosentendring som en variabel
    prosentendring = 1 + (kvdList[sted][1] / 100)

    #Regner ut totalpris
    totpris = pris * prosentendring ** antallAarInp

    #Regner hvor mye man har vunnet
    verdistigning = totpris - pris

    print(lin + "\n EIENDOM I {0}\n\n Forventet pris etter {1:.0f}aar: {2},-\n Verdistigning i kr: {3:.0f},-\n (Tallene forutsetter fast vekst paa {4}%)".format(sted.upper(), antallAarInp, round(totpris), verdistigning, kvdList[sted][1]))

'''def boligKalkDirectFunk(brukerInp):
    print("Brukersvar " + brukerInp)

    boligKalkDict = {
    "r": kostnadEiendom(),
    "k": egenKapitalFunk(),
    "h": hovedprogram(),
    "a": avslSet(),
    }

    if brukerInp in boligKalkDict:
        return boligKalkDict[brukerInp]'''


#Div variabler i program##Div variabler i program##Div variabler i program##Div variabler i program##Div variabler i program#
avslSet = " Programmet avsluttes..."

#Fellesvariabel for linjer
lin = (43 * '-')

def ugyldigSvarFunk(svar):
    return " Svaret '{0}' er ikke gyldig...\n".format(svar)

#Kaller hovedprogram##Kaller hovedprogram##Kaller hovedprogram##Kaller hovedprogram##Kaller hovedprogram##Kaller hovedprogram#
hovedprogram()