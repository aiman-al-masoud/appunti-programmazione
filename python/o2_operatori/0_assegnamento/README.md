# Assegnamento

L'operatore di assegnamento associa una variabile (vecchia o nuova) ad un oggetto. Per esempio, creiamo la variabile `a`:

```python
a = 1 + 1 
```
La variabile `a` punta all'intero `2`. Possiamo far puntare un'altra variabile allo stesso oggetto, così:

```python
b = a
```

Possiamo riassegnare la variabile `a`, anche con un tipo di dati diverso:

```python
a = "ciao"
```

Possiamo anche fare assegnamenti a catena:

```python
y = x = "ciao mondo"
```

Equivale a:

```python
x = "ciao mondo"
y = x
```