#
# In Python una funzione senza un return esplicito,
# o con un return vuoto ritorna None.
#
#

def func():
    pass # return 

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
t = get_web_source()
print(t, type(t))

# ma si possono "spacchettare" usando questa comoda sintassi:
h, c, j = get_web_source()
print(h, c, j)



