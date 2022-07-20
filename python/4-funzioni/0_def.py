# Funzioni
#
# Una funzione è un pezzo di codice riutilizzabile
# che può opzionalmente prendere argomenti, e ritornare 
# valori.
#
#

# funzione che non fa niente, ma ritorna None (default)
def func():
    pass

x = func()
print(x, "")

# funzione che prende un argomento 
# e ritorna un valore.
# è ricorsiva perché chiama sé stessa.
def fib(n):
    
    """
    Implementazione ricorsiva di fibonacci
    """

    if n in [0, 1]:
        return 1
    
    if n == 2:
        return 2

    if n > 2:
        return fib(n-2) + fib(n-1)


print([fib(n) for n in range(10)])
