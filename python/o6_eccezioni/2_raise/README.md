# Raise

Le eccezioni possono anche essere sollevate (raised):

```python
raise Exception("addio mondo crudele!") # Exception: addio mondo crudele!
```

Questo permette di delegare la gestione della situazione anomala ad altre parti del programma, dato che la posizione da dove è scaturita l'anomalia spesso non è il luogo adeguato dove risolverla:

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

Per fare un'analogia col cosiddetto "mondo reale", pensiamo alla "issue escalation" in un'azienda; ossia quando un problema (issue) che si scatena ai bassi livelli della gerarchia (semplici impiegati) viene sollevato (escalated) ai vertici più alti dell'azienda (i manager) perché possano loro prendere una decisione sul da farsi.