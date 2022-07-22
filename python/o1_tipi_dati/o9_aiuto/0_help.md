# Help

Sulla python shell, stampa a video la stringa di documentazione della funzione su cui è invocato.

```python
help(funzione)
```

```
Help on function funzione in module __main__:

funzione()
    Questa funzione serve a bla bla bla ...
(END)
```

Per uscire da questa visualizzazione premere il tasto Q (per **Q**uit).


## Con ipython

In alternativa, se stiamo usando la ipython shell, possiamo stampare la stringa di documentazione semplicemente postponendo un punto interrogativo al nome della funzione:

```python
funzione?
```
In questo caso non dobbiamo nemmeno quittare con Q.


## Documentazione

Le funzioni builtin e standard sono già ben documentate, ma se vogliamo ottenere lo stesso effetto per quelle che scriviamo noi, ci dobbiamo servire delle stringhe di documentazione, per esempio la funzione di sopra poteva essere definita così:

```python
def funzione():
    
    """
    Questa funzione serve a bla bla bla ...
    """
    # codice ...
```