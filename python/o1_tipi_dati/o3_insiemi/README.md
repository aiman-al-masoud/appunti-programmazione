# Insieme

Un insieme è una lista **non-ordinata** e **priva di duplicati**. È mutabile.


# No Duplicati

```python
set("caciocavallo") # {'a', 'v', 'l', 'c', 'o', 'i'}
```

# Operazioni

```python
volatili = {"barbagianni","oca","pipistrello"}
mammiferi = {"gatto","pipistrello", "elefante"}
```

## Unione

```python
s = volatili|mammiferi
print(s)
```

## Intersezione

```python
s = volatili&mammiferi
```

## Differenza

### c'è in volatili ma non in mammiferi

```python
print(volatili - mammiferi)
```

### c'è in mammiferi ma non in volatili
```python
print(mammiferi - volatili)
```
### differenza simmetrica

```python
print(mammiferi.symmetric_difference(volatili))
```

equivale a unione delle differenze:

```python
print((volatili - mammiferi)|(  mammiferi -volatili))
```




