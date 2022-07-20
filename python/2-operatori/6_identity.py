#
# Identità != Uguaglianza.
#
# Identità (is) fra due variabili vuol dire che puntano
# allo stesso oggetto in memoria.
# 
# Uguaglianza (==) vuol dire solo che gli oggetti hanno
# proprietà equivalenti.
#
# Identità implica Uguaglianza.
# Ma non viceversa.
#

x = {"gatto":"miao"}
y = x

x is y # True

x = {"gatto":"miao"}
y = {"gatto":"miao"}

x is y # False
x == y # True


# CONFRONTO NONE

# usa sempre (is) per controllare che un oggetto 
# sia non definito (None)

x = None 
x is None # Ok 
x == None # NON FARLO!

# perché logica del metodo di confronto (==) potrebbe 
# provare ad accedere agli attributi di None, provocando
# un'eccezione in runtime perché None non ha attributi.

class Persona:
    def __init__(self, nome):
        self.nome = nome 
    
    def __eq__(self, o):
        return self.nome == o.nome

p = Persona("Mario")
p == None # AttributeError: 'NoneType' object has no attribute 'nome'