#
# In Python una funzione senza un return esplicito,
# o con un return vuoto ritorna None.
#
#

def func():
    pass # return 

#
# Una funzione può ritornare qualsiasi numero di valori!
#

def get_web_source():
    html = "<h1></h1>"
    css = "h1{ color: red; }"
    js = "alert('hello world!')"
    return html, css, js

h, c, j = get_web_source()


print(h, c, j)
