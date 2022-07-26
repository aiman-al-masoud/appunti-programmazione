# Ritornare Annidate


Questa tecnica si può usare per creare e ritornare
nuove funzioni specializzate:

```python
def get_finder(regex):

    def finder(text):
        import re
        return re.findall(regex, text)

    return finder

f = get_finder(r"\d+")

f("3 4") # ['2', '3']
```

Get finder è una [funzione di ordine superiore](../3_first_class/1_higher_order.md) perché ritorna un'altra funzione.