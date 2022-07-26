# Cittadini di Prima Classe

In Python le funzioni sono a tutti gli effetti degli oggetti, si possono **assegnare a variabili** e **passare come argomento** ad altre funzioni.

Si dice che le funzioni sono **cittadine di prima classe**, (**first order citizens**), o più semplicemente **first order**.


def get_nome():
    return "Mario"

# funzione di ordine superiore
def saluta(fx):
    return "Ciao "+fx()+", come stai?"


# questa sintassi per fare riferimento,
# da notare che non non si usano le (), perché 
# NON vogliamo chiamare la funzione!

fx = get_nome

print(saluta(fx))



#
# Funzioni di ordine superiore:
# sono funzioni che prendono come argomento, o ritornano
# altre funzioni. 
# https://it.wikipedia.org/wiki/Funzione_di_ordine_superiore
# 
# saluta() è una funzione di ordine superiore.
#




