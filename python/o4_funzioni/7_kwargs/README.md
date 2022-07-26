# Kwargs

Se una funzione comincia ad avere troppi argomenti posizionali, può diventare difficile ricordarsi l'ordine esatto in cui inserirli,specie se molti sono opzionali.

Qui entrano in gioco i **keyword args** (o **kwargs**), che si possono passare in qualunque ordine e opzionalmente.


```python
def stampa(**kwargs):
    params = {"text":"ciao mondo", "ripetiz":2}
    params.update(kwargs)

    for i in range(params["ripetiz"]):
        print(params["text"])

stampa( ripetiz=4, text="the quick brown fox ...")
```

Nota che se una funzione ha sia argomenti posizionali che kwats, i primi esigono di essere inseriti prima dei kwargs.


