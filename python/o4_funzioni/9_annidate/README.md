# Funzioni Annidate

Si possono annidare funzioni dentro ad altre funzioni. Le annidate saranno visibili solo all'interno della funzione "madre".

```python
def outer():
    def inner():
        pass

outer()
inner() # NameError: name 'inner' is not defined
```

1. [Ritornare Funzioni](./1_ritornare_funzioni.md)
1. [Closures](./2_closures.md)

