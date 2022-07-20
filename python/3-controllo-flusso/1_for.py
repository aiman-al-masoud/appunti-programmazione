# per iterare su una lista
for i in [1,2,3]:
    print(i)

# per iterare su una stringa
for c in "ciao mondo!":
    print(c)

# per iterare su una lista, con indice
for i, val in enumerate(["un", "due", "tre"]):
    print(i, val)

# per iterare su una "lista di tuple"
d = {"gatto":"miao", "cane":"bau"}
for key, val in d.items():
    print(key, val)

# per emulare il for tradizionale del C:
for i in range(0, 10): # for(i=0;i<10;i++)
    print(i)

# più in generale:
start=0  # default=0 
stop=10 # param obbligatorio
step=1   # default=1
for i in range(start, stop, step):
    print(i)


# spesso conviene sostituire il for con una 
# list comprehension, eg:

l = [1,2,3,4] # voglio moltiplicare per 2 ciascun elem

# tradizionale:
for i in range(len(l)):
    l[i] *= 2

# meglio:
l = [2*x for x in l]




