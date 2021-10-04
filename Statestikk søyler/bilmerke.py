class Bilmerke:

    def __init__(self, merkenavn):
        self._merkenavn = merkenavn
        self._modeller = []
        self._antallSolgteMerke = 0
    
    def oppdaterSalgMerke(self, salg):
        self._antallSolgteMerke += int(salg)

    def visAntallSalgMerke(self):
        return self._antallSolgteMerke

    def faaAlleModeller(self):
        return self._modeller

    def merke(self):
        return self._merkenavn

    def leggTilModell(self, nyModell):
        self._modeller.append(nyModell)

    def visAlleModeller(self):
        modellNavn = []
        for i in self._modeller:
            navn = i.modell()
            modellNavn.append(navn)

        return modellNavn
    