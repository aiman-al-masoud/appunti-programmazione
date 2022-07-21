#
# Le eccezioni possono anche essere sollevante.
#
# Questo permette di delegare la gestione della situazione anomala
# ad altre parti del programma, non necessariamente la posizione
# da dove è scaturita l'anomalia.
#

from random import choice


def servizio_web1(x=""):

    """
    Questa è una funzione non interagisce con l'utente
    """

    connessione = choice([True, False])
    if not connessione:
        raise ConnectionError(choice([400, 500 ]))


# idem
servizio_web2 = servizio_web1


def main():

    """
    L'utente interagisce con questa funzione.
    """

    try:
        x = servizio_web1()
        y = servizio_web2(x)
        # ...
    except ConnectionError as e:
        print("Siamo spiacenti, si è verificato un errore:", e, ", riconnettersi e riprovare!")
        exit()


# 
if __name__ == "__main__":
    main()

