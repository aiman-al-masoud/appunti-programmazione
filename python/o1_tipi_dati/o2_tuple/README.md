# Tupla

Una tupla è come una [lista](../o0_liste/README.md), **ma è immutabile**.

Queste sono tuple:

```python
p1 = ("Pinko", 32, "marinaio")
p2 = ("Tizio", 43, "lattaio")
```

Questo è un errore:

```python
p1[0] = "Pallino" # TypeError: 'tuple' object does not support item assignment
```

## Tuple da un elemento

### sì 

```python
t = ("Mario",)
```

### no!

```python
t = ("Mario") # ="Mario"
```

# Chiavi per Dizionario

Ma a cosa caspita servono le tuple se abbiamo le liste? Servono proprio perché sono immutabili. Le chiavi di un dizionario devono essere immutabili. Quindi una stringa o una tupla (se non contiene oggetti mutabili) possono fungere da chiavi, ma le liste no, mai! Gli oggetti immutabili possono essere hashati:

```python
hash([]) # TypeError: unhashable type
hash( (1, 2) ) # -3550055125485641917
hash( (1, 2, []) ) # TypeError: unhashable type
```