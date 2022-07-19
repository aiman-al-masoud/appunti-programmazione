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

# KEYS

list(d.keys()) # ["gatto", "cane", "pesce"]

# VALUES

list(d.values()) # ["miao", "wof", None]

# ITEMS (lista di tuple)

list(d.items()) # [('gatto', 'miao'), ('cane', 'wof'), ('pesce', None)]

# per esempio:
for animale, verso in d.items():
    print(animale, "fa", verso)




# comprehension


# da lista di tuple

