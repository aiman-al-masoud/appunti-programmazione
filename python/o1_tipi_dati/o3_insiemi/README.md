# Insieme

Un insieme è una lista **non-ordinata** e **priva di duplicati**. È mutabile.


# No Duplicati

```python
set("caciocavallo") # {'a', 'v', 'l', 'c', 'o', 'i'}
```

# Operazioni

Sono definite alcune delle tipiche operazioni matematiche sugli insiemi, prendiamo come esempio:

```python
volatili = {"barbagianni","oca","pipistrello"}
mammiferi = {"gatto","pipistrello", "elefante"}
```

## Unione

```python
volatili|mammiferi # {'barbagianni','oca','pipistrello', 'gatto', 'elefante'}
```

## Intersezione

```python
volatili&mammiferi # {'pipistrello'}
```

## Differenza

### c'è in volatili ma non in mammiferi

```python
volatili - mammiferi # {'barbagianni', 'oca' }
```

### c'è in mammiferi ma non in volatili
```python
mammiferi - volatili # { 'gatto', 'elefante'}
```
### Differenza Simmetrica

```python
mammiferi.symmetric_difference(volatili) # {'barbagianni','oca', 'gatto', 'elefante'}
```

Equivale a unione delle differenze, o unione meno intersezione.


