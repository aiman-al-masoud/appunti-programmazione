È una no-op, non fa niente. La keyword serve dato che in Python l'indentazione è sintattica e richiede almeno una riga di codice nel blocco.

È spesso usata come un segnaposto per le funzioni o blocchi da implementare.

```python
def funzione():

    """
    NB: anche se non fa niente, questa funzione 
    ritorna comunque None.
    """
    pass
```

Nei linguaggi C-like basta lasciare il corpo vuoto.

```c
void funzione(){
 /* do nothing */
}
```
