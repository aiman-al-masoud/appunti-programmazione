# Modifica Globali da Funzione

Se si prova a **modificare** una variabile globale dall'interno di una funzione, Python crederà che si tratti di una variabile locale non ancora definita:

```python
x = 10

def change_x():
    x+=1 # UnboundLocalError: local variable 'x' referenced before assignment


change_x()
```


Per modificarla dall'interno della funzione, bisogna ricorrere alla keyword `global`:

```python
x = 1

def change_x_ok():
    global x
    x+=1 

change_x_ok()
x # 11
```