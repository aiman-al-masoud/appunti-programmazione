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
#
#


# Riassegnare (con =) una variabile argomento 
# funzionera sullo scope locale:

x = 10

def foo(x):
    x = 11

foo(x)
print(x)

# Gli oggetti immutabili non possono mutare:

y = 1

def foobar(y):
    y.imag = 1

# foobar(y)


# Invece, se il tipo dell'argomento è mutabile e lo si 
# modifica senza riassegnarlo, si sta modificando 
# l'originale:

li = [1,2]

def bar(li):
    li.append(3)
    
    # li = li + [4] # non modifica arg, perché chiaramente riassegnamento
    # li+=[4] # strano comportamento! https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists

bar(li)
print(li)


#
#
# Ufficialmente Python passa "By Assignment"
# https://realpython.com/python-pass-by-reference/
# https://stackoverflow.com/questions/50534394/what-does-it-mean-by-passed-by-assignment
#
#
