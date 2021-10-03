'''
Klassen for celler
'''
class Celle:
    
    #Definerer konstruktøren (fra start er cellen død)
    def __init__(self):
        self._levende = False

    #Setter cellens status til død
    def settDoed(self):
        self._levende = False

    #Setter cellens status til levende
    def settLevende(self):
        self._levende = True

    #Returnerer statusen til en celle
    def erLevende(self):
        return self._levende

    #Sender tilbake en visuell representasjon av cellene
    def visuellRep(self):
        if self._levende:
            return "O"
        else:
            return "."