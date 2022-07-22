# Moltiplicazione

Fra interi, float e complessi ...

```python
2 * 1.2 # 2.4
```

Ma anche fra interi e stringhe o interi e liste! 

```python
"ciao "*3 # 'ciao ciao ciao ' 
["ciao"]*3 # ['ciao', 'ciao', 'ciao'] 
```
Gli elementi della lista non vengono copiati, vengono solo creati più riferimenti allo stesso oggetto originale.

## Overloading 

Si può overloadare usando il metodo magico `__mul__()`.