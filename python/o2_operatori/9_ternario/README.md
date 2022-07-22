# Ternario

Si chiama ternario perché prende 3 operandi: una condizione, un valore se la condizione è soddisfatta, e un valore se non lo è.

```python
eta = 25
x = "maggiorenne" if eta >= 18 else "minorenne"
x # 'maggiorenne'
```

Molto meglio che:

```python
eta = 25

if eta >= 18:
    x = "maggiorenne"
else:
    x = "minorenne"

x # 'maggiorenne'
```

## 

# NB: se devi ottenere valori booleani, allora puoi
# semplificare ulteriormente, es:

if eta >= 18:
    x = True
else:
    x = False

# diventa:

x = eta >= 18


