# Return

La keyword `return` è usata per uscire da una funzione e restituire il controllo al blocco di codice che l'aveva invocata, opzionalmente ritornando uno o più valori.


In Python una funzione senza un return esplicito, o con un return vuoto, è implicito che ritorna `None`.

```python
def func():
    pass 
    # return None

x = func()
x # None
```

## Terminare

Una funzione può usare return vuto per terminare l'esecuzione


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



