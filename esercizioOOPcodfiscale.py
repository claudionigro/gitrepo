class Persona:
    def __init__(self, CodiceFiscale, Nome, Cognome):
        self.CodiceFiscale, self.Nome, self.Cognome = CodiceFiscale, Nome, Cognome

    def toString(self):
        return f"Codice Fiscale: {self.CodiceFiscale}, Nome: {self.Nome}, Cognome: {self.Cognome}"

class Studente(Persona):
    def __init__(self, CodiceFiscale, Nome, Cognome, Matricola, Universita):
        super().__init__(CodiceFiscale, Nome, Cognome)
        self.Matricola, self.Universita = Matricola, Universita

    def toString(self):
        return f"{super().toString()}, Matricola: {self.Matricola}, Università: {self.Universita}"

class Docente(Persona):
    def __init__(self, CodiceFiscale, Nome, Cognome, Materia, Salario):
        super().__init__(CodiceFiscale, Nome, Cognome)
        self.Materia, self.Salario = Materia, Salario

    def toString(self):
        return f"{super().toString()}, Materia: {self.Materia}, Salario: {self.Salario}"

class ElencoPersone:
    def __init__(self, max_persons):
        self.max_persons, self.elenco = max_persons, []

    def aggiungi(self, persona):
        self.elenco.append(persona) if len(self.elenco) < self.max_persons else print("L'elenco è pieno.")

    def toString(self):
        return '\n'.join([persona.toString() for persona in self.elenco])

class ProvaListaPersone:
    @staticmethod
    def crea_elenco_persone():
        num_persons = int(input("Inserisci il numero di persone da aggiungere all'elenco: "))
        elenco_persone = ElencoPersone(num_persons)
        for _ in range(num_persons):
            tipo_persona = input("Inserisci il tipo di persona (Persona/Studente/Docente): ").lower()
            if tipo_persona == "persona":
                elenco_persone.aggiungi(Persona(*input_persona()))
            elif tipo_persona == "studente":
                elenco_persone.aggiungi(Studente(*input_persona(), *input_studente()))
            elif tipo_persona == "docente":
                elenco_persone.aggiungi(Docente(*input_persona(), *input_docente()))
            else:
                print("Tipo di persona non valido. Riprova.")
        return elenco_persone

    @staticmethod
    def visualizza_elenco(elenco_persone):
        print(elenco_persone.toString() if elenco_persone else "Nessun elenco di persone.")

def input_persona():
    return input("Codice Fiscale: "), input("Nome: "), input("Cognome: ")

def input_studente():
    return input("Matricola: "), input("Università: ")

def input_docente():
    return input("Materia: "), input("Salario: ")

