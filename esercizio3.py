def acquisizioneNomi(numNomi):
    lista = []
    a = numNomi
    for i in range(int(a)):
        nome_utente = input("inserisci il nome da aggiungere:")
        lista.append(nome_utente)
    print(lista)
    return lista

def new_func():
    nome_utente = ""
    return nome_utente

def ricercaNomi(lista):
    risultato = ""
    if nome_utente in lista:
        risultato = nome_utente
        print("il nome utente è stato trovato: ", risultato)
    else: 
        print("il nome utente non è stato trovato")

ntngnùtèp,nènm,



numeroNomi = input("quanti nomi vuoi inserire?")
miaListaNomi = acquisizioneNomi(numeroNomi)

nomeRicerca = input("inserisci il nome da ricercare:")
ricercaNomi(miaListaNomi)

