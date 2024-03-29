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

*Nota Terminogica: le funzioni che non ritornano niente sono dette **funzioni void**, o **procedure** in altri linguaggi.*


## Return di valore

Una funzione può ritornare un valore:

```python
def func():
    return "ciao mondo!"
```

**Attenzione**, una funzione può ritornare un **tipo diverso** in base agli argomenti o allo stato quando viene chiamata!


```python
def func(n):
    if n ==0:
        return "ciao mondo"

    if n ==1:
        return 100
    
    if n ==2:
        return True


x, y, z = func(0), func(1), func(2)
x # 'ciao mondo'
y # 100
z # True
```


## Return tanti valori

Una funzione può ritornare un numero qualsiasi di valori di qualasiasi tipo!

```python
def get_web_source(url):
    html = "<h1></h1>"
    css = "h1{ color: red; }"
    js = "alert('hello world!')"
    return html, css, js
```

I valori vengono ritornati come una tupla:

```python
t = get_web_source("www.google.com")
type(t) # tuple
```

Ma si possono "spacchettare" usando questa comoda sintassi:

```python
h, c, j = get_web_source("www.google.com")
h # '<h1></h1>'
c # 'h1{ color: red; }'
j # "alert('hello world!')"
```

