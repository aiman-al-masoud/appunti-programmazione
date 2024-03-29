# Truthy & Falsy 

Abbiamo già visto che `bool` è una sottoclasse di `int`, e che `False` corrisponde ad uno `0` "speciale". Ma ci accorgiamo che anche lo `0` "normale" ha valore `False` se inserito in un if, o trattato alla stregua di un booleano:

```python
if 0:
    print("non stampo mai")
```
Si dice che lo zero è **falsy**. Tutti gli altri numeri invece, non soltanto l'`1`, hanno valore `True`, e si dice che sono **truthy**. Questa proprietà di fungere da valore booleano all'occorrenza non è esclusiva ai numeri, ma è pervasiva. Per esempio, la lista vuota è falsy, le liste con almeno un elemento sono truthy, e così via. Qui c'è un breve elenco di valori da sperimentare:


```python
x = 0
# x = 1
# x = 999999
# x = ""
# x = "ciao"
# x = {}
# x = {"a":1}
# x = []
# x = [""]
# x = None

if x:
    print(f"x={x} è truthy!")
else:
    print(f"x={x} è falsy!")
```