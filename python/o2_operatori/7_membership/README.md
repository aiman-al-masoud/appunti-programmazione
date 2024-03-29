# Membership (Appartenenza)

Viene usato per verificare l'appartenenza di un oggetto ad un altro, o ad un "insieme".


```python
18 in [1, 4, 0, 18, 3] # True
```

```python
"dica" in "abdicazione" # True
```

```python
"gatto" not in {"gatto":"miao", "cane":"bau"} # False
```

## Disambiguazione

`in` è la stessa keyword usata nei loop e nelle comprehensions, ma è semplicemente un altro contesto, non c'entra niente con l'operatore di membership.


## Overload 

Implementando il metodo speciale `__contains__()` di una nuova classe.

```python
class Foresta:
    def __contains__(self, o):
        return o in ["cinghiale", "gufo", "lince"]

f = Foresta()
"cinghiale" in f # True
"leone" in f # False
```