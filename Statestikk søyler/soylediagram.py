#import os

class Soylediagram:

    def __init__(self, soylenavn, sumTotal, navnPaaSoyle, sumPerSoyle):
        self._navn = soylenavn #Navnet paa soylen (str)
        self._sumTotal = sumTotal #Total sum paa alt som skal vises (int)
        self._navnPaaSoyle = navnPaaSoyle #Navnet paa hver enkelt soyle / antall soyler som skal vises (list)
        self._sumPerSoyle = sumPerSoyle #Summen til hver enkelt soyle. Maa vaere koblet med _navnPaaSoyle (list)
    
    def tegnSoyle(self):
        print("\n {0}".format(self._navn.upper()))
        
        for i in range(len(self._navnPaaSoyle)):
            prosentandel = (float(self._sumPerSoyle[i])/float(self._sumTotal))*100
            if round(prosentandel > 0):
                soyle = ("█" * int(round(prosentandel))) #Soylen tegnet
                print("\n {0:15s} {1:4.100s} {2}% / {3}".format(self._navnPaaSoyle[i], soyle, round(prosentandel), self._sumPerSoyle[i]))
        print(" Totalt: {0}".format(self._sumTotal))