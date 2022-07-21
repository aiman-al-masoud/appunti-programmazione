#
# Il modo più semplice di passare argomenti ad una 
# funzione è tramite gli argomenti posizionali.
#

def stampa(text, ripetiz):
    for i in range(ripetiz):
        print(text)

stampa("ciao",3)
