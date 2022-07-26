# Funzioni Lambda 

Altresì note come funzioni anonime, sono utili da passare come argomenti a funzioni di ordine superiore per farle fare qualcosa di utile.


Questa è una lambda che converte l'argomento in una stringa:
```python
lambda x : str(x) 
```

Applichiamo la lambda ad un'intera lista usando la funzione higher order `map()`:

```python
c = map(lambda x : str(x) , [1, True, "ciao", {}])
c = list(c)

c # ['1', 'True', 'ciao', '{}']
```