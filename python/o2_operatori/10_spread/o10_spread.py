# https://how.wtf/spread-operator-in-python.html
#
# Per svolgere lo 'spacchettamento' (unpacking) di un iterabile
# (lista, dizionario ...).
#
# Spacchettamento vuol dire potere usare gli elementi come argomenti
# di una funzione, oppure come literals in una nuova lista/dizionario.
#

# Lista
l = [1,2,3]
l = [*l, 4, 5, 6]

print(l)

# Dizionario
d = {"gatto":"miao", "cane":"bau"}

d = {**d, "tigre":"ciuff"}

print(d)

# Usare elementi lista come argomenti
def tre_arg(a,b,c):
    return a+b+c

tre_arg(*[1,2,3]) # 6