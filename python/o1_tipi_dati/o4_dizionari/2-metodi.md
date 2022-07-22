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

