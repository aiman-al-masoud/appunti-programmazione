# List Comprehension

Potente sintassi che funge da mappa e/o da filtro per gli elementi di una lista.Ritorna nuova lista, non modifica l'originale. Molto comoda se ci si prende la mano.

```python
l1 = [1,2,3,4,5,6]
```


# Mappa

Sottraggo uno a ciascun elemento.

```python
[x-1 for x in l1] # [0, 1, 2, 3, 4, 5]
```

# Filtro

tengo solo gli elementi maggiori di 2

```python
[x for x in l2 if x > 2] # [3, 4, 5, 6]
```

# Mappa+Filtro

Applico filtro prima, mappa dopo.


```python 
[x-1 for x in l1 if x > 2] # [2, 3, 4, 5]
```


# La Funzione Builtin Range

La menzioniamo qui al volo perché può essere utile in combinazione con le comprehensions... e negli esercizi!

```python
inizio=0
fine=100
passo=2
list(range(inizio, fine, passo)) # [0, 2, 4, 6, ... 98]
```