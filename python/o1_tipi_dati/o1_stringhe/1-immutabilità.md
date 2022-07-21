# Immutabilità

Le stringhe sono un tipo **immutabile**. L'immutabilità di un oggetto vuol dire che una volta creato, non ne si possono modificare gli attributi. 

Questo codice produce un errore se eseguito:

```python
s = "ciao mondo!"
s[5:10] = "socio" # TypeError: 'str' object does not support item assignment
```

Dovremo ricorrere alla **creazione di una nuova** stringa, così:

```python
s2 = s.replace("mondo", "socio")
```

Oppure così:

```python
s2 = s[:5]+"socio"+s[10:]
```

O anche così, dato che una lista è mutabile:

```python
l = list(s)
l[5:10] = list("socio")
s2 = "".join(l)
```