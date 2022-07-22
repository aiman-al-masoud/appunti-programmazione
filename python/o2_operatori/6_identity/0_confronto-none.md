# Confronto con None

usa sempre (`is`) per controllare che un oggetto sia non-definito (`None`).

```python
x = None 
x is None # Ok 
x == None # NON FARLO!
```

## Motivo

Come abbiamo accennato, `==` è implementato da un metodo speciale. Potrebbe essere che la logica di questo metodo provi ad accedere agli attributi di `None`, provocando un'eccezione in runtime perché None non ha attributi.

class Persona:
    def __init__(self, nome):
        self.nome = nome 
    
    def __eq__(self, o):
        return self.nome == o.nome

p = Persona("Mario")
p == None # AttributeError: 'NoneType' object has no attribute 'nome'