#
# Passaggio By Value vs By Reference 
# 
# By Value: la funzione riceve una copia dell'oggetto
# che le si passa.
#
# By Reference: la funzione riceve un riferimento
# all'oggetto originale che le si passa.
#
#


# Riassegnare un argomento funzionera solo sulla 
# copia locale.
x = 10
def foo(x):
    x = 11

foo(x)
print(x)









# pass by val vs pass "by ref": ovvero quando i parametri vengono modificati da funzione
