#
# A volte non sappiamo a priori quanti argomenti dovremo
# passare ad una funzione. Una valida opzione è passare una lista 
# o tupla di argomenti. Un'altra opzione, in Python, è di passare un numero 
# smodato di argomenti!
# 
# Bisogna usare la sintassi speciale con singolo asterisco. La funzione 
# riceverà tutti gli argomenti, in ordine, in una singola tupla.
#
#

from functools import reduce

def my_sum(*args):

    """
    Questa funzione fa la somma di tutti i suoi (illimitati)
    argomenti.
    """
    return reduce(lambda x,y:x+y, args)

my_sum(1,2,3,4) # 10


#
# Reduce è una funzione di ordine superiore. Prende una funzione g e una lista,
# applica la funzione g a due elementi della lista alla volta, partendo da sinistra,
# e accumulando il risultato.
#

