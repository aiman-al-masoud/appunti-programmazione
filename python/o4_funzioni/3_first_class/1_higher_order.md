# Funzioni di Ordine Superiore


Le [funzioni di ordine superiore](https://it.wikipedia.org/wiki/Funzione_di_ordine_superiore)(higher order functions) sono funzioni che prendono come argomento altre funzioni, o ritornano altre funzioni.

[`saluta()` nell'esempio precedente ](./README.md) è una funzione di ordine superiore, perché prende come argomento un'altra funzione.


## Funzioni Famose

Alcuni esempi paradigmatici di funzioni di ordine superiore sono:

## `map()`

Prende un iterabile e una funzione, applica la funzione a ciascun elemento dell'ierabile e ritorna una nuova copia di esso.


## `filter()`

Prende un iterabile e una funzione, usa la funzione come test per tenere o buttare via un elemento dell'iterabile, e ritorna una nuova copia potenzialmente accorciata.

## `reduce()`

Prende una funzione, un iterabile e, opzionalmente, un valore iniziale. Applica la funzione, in ordine, a due elementi contigui dell'iterabile, aggregandoli nell'accumulatore, opzionalmente inizializzato dal valore iniziale. Ritorna l'aggregato finale.

### Generatori
In Python `map()` e `filter()` chiamati su una lista non ritornano direttamente un'altra lista, ma un generatore. Per questo bisogna convertirlo usando `list()`.