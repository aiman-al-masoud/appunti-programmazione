# Break-Continue

Per uscire da un loop (`break`), o per saltare alla prossima iterazione (`continue`) precocemente.


Es: creiamo una lista di "record" su cui iterare:

```python
db = [{"nome":"Tizio", "eta":30},
      {}, # vuoto
      {"nome":"Caio", "eta":40},
      {"nome":"Sempronio", "eta":50}]
```

## Continue

Se trovi record vuoto, salta alla prossima iterazione.

```python
for r in db:
    
    if not r: # vuoto è falsy
        continue

    print(r)
```

## Break

Se trovi record vuoto, interrompi il loop

```python
for r in db:
    
    if not r: # vuoto è falsy
        break

    print(r)
```