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

print(y) # NameError: name 'y' is not defined


# LETTURA GLOBALI DA FUNZIONE




# variabili locali
# variabili globali
# pass by val vs pass "by ref": ovvero quando i parametri vengono modificati da funzione
# keyword global ( modificare globali da funzione)