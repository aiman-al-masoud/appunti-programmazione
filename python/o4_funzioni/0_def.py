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


# funzione che ritorna il doppio dell'argomento.
def per_due(n):
    return 2*n 


print(per_due(10))
print(per_due("ciao ")) # che succede qui?


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