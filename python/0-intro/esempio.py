# questo è un commento normale 
# questo è un altro, ok ... ?

x='''
Questa è una "stringa di documentazione" (docstring).
Su più righe! Assegnata ad una variabile!
'Ciao mondo!'
'''

# chiamata a funzione builtin 
print(x)


# Python è 'dinamico': le variabili possono cambiare tipo
x = 1
x = True
x = []


# ESPRESSIONI vs STATEMENT
# 
# Le espressioni sono combinabili, si semplificano,
# e ritornano un valore (simile a matematica).
#
# Gli statement non hanno un valore di ritorno.
#

# questo è uno statement
if True:
    # ( l'indentazione è sintattica! )
    print("ciao mondo")

# questa è un'espressione
"ciao "+str(1+(1//2)+21)+" volte"


# PASS
# pass serve per tenere il posto e non fare
# nulla.
#

# questo if non fa nulla
if True:
    pass
