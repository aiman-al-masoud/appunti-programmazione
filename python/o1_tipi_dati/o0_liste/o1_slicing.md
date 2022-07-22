# Slicing

Crea una **shallow copy** della lista originale, dal primo indice (incluso), all'ultimo indice (escluso).

```python
l1 = [1,2,3,4,5]
l2 = l1[2:4]
l2 # [3, 4]
```

## Trucco per copiare lista 

```python
l3 = l1[:] 
l3[0] = 9 # modifico solo copia
l1 # [1,2,3,4,5]
l3 # [9, 2, 3, 4, 5]
```

### Shallow Copy:
Questo 'trucco' duplica la struttura della lista, ma i gli elementi puntano a quelli originali in memoria. Quindi riassegnare un un indice non modifica ambo le liste (struttura duplicata). Ma modificare un elemento lo fa (oggetti identici). In questo caso però si tratta di int, che sono immutabili.

## Step

Con inizio e fine impliciti, e step esplicito:

```python
l4 = l1[::2] # step=2 (salto gli indici pari)
l4 # [2, 4]
```
