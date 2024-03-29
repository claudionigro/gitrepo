class Veicolo:
    _numeroDiRuote = 0
    _alimentazione = ""
    _larghezza = 0
    _lunghezza = 0
    _peso = 0
    _marca = ""
    _assicurazionePresente = False
    _targaPresente = False
    _codiceTarga = ""

    def __init__(self, numeroDiRuote, alimentazione, larghezza, lunghezza, peso, marca, assicurazionePresente, targaPresente):
        self._numeroDiRuote = numeroDiRuote
        self._alimentazione = alimentazione
        self._larghezza = larghezza
        self._lunghezza = lunghezza
        self._peso = peso
        self._marca = marca
        self._assicurazionePresente = assicurazionePresente
        self._targaPresente = targaPresente

    def updateAlimentazione(self, nuovaAlimentazione):
        self._alimentazione = nuovaAlimentazione
    def updateCodiceTarga(self, nuovoCodiceTarga):
        if self._codiceTarga == True:
            self._codiceTarga = nuovoCodiceTarga
    def stampaLarghezza(self):
        risultatoLarghezza = str(self._larghezza)
        return risultatoLarghezza

mioVeicolo = Veicolo(4,"benzina", 2, 4, 1000, "fiat", True, True)
mioVeicolo.updateAlimentazione("GPL")
mioVeicolo.updateCodiceTarga("ABCD0134")
stampaLarghezza = mioVeicolo.stampaLarghezza()
print(stampaLarghezza)

class Auto(Veicolo):
    _cavalli = 0
    _numeroPosti = 0
    _numeroPorte = 0
    _cilindrata = 0
    _guidaAutonoma = False
    _daLavare = False

    def __init__(self, cavalli, numeroPosti, numeroPorte,cilindrata,guidaAutonoma,daLavare):
        super().__init__(4,"",2, 4, 2000, "bmw", True, True)
        self._cavalli = cavalli
        self._numeroPosti= numeroPosti
        self._numeroPorte = numeroPorte
        self._cilindrata=cilindrata
        self._guidaAutonoma = guidaAutonoma
        self._daLavare = daLavare
    
    def autoDaLavare(self, daLavare):
        self._daLavare = daLavare
    
    def  lavaggioAuto(self):
        if self._daLavare == True:
            print("l'auto è da lavare")
        else:
            print("l'auto è pulitissima")

miaAuto = Auto(75, 5, 5, False, 1000, False)
miaAuto.lavaggioAuto()
miaAuto.autoDaLavare(True)
miaAuto.lavaggioAuto()

miaAuto.updateAlimentazione("GPL")
miaAuto.stampaLarghezza()











