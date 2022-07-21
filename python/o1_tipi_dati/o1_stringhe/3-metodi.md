Segue un breve elenco di metodi utili degli oggetti di tipo stringa. Tutti questi metodi creano nuove copie della stringa su cui vengono chiamati, e non modificano mai l'originale.


# REPLACE

print(s.replace("mondo", "socio"))


# JOIN
# concatena le stringhe di una lista con un separatore
print(".".join(["www", "google", "it"]))


# SPLIT

print("www.google.it".split("."))

# STRIP

print("["+"  toglie gli spazi ai lati  ".strip()+"]")


# PRESENZA SOTTOSTRINGHE

"ciao" in "ciao mondo" # true
"miao" in "ciao mondo" # false