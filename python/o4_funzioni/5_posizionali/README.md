# Argomenti Posizionali

Li abbiamo già intravisto, è il modo più semplice di passare argomenti ad una funzione:

```python
def stampa(text, ripetiz):
    for i in range(ripetiz):
        print(text)

stampa("ciao",3) # stampa 3 volte 
```

Gli argomenti posizionali (se ci sono) sono i primi che devono essere inseriti, e il loro ordine deve essere rispettato:

```python
stampa(3, "") # TypeError: 'str' object cannot be interpreted as an integer
```

## Default 

Si possono anche impostare valori di default degli argomenti posizionali, così:

```python
def stampa(text, ripetiz=2):
    for i in range(ripetiz):
        print(text)

stampa("ciao mondo") # stampa due volte
```