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

## Semplificazione Ulteriore

Se il booleano è il tuo 'capolinea', allora puoi semplificare ulteriormente, es:

```python
if eta >= 18:
    x = True
else:
    x = False
```

Diventa:

```python
x = eta >= 18
```