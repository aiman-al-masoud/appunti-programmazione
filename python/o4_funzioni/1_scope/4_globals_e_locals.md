# Le builtin `globals()` e `locals()`

`globals()`: ritorna un dizionario di nomi-oggetti nello scope globale.

`locals()`: (chiamata dall'interno di una funzione f) ritorna un dizionario di nomi-oggetti nello scope locale (della funzione f).


Se chiamati entrambi a livello di modulo: `globals() == locals()`

