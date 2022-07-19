# ISIEME
# 
# Un insieme è una lista non-ordinata e 
# priva di duplicati. è mutabile.
#
#


# PRIVA DI DUPLICATI

set("caciocavallo") # {'a', 'v', 'l', 'c', 'o', 'i'}


# OPERAZIONI SUGLI INSIEMI

volatili = {"barbagianni","oca","pipistrello"}
mammiferi = {"gatto","pipistrello", "elefante"}


# UNIONE

s = volatili|mammiferi
print(s)

# INTERSEZIONE

s = volatili&mammiferi
print(s)

# DIFFERENZA

print(volatili - mammiferi)
print(mammiferi - volatili)









