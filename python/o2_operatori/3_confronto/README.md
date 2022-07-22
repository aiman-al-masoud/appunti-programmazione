# Confronto

Sono operatori di "equivalenza" o confronto "logico" fra oggetti.

* `==`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

```python
"ciao mondo" == "ciao "+"mondo"  # True
```

"zorro" > "aereo" # True
"accumulare" > "abbondare" # True

"ciao" != "CIAO" # True

# possono anche essere concatenati
n = 0.1
0 <= n <=1 # True

## Overload
li possiamo definire noi per le classi che creiamo, implementando i metodi speciali `__eq__()`, `__gt__()`...


