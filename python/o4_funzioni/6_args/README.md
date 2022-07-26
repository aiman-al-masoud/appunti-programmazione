# Args 

A volte non sappiamo a priori quanti argomenti dovremo passare ad una funzione. Una valida opzione è passare una lista o tupla di argomenti. Un'altra opzione, in Python, è di passare un numero 
smodato di argomenti!

Bisogna usare la sintassi speciale con singolo asterisco. La funzione riceverà tutti gli argomenti, in ordine, in una singola tupla.

```python
from functools import reduce

def my_sum(*args):

    """
    Questa funzione fa la somma di tutti i suoi (illimitati)
    argomenti.
    """
    return reduce(lambda x,y:x+y, args)

my_sum(1,2,3,4) # 10
```

La [`reduce()` è una funzione di ordine superiore.](../3_first_class/1_higher_order.md#reduce)
