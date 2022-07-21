# F-strings

Schemi fissi, ma valori che cambiano spesso? Niente paura, per creare stringhe **template** (aka: formattate) ci sono diversi modi. Uno di questi:

```python
from datetime import datetime
oggi = datetime.today()
s = f"Oggi è il {oggi.day}/{oggi.month}/{oggi.year}"
```