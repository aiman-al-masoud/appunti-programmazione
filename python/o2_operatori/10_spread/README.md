# Unpacking/Spread


Per svolgere lo 'spacchettamento' (unpacking) di un **tipo iterabile**
(lista, dizionario, insieme, tupla ...). Spacchettamento vuol dire poter usare gli elementi dell'iterabile come argomenti di una funzione, oppure al posto dei literals in una nuova lista/dizionario.

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


https://how.wtf/spread-operator-in-python.html