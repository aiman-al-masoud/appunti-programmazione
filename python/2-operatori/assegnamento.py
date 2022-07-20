
# ASSEGNAMENTO
y = x = "ciao mondo"


# WARLUS (TRICHECO)
# assegnamento di valori all'interno di espressioni.

# errore
# "ciao "+(x = 10)+" mondo"

"ciao "+(x := 10)+" mondo" # va bene

# if x = 0: # errore
    # print("capra")

if x := 0: #non esegue. Assegno 0 a x e ritorno 0, 0 falsy. 
    print("capra")

x = 11
def countdown():
    global x
    x -= 1
    return x

while x := countdown():
    print(x)




import sys
print(sys.version)