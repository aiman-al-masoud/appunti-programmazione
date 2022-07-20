#
# Si chiama ternario perché prende 3 operandi,
# una condizione, un valore se la condizione 
# è soddisfatta, e un valore se la condizione 
# non è soddisfatta.
#
#

eta = 25
x = "maggiorenne" if eta >= 18 else "minorenne"
x # "maggiorenne"

# MOLTO meglio che:

if eta >= 18:
    x = "maggiorenne"
else:
    x = "minorenne"


# NB: se devi ottenere valori booleani, allora puoi
# semplificare ulteriormente, es:

if eta >= 18:
    x = True
else:
    x = False

# diventa:

x = eta>=18








