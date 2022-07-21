#
# Ma quando ci sono veramente tanti argomenti da linea 
# di comando, si ripresenta il problema degli argomenti
# posizionali! Vorremmo poter passare gli argomenti
# in qualsiasi ordine, come facciamo con i kwargs in Python. 
#
# Usando sys.argv, questo richiederebbe molto lavoro
# da parte nostra. Fortunatamente, in Python c'è già 
# una libreria standard che fa a caso nostro.
#
#

import argparse


p =argparse.ArgumentParser()

p.add_argument("-n", "--ripetizioni")
p.add_argument("-c", "--colore")



d = p.parse_args()

print(d)


