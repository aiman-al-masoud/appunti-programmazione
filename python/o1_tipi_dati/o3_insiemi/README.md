# Insieme

Un insieme è una lista **non-ordinata** e **priva di duplicati**. È mutabile.


# No Duplicati

```python
set("cacipaperovallo") # {'a', 'v', 'l', 'c', 'o', 'i'}
```

# Operazioni

Sono definite alcune delle tipiche operazioni matematiche sugli insiemi, prendiamo come esempio questi due:

```python
volatili = {"barbagianni","papero","pipistrello"}
mammiferi = {"gatto","pipistrello", "elefante"}
```

## Unione

```python
volatili|mammiferi # {'barbagianni','papero','pipistrello', 'gatto', 'elefante'}
```

## Intersezione

```python
volatili&mammiferi # {'pipistrello'}
```

## Differenza

### c'è in volatili ma non in mammiferi

```python
volatili - mammiferi # {'barbagianni', 'papero' }
```

### c'è in mammiferi ma non in volatili
```python
mammiferi - volatili # { 'gatto', 'elefante'}
```
## Differenza Simmetrica

```python
mammiferi.symmetric_difference(volatili) # {'barbagianni','papero', 'gatto', 'elefante'}
```

Equivale a unione delle differenze, o unione meno intersezione.


