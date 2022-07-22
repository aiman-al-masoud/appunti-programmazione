# Shortcircuting

Cosa succede se si concatenana una sfilza di valori booleani (o falsy/truthy) tramite gli operatori `and` o `or`? L'interprete, inguaribile pigrone, prova a fermarsi prima di aver completato l'intera catena di `and`/`or`, se vede che il risultato finale è già chiaro.


Una catena di `or` si ferma non appena trova un valore truthy:

```python
x = False or None or 0 or 2 or 1
x # 2
```

Da notare che quello che verrà assegnato alla x è proprio un `2`, il primo valore truthy trovato nella catena.


Al contrario, una catena di `and` si ferma non appena trova un valore falsy

x = True and 1 and "ciao" and 0 and None 
print(x) # 0


# all()
# any()

