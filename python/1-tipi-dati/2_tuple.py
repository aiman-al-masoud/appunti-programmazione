# TUPLA
#
# Una tupla è come una lista, ma è IMMUTABILE.
#


# queste sono tuple:
p1 = ("Pinko", 32, "marinaio")
p2 = ("Tizio", 43, "lattaio")

# errore:
# p1[0] = "Pallino"


# CREARE TUPLE DA UN ELEMENTO

# sì 
t = ("Mario",)

# no!
t = ("Mario") # ="Mario"



# INDICI PER DIZIONARIO

# gli indici di un dizionario devono essere immutabili.
# quindi una stringhe o una tuple (se non contiene oggetti mutabili) 
# possono fungere da indici, ma le liste no! 

hash([]) # TypeError: unhashable type
hash( (1, 2) ) # -3550055125485641917
hash( (1, 2, []) ) # TypeError: unhashable type
