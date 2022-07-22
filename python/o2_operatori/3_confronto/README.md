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
"ciao" != "CIAO" # True

## Concatenazione

Possono anche essere concatenati, "come in notazione matematica standard":

```python
0 <= 0.1 <=1  # True
```

Attenzione però che vale la stessa regola delle catene di `and` esplicite, cioè non per forza 


## Overload
li possiamo definire noi per le classi che creiamo, implementando i metodi speciali `__eq__()`, `__gt__()`...


