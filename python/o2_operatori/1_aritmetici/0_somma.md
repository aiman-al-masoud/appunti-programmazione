# Somma

Somma fra interi, float, complessi:

```python
1 + 4 # 5
1.1 + .2 # 1.3
0+1j + 1 # (1+1j)
```

Ma anche fra stringhe, liste ecc...

```python
"ciao "+"mondo" # 'ciao mondo'
[1,2]+[3,4] # [1, 2, 3, 4]
```

## Overloading 
Si può overloadare usando il metodo magico `__add__()`.