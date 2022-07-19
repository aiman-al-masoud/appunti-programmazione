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

s = volatili+mammiferi
print(s)

# DIFFERENZA

# c'è in volatili ma non in mammiferi
print(volatili - mammiferi)

# c'è in mammiferi ma non in volatili
print(mammiferi - volatili)

# tutti gli elementi che mancano in entrambe i set
print(mammiferi.symmetric_difference(volatili))
# equivale a:
(volatili - mammiferi)|(volatili - mammiferi)









