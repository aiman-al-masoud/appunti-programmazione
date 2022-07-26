# Return

La keyword `return` è usata per uscire da una funzione e restituire il controllo al blocco di codice che l'aveva invocata, opzionalmente "ritornandogli" uno o più valori.

## Return Implicito

Una funzione senza un return esplicito, o con un return vuoto, ritorna implicitamente `None`. 

Queste si comportano tutte uguali:

### Func 1
```python
def func():
    pass 
```

### Func 2
```python
def func():
    return 
```

### Func 3
```python
def func():
    return None
```

```python
x = func()
x # None
```

L'utilità del return vuoto è di terminare l'esecuzione prima che finisca il codice della funzione, e questa ritorni da sé (come in [Func 1](#func-1)).



## Return di valore

Una funzione può ritornare un valore:

```python
def func():
    return "ciao mondo!"
```





#
# Una funzione può ritornare qualsiasi numero e 
# qualsiasi tipo di valori!
#

def get_web_source(url):
    html = "<h1></h1>"
    css = "h1{ color: red; }"
    js = "alert('hello world!')"
    return html, css, js

# i valori vengono ritornati come una tupla
t = get_web_source("www.google.com")
print(t, type(t))

# ma si possono "spacchettare" usando questa comoda sintassi:
h, c, j = get_web_source("www.google.com")
print(h, c, j)



