# iterare su una lista
for i in [1,2,3]:
    print(i)


d = {"gatto":"miao", "cane":"bau"}
for key, val in d.items():
    print(key, val)


for c in "ciao mondo!":
    print(c)


# per emulare il for tradizionale del C:

for i in range(0, 100): # for(i=0;i<100;i++)
    print(i)


# molto spesso conviene sostituire il for con una 
# list comprehension



