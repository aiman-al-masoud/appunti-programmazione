# Confronto

Sono operatori di "equivalenza" o confronto "logico" fra oggetti. Ritornano un bool.

* `==`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

```python
3 > 2 # True
```

```python
"ciao mondo" == "ciao "+"mondo"  # True
```

```python
"zorro" > "aereo" # True
"accumulare" > "abbondare" # True
```

## Concatenazione

Possono anche essere concatenati, "come in notazione matematica":

```python
0 <= 0.1 <=1  # True
```

che equivale a:

```python
(0 <= 0.1) and ( 0.1 <= 1)  # True
```

Attenzione però, proprio per via di questa equivalenza, vale il fatto che non per forza si va fino alla fine, se l'esito della catena è già chiaro:

```python
def uno():

    """
    Una funzione che stampa un messaggio e ritorna 1.
    """
    print("La funzione esegue!")
    return 1 
```

### Qui eseguo tutta la catena:

```python
0.2 < 0.5 < uno() # True
```

```
La funzione esegue!
```

### Qui no

è già chiaro che `0.2` non è minore di `0.1` e quindi tutta la disuguaglianza è falsa. La funzione `uno()` non viene nemmeno eseguita.

```python
0.2 < 0.1 < uno() # False
```


## Overload
li possiamo definire noi per le classi che creiamo, implementando i metodi speciali `__eq__()`, `__gt__()`...


