# Unpacking/Spread

Per svolgere lo 'spacchettamento' (unpacking) di un **tipo iterabile**
(lista, dizionario, insieme, tupla ...). 

**Spacchettamento** vuol dire: poter usare gli elementi dell'iterabile come argomenti di una funzione, oppure al posto dei literals quando si crea una nuova lista, dizionario ecc...

## Lista

```python
l = [1,2,3]
l = [*l, 4, 5, 6]
l # [1, 2, 3, 4, 5, 6]
```

### Come Argomenti

```python
def tre_arg(a,b,c):
    return a+b+c

tre_arg(*[1,2,3]) # 6
```

## Dizionario

Col dizionario **due** asterischi invece che uno.

```python
d = {"gatto":"miao", "cane":"bau"}
d = {**d, "tigre": "ciuff"}
d # {'gatto': 'miao', 'cane' : 'bau', 'tigre' : 'ciuff'}
```

Sì, le [tigri fanno ciuff](https://www.youtube.com/watch?v=5Ksr0-H1gmI).



