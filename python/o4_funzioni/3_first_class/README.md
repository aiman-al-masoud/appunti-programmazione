# Cittadini di Prima Classe

In Python le funzioni sono a tutti gli effetti degli oggetti, si possono **assegnare a variabili** e **passare come argomento** ad altre funzioni.

Si dice che le funzioni sono **cittadine di prima classe**, (**first order citizens**), o più semplicemente **first order**.


```python
def get_nome():
    return "Mario"


def saluta(fx):
    return "Ciao "+fx()+", come stai?"

# assegnamento a var
fx = get_nome


# passaggio come arg
saluta(fx) # 'Ciao Mario, come stai?'

```




#
# Funzioni di ordine superiore:
# sono funzioni che prendono come argomento, o ritornano
# altre funzioni. 
# https://it.wikipedia.org/wiki/Funzione_di_ordine_superiore
# 
# saluta() è una funzione di ordine superiore.
#




