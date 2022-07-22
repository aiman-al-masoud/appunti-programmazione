# Modulo

Per calcolare `a % b`, si sottrae `b` da `x=a` fino a quando `x` non diventa minore di `b`.

```python
10%9 # 1
11%9 # 2
18%9 # 0
19%9 # 1
```


Esempio `19 % 9`:

```
x = 19
x = x - 9 # x è 10 > 9
x = x - 9  # x è 1 < 9
risultato = x = 1
```


## Overloading 

`__mod__()`