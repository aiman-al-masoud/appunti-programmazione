# DIZIONARIO
# 
# Un dizionario è un insieme non-ordinato di 
# coppie chiave-valore. è mutabile.
#
#

d = {} # dizionario vuoto
d = {"gatto": "miao", "cane": "bau", "pesce": None}


# INDICIZZAIONE

d["gatto"] # 'miao'


# AGGIORNAMENTO

d["cane"] = "grrr"
# oppure:
d.update({"cane":"wof"})

# CANCELLAZIONE

# del d["cane"]

# KEYS

list(d.keys()) # ["gatto", "cane", "pesce"]

# VALUES

list(d.values()) # ["miao", "wof", None]

# ITEMS (lista di tuple)

list(d.items()) # [('gatto', 'miao'), ('cane', 'wof'), ('pesce', None)]

# per esempio:
for animale, verso in d.items():
    print(animale, "fa", verso)

# DA LISTA DI TUPLE

dict([('gatto', 'miao'), ('cane', 'wof'), ('pesce', None)])


# COMPREHENSION

l1 = [('gatto', 'miao'), ('cane', 'wof'), ('pesce', None)]
d={x[1]:x[0] for x in l1 }
print(d)

