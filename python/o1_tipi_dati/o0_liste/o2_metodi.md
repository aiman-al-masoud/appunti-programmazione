# Metodi

Un elenco di metodi delle liste. Tutto è un oggetto in Python, comprese le liste. Gli oggetti hanno metodi, che sono funzioni associate all'oggetto.


Creo una lista di prova 

```python
l1 = [1,2,3,4,5]
```

# Append

```python
l1.append("ciao")
l1 # [1, 2, 3, 4, 5, "ciao"]
```

# Insert

```python
l1.insert(0, "mondo")
l1 # ["mondo", 1, 2, 3, 4, 5, "ciao"]
```

# Extend

```python
l1.extend([6,7,8])
# oppure: l1 = l1 + [6, 7, 8]
l1 # ["mondo", 1, 2, 3, 4, 5, "ciao", 6, 7, 8]
```

# Remove

(rimuove solo la prima occorrenza)

```python
l1.remove("mondo") 
l1.remove("ciao") 
l1 # [ 1, 2, 3, 4, 5, 6, 7, 8]
```

# Del

```python
del l1[0]
l1 # [2, 3, 4, 5, 6, 7, 8]
```

# Pop

```python
x = l1.pop()
x # 8
l1 # [2, 3, 4, 5, 6, 7]
```

# Len

```python
len(l1) # 6
```

# Sort

Ordina la lista. Bisogna fare attenzione a non ordinare liste disomogenee, come liste di interi e stringhe, perché il confronto fra tipi diversi potrebbe non essere definito.

```python
l1.sort()
l1 # [2, 3, 4, 5, 6, 7]
```


# Count

Conta le occorrenze di un elemento. In caso di liste annidate **NON** è ricorsivo! 

```python
l1.append(4)
l1.count(4) # 2
```