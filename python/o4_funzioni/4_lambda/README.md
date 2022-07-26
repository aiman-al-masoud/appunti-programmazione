# Funzioni Lambda 

Altresì note come funzioni anonime, sono utili da passare come argomenti a funzioni di ordine superiore per farle fare qualcosa di utile.

```python
c = map(lambda x : str(x) , [1, True, "ciao", {}])
c = list(c)

print(c)
```