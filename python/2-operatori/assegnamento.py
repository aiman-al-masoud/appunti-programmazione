y = x = "ciao mondo"


# if x = 0: # errore
    # print("capra")


if x := 0: #non va mai. Assegno 0 a x e ritorno 0, 0 falsy. 
    print("capra")

x = 11
def countdown():
    global x
    x -= 1
    return x

while x := countdown():
    print(x)