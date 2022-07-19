# LISTA
#
# Una lista è un insieme ordinato e mutabile di
# di elementi eterogenei.
#

l1  = [1, 2.2, "ciao", True, 1+1j]
print("(0)", l1)

# INDICIZZAZIONE

x = l1[0]
y = l1[1]
print("(1)", x, y)

# INDICIZZAZIONE NEGATIVA

x = l1[-1] # ultimo elemento
y = l1[-2] # penultimo ... 
print("(2)", x, y)

# SLICING

# crea copia con elemento al primo indice incluso, all'ultimo indice escluso.
x = l1[2:4]
print("(3)", x)

# trucco per copiare lista 
x = l1[:] 
print("(4)", x)

# con inizio e fine impliciti, e step=2 (salto pari) 
x = l1[::2]
print("(5)", x)


# x[0]  ="CAPRA"
# print(x)
# print(l1)
# indexing 
# slicing 

