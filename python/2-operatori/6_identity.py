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




