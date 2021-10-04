from soylediagram import Soylediagram
from bilmerke import Bilmerke
from bilmodell import Bilmodell

def leggTilObjekt(filnavn):
    alleMerker = {} #Merker
    objektListe = [] #Objektadresser merker
    totalSalg = 0

    for linjer in open(filnavn):
        (merke, modell, antallSalg) = linjer.strip().split(": ")

        if merke not in alleMerker.keys():
            nyttMerke = Bilmerke(merke) #Lager et nytt objekt i merker
            alleMerker[merke] = nyttMerke
            objektListe.append(nyttMerke)
            nyttMerke.oppdaterSalgMerke(antallSalg) #Oppdaterer salget til merket
        else:
            alleMerker[merke].oppdaterSalgMerke(antallSalg) #Oppdaterer salget til merket dersom merket allerede finnes

        if modell not in nyttMerke.visAlleModeller():
            nyModell = Bilmodell(modell) #Lager et nytt objekt i modeller
            nyttMerke.leggTilModell(nyModell) #Legger til modellen i merket
            nyModell.oppdaterSalgModell(antallSalg) #Oppdaterer salget til modellen
            totalSalg += int(antallSalg)

        else:
            nyModell.oppdaterSalgModell(antallSalg) #Oppdaterer salget til modellen
            totalSalg += int(antallSalg)

    #print(alleMerker, "\n\n", objektListe, "\n\n", totalSalg)

    return objektListe, totalSalg
        

def test():
    objekter = leggTilObjekt("BilsalgOversikt.txt")

    navneListe = []
    soyleVerdi = []

    for i in objekter[0]:
        nyttNavn = i.merke()
        navneListe.append(nyttNavn)
        nyVerdi = i.visAntallSalgMerke()
        soyleVerdi.append(nyVerdi)

    bilSoyleDiagram = Soylediagram("Bilstatestikk", objekter[1], navneListe, soyleVerdi)
    bilSoyleDiagram.tegnSoyle()

    '''
    Bilmodeller
    '''

    modellNavneListe = []
    modellSoyleVerdi = []

    for i in objekter[0]:
        for j in i.faaAlleModeller():
            nyttNavnModell = j.modell()
            modellNavneListe.append(nyttNavnModell)

            nyVerdiModell = j.visAntallSalgModell()
            modellSoyleVerdi.append(nyVerdiModell)

    modellSoyleDiagram = Soylediagram("Bilmodeller", objekter[1], modellNavneListe, modellSoyleVerdi)
    modellSoyleDiagram.tegnSoyle()

test()