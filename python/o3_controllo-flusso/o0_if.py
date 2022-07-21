condizione = True
altra_condizione = True
altra_condizione2 = True

# compi una sola di queste azioni, 
# la prima per cui la condizione vale:

if condizione:
    pass # fai qualcosa se condizione
elif altra_condizione: 
    pass # fai qualcos'altro se altra_condizione
elif altra_condizione2:
    pass # fai qualcos'altro se altra_condizione2
else: 
    pass # se tutto il resto fallisce, fai questo 


# Consiglio: non usare troppi elif, e non annidarli, 
# diventa difficile ragionare sul programma.
#