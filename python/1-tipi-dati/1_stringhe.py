# STRINGA
#  
# Una stringa è una sequenza immutabile di stringhe 
# di lunghezza=1. (Non esiste il tipo char).
#

# questa è una stringa
s = "ciao mondo!"

# INDEXING & SLICING 

# proprio come nelle liste
s[0] # 'c'
s[5:] # 'mondo'

# APICI DOPPI == APICI SINGOLI

s = "ciao mondo!"
# oppure:
s = 'ciao mondo!'

# ESCAPE CHARS

'ho detto \'ciao mondo!\''
# oppure:
'ho detto "ciao mondo!"'


# IMMUTABILITÀ

# le stringhe sono un tipo immutabile, questo
# codice produce un errore se eseguito:

s = "ciao mondo!"
# s[5:] = "socio"


# REPLACE

print(s.replace("mondo", "socio"))


# JOIN
# concatena le stringhe di una lista con un separatore
print(".".join(["www", "google", "it"]))


# SPLIT

print("www.google.it".split("."))

# STRIP

print("["+"  toglie gli spazi ai lati  ".strip()+"]")

# F-STRINGS

from datetime import datetime
oggi = datetime.today()
s=f"Oggi è il {oggi.day}/{oggi.month}/{oggi.year}"
print(s)

