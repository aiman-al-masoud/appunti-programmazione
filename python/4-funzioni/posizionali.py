#
# Il modo più semplice di passare argomenti ad una 
# funzione è tramite gli argomenti posizionali.
#

def stampa(text, ripetiz):
    for i in range(ripetiz):
        print(text)

stampa("ciao",3)

#
# Gli argomenti posizionali (se ci sono) sono i primi
# che una funzione accetta, e l'ordine è importante
#

# stampa(3, "") # TypeError: 'str' object cannot be interpreted as an integer

#
# Si possono anche impostare valori di default
# degli argomenti, così:
#

def stampa(text, ripetiz=2):
    for i in range(ripetiz):
        print(text)

stampa("ciao mondo")