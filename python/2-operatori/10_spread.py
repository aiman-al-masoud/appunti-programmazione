# https://how.wtf/spread-operator-in-python.html
#
# Per svolgere lo 'spacchettamento' (unpacking) di un iterabile
# (lista, dizionario ...).
#
#



d = {"gatto":"miao", "cane":"bau"}

d = {**d, "tigre":"ciuff"}

print(d)

l = [1,2,3]
l = [*l, 4, 5, 6]
print(l)


def tre_arg(a,b,c):
    return a+b+c

print(tre_arg(*[1,2,3]))