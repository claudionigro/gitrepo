class Persona:
    nome=""
    cognome=""
    
    #per convenzione, vi consiglio sempre di mettere la def dell'init
    def __init__(self):
        pass

    def updateNome(self,nuovoNome):
        self.nome = nuovoNome

    def updateCognome(self, nuovoCognome):
        self.cognome = nuovoCognome
    
    def getPersonaInJSON(self):
        return {"nome": self.nome, "cognome": self.cognome}

persona1 = Persona()
persona2 = Persona()

listaDiPersone = []


persona1.updateNome("ilario")
persona1.updateCognome("ciocia")

persona2.updateNome("fabio")
persona2.updateCognome("marchitelli")

listaDiPersone.append(persona1.getPersonaInJSON())
listaDiPersone.append(persona2.getPersonaInJSON())


print(listaDiPersone)






    