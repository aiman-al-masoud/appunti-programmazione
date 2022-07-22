# Keys

```python
list(d.keys()) # ['gatto', 'cane', 'pesce']
```

# Values

```python
list(d.values()) # ['miao', 'wof', None]
```

# Items (lista di tuple)

```python
list(d.items()) # [('gatto', 'miao'), ('cane', 'wof'), ('pesce', None)]
```

Per esempio:

```python
for animale, verso in d.items():
    print(animale, "fa", verso)
```

# Da lista di Tuple

```python
l1 = [('gatto', 'miao'), ('cane', 'wof')]
dict(l1) # {'gatto': 'miao', 'cane': 'wof'}
```
