# Esempio 2: Ricorsività 

Una funzione che implementa un [algoritmo ricorsivo](https://it.wikipedia.org/wiki/Algoritmo_ricorsivo), invoca se stessa più volte con argomenti via via più "semplici". Gli input più "semplici" sono speciali, e provocano la terminazione della funzione, e si dice che la funzione raggiunge il suo base case; senza di esso, la funzione chiamerebbe se stessa così tante volte da intasare lo stack delle chiamate a funzione, provocando un'eccezione di tipo: `RecursionError` con messaggio `maximum recursion depth exceeded`.


```python
def fib(n):
    
    """
    Implementazione ricorsiva di fibonacci
    """

    # base case 1
    if n in [0, 1]:
        return 1
    
    # base case 2
    if n == 2:
        return 2

    # è 'ricorsiva' perché chiama se stessa:
    if n > 2:
        return fib(n-2) + fib(n-1)
```



```python
print([fib(n) for n in range(10)])
print(fib(-1)) # che succede?
```