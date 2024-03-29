class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno di pubblicazione: {self.anno_pubblicazione}"


class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.collezione_libri = []

    def aggiungi_libro(self, libro):
        self.collezione_libri.append(libro)

    def rimuovi_libro(self, titolo):
        for libro in self.collezione_libri:
            if libro.titolo == titolo:
                self.collezione_libri.remove(libro)
                return f"Il libro '{titolo}' è stato rimosso dalla collezione."
        return f"Il libro '{titolo}' non è presente nella collezione."

    def cerca_libro(self, criterio, valore):
        risultati = []
        if criterio == 'titolo':
            risultati = [libro for libro in self.collezione_libri if valore.lower() in libro.titolo.lower()]
        elif criterio == 'autore':
            risultati = [libro for libro in self.collezione_libri if valore.lower() in libro.autore.lower()]
        elif criterio == 'anno':
            risultati = [libro for libro in self.collezione_libri if valore == libro.anno_pubblicazione]
        return risultati

    def ordina_libri(self, criterio):
        if criterio == 'titolo':
            self.collezione_libri.sort(key=lambda libro: libro.titolo)
        elif criterio == 'autore':
            self.collezione_libri.sort(key=lambda libro: libro.autore)
        elif criterio == 'anno':
            self.collezione_libri.sort(key=lambda libro: libro.anno_pubblicazione)

#key=lambda viene utilizzato per definire una funzione sort personalizzata in base al criterio selezionato
    def mostra_collezione(self):
        if self.collezione_libri:
            for libro in self.collezione_libri:
                print(libro)
        else:
            print("La tua collezione è vuota.")


# Esempio di utilizzo
#utente1 = Utente("Mario")
#libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980)
#libro2 = Libro("Harry Potter e la pietra filosofale", "J.K. Rowling", 1997)
#libro3 = Libro("1984", "George Orwell", 1949)

#utente1.aggiungi_libro(libro1)
#utente1.aggiungi_libro(libro2)
#utente1.aggiungi_libro(libro3)

#utente1.mostra_collezione()

#print("\nRicerca per autore 'Rowling':")
#risultati_ricerca = utente1.cerca_libro('autore', 'Rowling')
#for libro in risultati_ricerca:
#    print(libro)

#print("\nOrdinamento per titolo:")
#utente1.ordina_libri('titolo')
#utente1.mostra_collezione()
