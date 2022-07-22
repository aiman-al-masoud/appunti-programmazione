# Warlus (Tricheco)

Questo buffo soprannome deriva dalla forma dell'operatore `:=` che rammenta gli occhi e zanne di un trichecho sdraiato.

L'operatore "tricheco" (presente a partire da Python 3.8) serve ad assegnare valori all'interno di espressioni.

Con l'assegnamento normale, questo è un errore:

```python
s = "ciao "+(x = 'a te')+" mondo"
```

Col tricheco, funziona:

```python
s = "ciao "+(x := 'a te')+" mondo"
s # 'ciao a te mondo'
x # 'a te'
```



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

