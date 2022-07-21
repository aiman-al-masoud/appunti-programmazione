Segue un breve elenco di metodi utili degli oggetti di tipo stringa. Tutti questi metodi creano nuove copie della stringa su cui vengono chiamati, e non modificano mai l'originale.


# Replace

Sostituisce una sottostringa con un'altra (**no** regex).

```python
s = "ciao mondo!"
s.replace("mondo", "socio") # 'ciao socio!'
```

Può anche essere usato per rimuovere il whitespace, così:

```python
" ci a  o  !".replace(' ','') # 'ciao!'
```

# Join

Usa la stringa come separatore per concatenare le stringhe nella lista.

```python
".".join(["www", "google", "it"])  # www.google.it
```

# Split

```python
"www.google.it".split(".") # ['www', 'google', 'it']
```

# Strip

```python
"  toglie gli spazi ai lati   ".strip() # 'toglie gli spazi ai lati'
```

Oppure un'altro char:

```python
"----ciao-----".strip('-') # 'ciao'
```

# Ricerca Sottostringe

Un modo semplice (**no** regex) è di usare l'operatore di appartenenza **in**.

```python
"ciao" in "ciao mondo" # True
"miao" in "ciao mondo" # False
```