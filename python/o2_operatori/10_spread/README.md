# Unpacking/Spread

Per svolgere lo 'spacchettamento' (unpacking) di un **tipo iterabile**
(lista, dizionario, insieme, tupla ...). 

**Spacchettamento** vuol dire: poter usare gli elementi dell'iterabile come argomenti di una funzione, oppure al posto dei literals quando si crea una nuova lista, dizionario etc...

## Lista

```python
l = [1,2,3]
l = [*l, 4, 5, 6]
```

### Usare elementi lista come argomenti

```python
def tre_arg(a,b,c):
    return a+b+c

tre_arg(*[1,2,3]) # 6
```

## Dizionario

```python
d = {"gatto":"miao", "cane":"bau"}
d = {**d, "tigre":"ciuff"}
```



https://how.wtf/spread-operator-in-python.html