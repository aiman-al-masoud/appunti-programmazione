# ASSEGNAMENTO

a = 1 + 1 
y = x = "ciao mondo"


# WARLUS (TRICHECO)
# assegnamento di valori all'interno di espressioni.
# (a partire da Python 3.8)

# errore:
# "ciao "+(x = 10)+" mondo"

"ciao "+(x := 10)+" mondo" # va bene

# if x = 0: # errore
    # print("ciao")

if x := 0: #non esegue. Assegno 0 a x e ritorno 0, 0 falsy. 
    print("ciao")

# utile per while loop dove x è sia condizione fine,
# sia letta nel corpo del loop.
x = 11
def countdown():
    global x
    x -= 1
    return x

while x := countdown(): # si ferma quando x è falsy
    print(x)

