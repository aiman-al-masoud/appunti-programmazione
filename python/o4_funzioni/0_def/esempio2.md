
# funzione che prende un argomento e ritorna un valore.
def fib(n):
    
    """
    Implementazione ricorsiva di fibonacci
    """

    if n in [0, 1]:
        return 1
    
    if n == 2:
        return 2

    # è 'ricorsiva' perché chiama sé stessa:
    if n > 2:
        return fib(n-2) + fib(n-1)


print([fib(n) for n in range(10)])


print(fib(-1)) # che succede?