# Passaggio By value vs By reference 

## By value (Per valore): 
La funzione riceve una **copia** dell'oggetto che le si passa. 

Utile per garantire l'assenza di [effetti collaterali](../1_scope/3_scrittura_globali.md#effetti-collaterali), e semplificare il debugging e ragionamento sulle funzioni.

## By reference (Per riferimento): 
La funzione riceve un riferimento all'oggetto **originale** che le si passa, e lo può modificare. 

Utile per condividere/aggiornare dati comuni, e per risparmiare spazio in memoria.


## By Assignment

Con Python si possono emulare ambo le modalità di passaggio valori, ufficialmente Python si dice un linguaggio "pass by assignment". [[1]](https://realpython.com/python-pass-by-reference/) [[2]](https://stackoverflow.com/questions/50534394/what-does-it-mean-by-passed-by-assignment)


## 1) Riassegnamento dentro Funzione

Riassegnare (con `=`) una variabile argomento funzionera sullo scope locale, non cambia mai la globale:

```python
x = "vecchio"

def foo(x):
    x = "nuovo"

foo(x)
x # 'vecchio'
```

## 2) Modifica attributi di Oggetto


Però, se si modifica il contenuto di un oggetto passato come argomento, (**senza riassegnare** la variabile), si sta proprio modificando l'originale globale:


```python
li = [1,2]

def bar(li):

    # chiamata metodo modifica l'originale.
    li.append(3)
    
    # questo no, perché chiaramente riassegnamento.
    li = li + [4] 
   

bar(li)
li # [1, 2, 3]
```


Questo funziona se e solo se il tipo dell'argomento è mutabile.



 <!-- # li+=[4] # strano comportamento dovuto a __iadd__() https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists -->


## 3) Oggetti Immutabili

Invece, gli oggetti immutabili (numeri, stringhe, tuple) non possono mutare le loro proprietà, né nelle funzioni, né da nessun'altra parte:

```python
y = 1

def foobar(y):
    y.imag = 1

foobar() # AttributeError: attribute 'imag' of 'int' objects is not writable
```
