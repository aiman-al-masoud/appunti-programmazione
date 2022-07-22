# Type

Ritorna il tipo dell'oggetto su cui viene invocato.

```python
s = "questa è una stringa"
t = type(s)
t # str
```

Questa è proprio la builtin `str()`, o costruttore delle stringhe, a cui adesso stiamo puntando con la variabile `t`.

```python
t(1) # '1'
```

Nel caso di oggetti di una classe custom, type ritornerà proprio il costruttore di quella classe.