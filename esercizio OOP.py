class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def __str__(self):
        return f"{self.nome} {self.cognome}"

avvocato = Persona("Ilario", "Ciocia")
figlio1 = Persona("Hekuran","Osma")
figlio2 = Persona("Pascal","Tufariello")
insegnante = Persona("Fabio","Marchitelli")
print(avvocato)

















