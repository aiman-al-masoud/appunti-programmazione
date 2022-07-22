# COMPREHENSION

Come le liste, le tuple e gli insiemi, anche i dizionari hanno una comprehension. Ma un po' diversa dato che si tratta di coppie chiave-valore. Per esempio, possiamo costruire un dizionario :

```python
l1 = [('gatto', 'miao'), ('cane', 'wof'), ('pesce', None)]
d={x[1]:x[0] for x in l1 }
print(d)
```