# Type Casting

Il type casting è la conversione da un tipo di dato ad un altro.

In tanti casi, si può fare affidamento a queste funzioni builtin:

* `int()`
* `float()`
* `str()`
* `dict()`
* `list()`
* `set()`

Per esempio:

## stringa -> int

```python
int("1012") # 1012
```

Oppure con base diversa da 10:

```python
int("0101", 2) # 5
```

## int -> stringa


```python
x = 100
"ho mangiato "+str(x)+" torte" # 'ho mangiato 100 torte'
```


ecc ...