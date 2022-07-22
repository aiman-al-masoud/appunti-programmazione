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
(0 <= 0.1) and (0.1 <= 1)  # True
```

Attenzione però, proprio per via di questa equivalenza, vale la regola della **pigrizia**; [non si va fino alla fine se l'esito della catena è già chiaro](../../o1_tipi_dati/o5_booleani/2-short-circuiting.md#shortcircuting):

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

### Qui invece no

```python
0.2 < 0.1 < uno() # False
```

è già chiaro che `0.2` non è minore di `0.1` e quindi tutta la disuguaglianza è falsa. La funzione `uno()` non viene nemmeno eseguita.



## Overload
Possiamo definire noi i confronti per le classi che creiamo, implementando i metodi speciali `__eq__()`, `__gt__()`...


