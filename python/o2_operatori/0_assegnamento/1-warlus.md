# Warlus (Tricheco)

Questo buffo nomignolo deriva dalla forma dell'operatore `:=` che rammenta gli occhi e zanne di un trichecho sdraiato (con tanta immaginazione).

L'operatore "tricheco" (presente a partire da Python 3.8) serve ad assegnare valori **all'interno di espressioni**.

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


## Caso d'uso

Utile per while loop dove x è sia condizione di fine, sia letta nel corpo del loop:

```python

x = 11
def countdown():
    global x
    x -= 1
    return x

while x := countdown(): # si ferma quando x è falsy
    print(x, "secondi/o al lancio!")
```

## Attenzione agli if

Attenzione ovviamente a non confondere `=` o `:=`, con `==`.