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

