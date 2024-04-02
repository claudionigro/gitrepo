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
        

