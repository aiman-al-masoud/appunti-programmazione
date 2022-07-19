# LISTA
#
# Una lista è un insieme ordinato e mutabile di
# di elementi potenzialmente eterogenei.
#

l1  = ["un", "due", "tre", "quatr", "cinq", "sei"]
print("(0)", l1)

# INDICIZZAZIONE

x, y = l1[0], l1[1]
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
x[0] = 1200102 # modifico solo copia
print("(4)", x, l1)

# con inizio e fine impliciti, e step=2 (salto i pari) 
x = l1[::2]
print("(5)", x)


# APPEND

l1.append("ciao")
l1.append("mondo")
print("(6)", l1)

# INSERT

l1.insert(1, "mondo")
print("(7)", l1)

# EXTEND

l1.extend([7,8,9])
print("(8)", l1)

# REMOVE

l1.remove("mondo")
print("(9)", l1)

# DEL

del l1[0]
print("(10)", l1)

# POP

x = l1.pop()
print("(11)", l1, x)

# LEN

print("(12)", len(l1))

# SORT

l2 = [3,2,1,4,5,1,8,6]
l2.sort()
print("(13)", l2)

# COUNT 

print("(14)", l2.count(1))


# LIST COMPREHENSION

# comodissima sintassi per "mappare" e "filtrare" gli elementi di una lista,
# ritorna nuova lista.

# mappa: sottraggo uno a ciascun elemento
print("(15)", [x-1 for x in l2])

# filtro: tengo solo gli elementi maggiori di 2
print("(16)", [x for x in l2 if x > 2])

# mappa+filtro: filtro e poi mappo
print("(17)", [x-1 for x in l2 if x > 2])



# SFIDA!











