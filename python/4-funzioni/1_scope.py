#
# Scope di una Variabile
#
# È la regione del programma in cui si può 
# fare riferimento alla variabile. 
#  
#

# VARIABILI GLOBALI

# Sono dichiarate a livello di modulo (file), cioè al 
# di fuori di qualunque funzione, classe o oggetto. Sono 
# visibili in lettura dappertutto nel modulo.
x = 10


# VARIABILI LOCALI

# Sono dichiarate all'interno di una funzione, non
# sono visibili al suo esterno.

def func():
    y = 10

func()
# print(y) # NameError: name 'y' is not defined


# LETTURA GLOBALI DA FUNZIONE

# come già detto, non necessita di accorgimenti
# particolari.

def print_x():
    print(x)

print_x()


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




