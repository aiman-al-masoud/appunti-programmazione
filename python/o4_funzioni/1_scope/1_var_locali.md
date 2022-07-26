# Variabili Locali

Sono dichiarate all'interno di una funzione, non sono visibili al suo esterno, ed esistono solo durante l'esecuzione della funzione, poi vengono deallocate.

```python
def func():
    y = 10


func()
print(y) # NameError: name 'y' is not defined
```



