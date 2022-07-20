#
# Per uscire da un loop (break), o per saltare alla 
# prossima iterazione (continue) in modo prematuro.
#


# es: 

db = [{"nome":"Tizio", "eta":30},
      {}, # vuoto
      {"nome":"Caio", "eta":40},
      {"nome":"Sempronio", "eta":50}]


for r in db:
    
    if not r: # è vuoto
        continue

    print(r)
