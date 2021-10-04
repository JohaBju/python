class Bilmodell:
    
    def __init__(self, modellnavn):
        self._modellnavn = modellnavn
        self._antallSolgteModell = 0

    def modell(self):
        return self._modellnavn

    def oppdaterSalgModell(self, salg):
        self._antallSolgteModell += int(salg)

    def visAntallSalgModell(self):
        return self._antallSolgteModell