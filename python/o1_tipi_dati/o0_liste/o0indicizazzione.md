# Indicizzazione

L'indicizzazione parte da zero, e va fino alla dimensione della lista meno uno.

Creo una lista di prova:

```python
l1 = [1,2,3,4,5]
```

Proviamo ad estrarre dei valori:

```python
x = l1[0] # 1 (primo elemento)
y = l1[1] # 2 (secondo elemento) 
z = l1[4] # 5 (ultimo elemento)

x, y, z = l1[0], l2[1], l2[4] # oppure così
```

# Indicizzazione Negativa

Gli indici possono anche essere negativi, il meno uno corrisponde all'ultimo elemento, il meno due al penultimo, e così via fino al valore dimensione negativo. 

```python
x = l1[-1] # 5 (ultimo elemento)
y = l1[-2] # 4 (penultimo) 
z = l1[-5] # 1 (primo)
```