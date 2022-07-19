# tipizzazione dinamica
# expressions vs statements 
# funzione/builtin vs operatore
# commenti
# duck-typing
# import
# moduli
# venv
# pip


# questo è un commento normale 

x="""
Questo è un commento "di documentazione".
Su più righe!
'Ciao mondo!'
"""

# chiamata a funzione builtin 
print(x)


# ESPRESSIONI vs STATEMENT
# Le espressioni sono combinabili, si semplificano,
# e ritornano un valore.
#
# Gli statement non hanno un valore e non 
# ritornano niente.
#

# questo è uno statement
if True:
    # ( l'indentazione è sintattica! )
    print("ciao mondo")

# questa è un'espressione
"ciao "+str(1+(1//2)+21)+" volte"



# questo if non fa nulla
if True:
    pass



