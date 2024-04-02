import json
from datetime import datetime, timedelta
class Alimento:
        def __init__(self, nome, calorie, proteine, carboidrati, grassi):
        self.nome = nome
        self.calorie = calorie
        self.proteine = proteine
        self.carboidrati = carboidrati
        self.grassi = grassi
class Pasto:
    def __init__(self):
        self.alimenti = []

    def aggiungi_alimento(self, alimento):
        self.alimenti.append(alimento)

    def totale_calorie(self):
        return sum(alimento.calorie for alimento in self.alimenti)
class Diario:
    def __init__(self):
        self.diario = {}

    def aggiungi_pasto(self, data, pasto):
        if data not in self.diario:
            self.diario[data] = []
        self.diario[data].append(pasto)

    def totale_calorie_giornaliere(self, data):
        if data in self.diario:
            return sum(pasto.totale_calorie() for pasto in self.diario[data])
        return 0

    def riassunto_settimanale(self):
        oggi = datetime.now()
        inizio_settimana = oggi - timedelta(days=oggi.weekday())
        fine_settimana = inizio_settimana + timedelta(days=6)
        riassunto = {}
        for i in range(7):
            data = inizio_settimana + timedelta(days=i)
            data_str = data.strftime('%Y-%m-%d')
            riassunto[data_str] = self.totale_calorie_giornaliere(data_str)
        return riassunto

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.diario, f, default=lambda x: x.to_dict(), indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.diario = json.load(f)

def main():
    diario = Diario()

    # Caricamento dei dati dal file JSON se esiste
    try:
        diario.load_from_file('diario_alimentare.json')
    except FileNotFoundError:
        pass

    while True:
        print("\n1. Aggiungi pasto")
        print("2. Visualizza totale calorie giornaliere")
        print("3. Visualizza riassunto settimanale")
        print("4. Esci")

        scelta = input("Scelta: ")

        if scelta == '1':
            nome_past = input("Inserisci il nome del pasto: ")
            pasto = Pasto(nome_past)
            while True:
                nome_alimento = input("Inserisci il nome dell'alimento (o 'fine' per terminare): ")
                if nome_alimento.lower() == 'fine':
                    break
                calorie = float(input("Inserisci le calorie: "))
                proteine = float(input("Inserisci le proteine: "))
                carboidrati = float(input("Inserisci i carboidrati: "))
                grassi = float(input("Inserisci i grassi: "))
                alimento = Alimento(nome_alimento, calorie, proteine, carboidrati, grassi)
                pasto.aggiungi_alimento(alimento)
            data = input("Inserisci la data del pasto (YYYY-MM-DD): ")
            diario.aggiungi_pasto(data, pasto)
            diario.save_to_file('diario_alimentare.json')
            print("Pasto aggiunto con successo!")
        elif scelta == '2':
            data = input("Inserisci la data (YYYY-MM-DD): ")
            print(f"Totale calorie giornaliere per il {data}: {diario.totale_calorie_giornaliere(data)}")
        elif scelta == '3':
            print("Riassunto settimanale delle calorie giornaliere:")
            riassunto_settimana = diario.riassunto_settimanale()
            for data, totale_calorie in riassunto_settimana.items():
                print(f"{data}: {totale_calorie}")
        elif scelta == '4':
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()

