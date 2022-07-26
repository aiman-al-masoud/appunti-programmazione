# Raise

Le eccezioni possono anche essere sollevante (raised):

```python
raise Exception("addio mondo crudele!") # Exception: addio mondo crudele!
```

Questo permette di delegare la gestione della situazione anomala ad altre parti del programma, non necessariamente la posizione da dove è scaturita l'anomalia; che potrebbe non essere un luogo adeguato per risolvere il problema:

```python

def subroutine():
    
    # fai qualcosa ...

    if condizione_anomala:
        raise NonRiescoAGestirlaException(error_code)
    
    # fai qualcosa ...

def main():
    
    # fai qualcosa ...
    
    try:
        subroutine()
    except NonRiescoAGestirlaException as e:
        print(f"Si è verificato l'errore: {str(e)}, cosa vuoi fare?")

    # fai qualcosa ...

```

Per fare un'analogia col cosiddetto "mondo reale", pensiamo alla "issue escalation" in un'azienda;

