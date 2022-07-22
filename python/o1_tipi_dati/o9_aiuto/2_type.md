# Type

Ritorna il tipo dell'oggetto su cui viene invocato.

```python
s = "questa è una stringa, ma verifichiamolo"
t = type(s)
t # str
```

Cos'è `str`? Ma è proprio la builtin `str()`, o costruttore delle stringhe, a cui adesso stiamo puntando con la nostra variabile `t`.

```python
t(1) # '1'
```

Come fare:

```python
str(1) # '`'
```

Nel caso di oggetti di una classe custom, type ritornerà proprio il costruttore di quella classe.