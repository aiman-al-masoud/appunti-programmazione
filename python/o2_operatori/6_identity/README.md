# Identità

**Identità != Uguaglianza.**

**Uguaglianza** (`==`) vuol dire solo che due oggetti hanno
proprietà **equivalenti**.

**Identità** (`is`) fra due variabili vuol dire che puntano
allo **stesso** oggetto in memoria, è una condizione più forte.


L'identità implica l'uguaglianza ovviamente, perché un oggetto è equivalente a se stesso. Ma non vale il viceversa.


```python
x = {"gatto":"miao"}
y = x

x is y # True

x = {"gatto":"miao"}
y = {"gatto":"miao"}

x is y # False
x == y # True
```

## Sul confronto con `None`

vai qui: [confronto con None](./0_confronto-none.md#confronto-con-none).