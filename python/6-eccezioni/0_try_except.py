#
# Un’eccezione è un evento anomalo che provoca 
# l’interruzione del normale flusso esecuzione 
# di un programma
# 
# Se un'eccezione non viene catturata, il programma uscira dall'attuale
# blocco di codice, verso quello esterno. Se non viene catturata in nessun
# blocco di codice estero, l'eccezione finirà per uscire il programma
# con un errore.
#
# Se sospettiamo che del codice lancerà un'eccezione, possiamo 
# gestirla tramite un try-except:
#

try: # viene eseguito tutto solo se non solleva eccezioni
    1/0
except Exception as e: #viene eseguito solo in caso di eccezione
    print(e)


#
# Vediamo un altro esempio con un tipo diverso di eccezione, 
# specificamente catturato:
#

duck = {}
try:
    duck.quack()
except AttributeError as e: # solo eccezioni AttributeError
    print(e)
except Exception as e: # tutte le altre eccezioni
    print(e)
    




