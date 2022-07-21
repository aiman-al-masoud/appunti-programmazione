#
# Le eccezioni possono anche essere sollevante.
#
# Questo permette di delegare la gestione della situazione anomala
# ad altre parti del programma, non necessariamente la posizione
# da dove è scaturita l'anomalia.
#

from random import choice


def servizio_web():

    """
    Questa è una funzione non interagisce con l'utente
    """

    connessione = choice([True, False])
    if not connessione:
        raise ConnectionError("Connessione assente, perché errore ...")
    

def main():

    """
    L'utente interagisce con questa funzione.
    """

    try:
        x = servizio_web()
        # fai qualcos'altro ...
    except :
        print("La ")


