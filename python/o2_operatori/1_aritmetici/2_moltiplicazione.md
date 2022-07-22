# Moltiplicazione

Fra interi, float e complessi ...

```python
2 * 1.2 # 2.4
```

Ma anche fra interi e stringhe o interi e liste!

```python
"ciao "*10
["ciao"]*10 # molti riferimenti allo STESSO oggetto
```

## Overloading 

Si può overloadare usando il metodo magico `__mul__()`.