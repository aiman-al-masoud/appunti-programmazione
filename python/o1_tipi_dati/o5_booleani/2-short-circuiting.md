# Shortcircuting

Cosa succede se si concatenana una sfilza di valori booleani (o falsy/truthy) tramite gli operatori `and` o `or`? L'interprete, inguaribile pigrone, prova a fermarsi prima di aver completato l'intera catena di `and`/`or`, non appena si accorge che il risultato finale è già evidente.


Una catena di `or` si ferma non appena trova un valore truthy:

```python
x = False or None or 0 or 2 or 1
x # 2
```

Da notare che quello che verrà assegnato alla x è proprio un `2`, il primo valore truthy trovato nella catena.


Al contrario, una catena di `and` si ferma non appena trova un valore falsy:

```python
x = True and 1 and "ciao" and 0 and None 
x # 0
```

Il trucchetto dell'`or` è utilizzato per definire valori di default/fallback quando si teme che una variabile sia [`None`](../o10_none/README.md). 

```python
quantita = None
# ...
ordina_spedizione(quantita or 1) # se quantità non specificata da utente, default=1
```

L'uncia cosa è stare attenti quando lo `0` (o la lista vuota `[]`, o la stringa vuota `""` ...) sono valori validi, perché verrano rimpiazzati dal default in quanto falsy!

# Builtin `all()` & `any()`

Da menzionare anche le builtin `all()` e `any()`, che prendono una lista di condizioni e restituiscono un booleano. La `all()` è `True` se tutte le condizioni sono vere, `any()` se almeno una è vera.

```python
all([True, 1, 22, "ciao"]) # True
```
