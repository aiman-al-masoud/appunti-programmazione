# Raise

Le eccezioni possono anche essere sollevante (raised):

```python
raise Exception("bye bye mondo!") # Exception: bye bye mondo!
```

Questo permette di delegare la gestione della situazione anomala ad altre parti del programma, non necessariamente la posizione da dove è scaturita l'anomalia.

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
        print(f"Si è verificato l'errore: {str(e)}")

    # fai qualcosa ...

```

