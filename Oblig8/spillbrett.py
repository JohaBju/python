from random import randint
from celle import Celle
import os

class Spillbrett:

    def __init__(self, r, k):
        #Generasjon, starter på 0
        self._gen = 0

        #Antall kolonner og rader
        self._rader = int(r)
        self._kolonner = int(k)
        #Lager spillbrettet
        self._brett = []

        #Legger inn celler på spillbrettet
        for rad in range(0, self._rader):
            self._brett.append([])

            for kolonne in range(0, self._kolonner):
                self._brett[rad].append(Celle())

        #Kaller metoden
        self._generer()


    def tegnBrett(self):
        #Renser terminalen før den tegner på nytt
        rensTerminal()

        #Gir informasjon på skjermen utifra status på cellene
        if self.antallLevendeCeller() == 0:
            print("\nAlle cellene er nå døde. Brettet overlevde til generasjon {0}.\n".format(self._gen))
        else:
            print("\nGenerasjon: {0} // Levende celler: {1}\n".format(self._gen, self.antallLevendeCeller()))

        #Løser opp den nøstete listen
        for i in self._brett: 
            for j in i:
                #Printer hver linje 
                print("".join(j.visuellRep()), sep="", end=" ")
            
            print()


    def _generer(self):
        #Tilfeldige tall-variabler, kan enkelt endres for å endre sannsynligheten i spillet
        tall1 = 0
        tall2 = 2

        #Kjører igjennom for alle celler 
        for rad in self._brett:
            for kolonne in rad:

                #Lager et tilfeldig tall
                tilfTall = randint(tall1, tall2)
                
                #Setter cellen levende utefra tilfeldig tall
                if tilfTall < 1:
                    kolonne.settLevende()
                
        
    def finnNaboer(self, rad, kolonne):
        #Oppretter en lokal liste som tar vare på kordinatene til nabocellene
        naboliste = []

        #Sjekker alle celler rundt om en celle
        for rader in range(-1, 2):
            for kol in range(-1, 2):
                naboRad = rad + rader
                naboKolonne = kolonne + kol
                
                #Bool-test som sjekker at 
                gyldig = False

                #Gjør diverse tester som sørger for at naboen ikke er utenfor spillbrettet
                if not (kol == 0 and rader == 0):
                    if not (naboKolonne < 0 or naboRad < 0):
                        if not(naboRad > self._rader-1 or naboKolonne > self._kolonner-1):
                            gyldig = True

                #Legger til kordinatene til naboer som er gyldige
                if gyldig:
                    naboliste.append(self._brett[naboRad][naboKolonne])
        
        #Test for å sjekke at alle objektene har riktig antall naboer
        #print(len(naboliste))

        #Returnerer nabolisten
        return naboliste


    def oppdatering(self):
        #Oppretter en liste som holder på døde og levende celler (objektadressen)
        dodeCeller = []
        levendeCeller = []

        #Går igjennom spillbrettet
        for rad in self._brett:
            for kolonne in rad:
                levendeNabo = 0

                #Får en liste med naboer for alle objektene på brettet, en celle om gangen
                for nabo in self.finnNaboer(self._brett.index(rad), rad.index(kolonne)):
                    if nabo.erLevende():
                        levendeNabo += 1
                if kolonne.erLevende():
                    #Sjekker alle naboene rundt
                    if levendeNabo < 2 or levendeNabo > 3:
                        dodeCeller.append(kolonne)
                else:    
                    if levendeNabo == 3:
                        levendeCeller.append(kolonne)
        
        #Til slutt oppdateres statusene til alle cellene 
        for celler in dodeCeller:
            celler.settDoed()
        for celler in levendeCeller:
            celler.settLevende()

        #Legger til slutt til at det er en ny generasjon
        self._gen += 1


    #Metode for å sjekke antall levende celler som er igjen på brettet
    def antallLevendeCeller(self):
        antCeller = 0
        #Går igjennom brettet (nøstet liste)
        for rad in self._brett:
            for celler in rad:
                #Legger til 1 dersom cellens metode returnerer True
                if celler.erLevende():
                    antCeller += 1
        #Returnerer verdien
        return antCeller



#Lager en funksjon for å rense terminalen mellom hver gang spillbrettet printes ut
def rensTerminal():
    #Sjekker operativsystem (Funker for Linux og Windows)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')