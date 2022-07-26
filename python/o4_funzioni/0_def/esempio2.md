# Esempio 2: Ricorsività 

Una funzione che implementa un [algoritmo ricorsivo](https://it.wikipedia.org/wiki/Algoritmo_ricorsivo), invoca se stessa più volte con argomenti via via più "semplici". Gli input più "semplici" in assoluto fermano questo processo, ritornando un valore concreto; e si dice che la funzione raggiunge il suo base case. Senza un base case, o condizione di terminazione, la funzione chiamerebbe se stessa così tante volte da intasare lo stack delle chiamate a funzione, provocando in Python un'eccezione di tipo: `RecursionError` con messaggio `maximum recursion depth exceeded`, altresì nota come stack overflow.


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

Spiegazione dell'esecuzione con esempio:

```python
fib(4)
```

La funzione ritorna:

```python
fib(2) + fib(3) 
```

```python






```python
print([fib(n) for n in range(10)])
print(fib(-1)) # che succede?
```



<!-- https://stackoverflow.com/questions/310974/what-is-tail-call-optimization -->