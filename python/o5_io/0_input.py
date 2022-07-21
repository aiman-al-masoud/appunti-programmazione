#
# Ottenere un input testuale dall'utente durante 
# l'esecuzione del programma è molto facile in Python.
#

# il programma va in pausa, finché l'utente non preme invio.
x = input()
print(x)


# si può anche opzionalmente specificare un messaggio
# direttamente nella funzione input()

x = input("Inserisci il tuo nome:\n")
print("ciao", x+"!")

# Nota che il valore di ritorno di input() è sempre
# una stringa! Se ci si aspetta un valore numerico
# dall'utente, bisognerà poi fare il casting esplicito.

