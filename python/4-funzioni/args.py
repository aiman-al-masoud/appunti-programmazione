#
# Una funzione in Python può accettare un numero smodato di argomenti!
# 
# Bisogna usare la sintassi speciale con singolo asterisco.
# La funzione riceverà tutti gli argomenti in ordine in una singola tupla.
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
