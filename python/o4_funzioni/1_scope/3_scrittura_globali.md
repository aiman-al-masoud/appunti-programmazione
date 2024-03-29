# Modifica Globali da Funzione

Se si prova a **modificare** una variabile globale dall'interno di una funzione, Python crederà che si tratti di una variabile locale non ancora definita, e lancerà un'eccezione:

```python
x = 10

def change_x():
    x+=1 # UnboundLocalError: local variable 'x' referenced before assignment


change_x()
```


## Keyword `global`
Per modificare una globale dall'interno della funzione, bisogna ricorrere alla keyword `global`:

```python
x = 10

def change_x_ok():
    global x
    x+=1 

change_x_ok()
x # 11
```

## Effetti Collaterali

Tuttavia, è consigliato provare altri stratagemmi prima di ricorrere a questo: se troppe funzioni modificano le variabili globali impunemente, rischiamo di dimenticarcene, e di non accorgerci di eventuali bachi relativi agli [effetti collaterali](https://it.wikipedia.org/wiki/Effetto_collaterale_(informatica)) di queste funzioni.

