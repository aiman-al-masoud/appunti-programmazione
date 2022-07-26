# MODIFICA GLOBALI DA FUNZIONE 

# Se si prova a modificare una var globale dall'interno
# di una funzione, Python crederà che si tratti di 
# una variabile locale non ancora definita:

def change_x():
    x+=1 # UnboundLocalError: local variable 'x' referenced before assignment

# change_x()

# Per modificarla, bisogna dichiarare esplicitamente
# che si sta usando una var globale:

def change_x_ok():
    global x
    x+=1 

change_x_ok()
print(x)
