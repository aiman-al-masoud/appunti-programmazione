#
# Per uscire da un loop (break), o per saltare alla 
# prossima iterazione (continue) in modo prematuro.
#


db = [{"nome":"Tizio", "eta":30},
      {}, # vuoto
      {"nome":"Caio", "eta":40},
      {"nome":"Sempronio", "eta":50}]


# se trovi record vuoto, salta alla prossima iterazione
for r in db:
    
    if not r: # è vuoto
        continue

    print(r)


# se trovi record vuoto, interrompi il loop
for r in db:
    
    if not r: # è vuoto
        break

    print(r)
