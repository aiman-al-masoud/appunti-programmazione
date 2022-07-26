# For

## Per iterare su una lista

```python
for i in [1,2,3]:
    print(i)
```

## Per iterare su una stringa
```python
for c in "ciao mondo!":
    print(c)
```
## Per iterare su una lista, con indice

```python
for i, val in enumerate(["un", "due", "tre"]):
    print(i, val)
```

## Per iterare su una "lista di tuple"
```python
d = {"gatto":"miao", "cane":"bau"}
for key, val in d.items():
    print(key, val)
```

## Per emulare il for tradizionale del C:
```python
for i in range(0, 10): # for(i=0;i<10;i++)
    print(i)
```

## Più in generale:
```python
start=0  # default=0 
stop=10 # param obbligatorio
step=1   # default=1
for i in range(start, stop, step):
    print(i)
```

## Loop vs List Comprehension

spesso conviene sostituire il for con una list comprehension, eg:

```python
l = [1,2,3,4] # vorrei moltiplicare per 2 ciascun elemento
```
# modo tradizionale:

```python
for i in range(len(l)):
    l[i] *= 2
```

# molto meglio:
```python
l = [2*x for x in l]
```
