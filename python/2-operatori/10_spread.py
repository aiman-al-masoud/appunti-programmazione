# https://how.wtf/spread-operator-in-python.html


d = {"gatto":"miao", "cane":"bau"}

d = {**d, "tigre":"ciuff"}

print(d)

l = [1,2,3]
l = [*l, 4, 5, 6]
print(l)