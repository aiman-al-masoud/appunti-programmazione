# F-STRINGS

from datetime import datetime
oggi = datetime.today()
s=f"Oggi è il {oggi.day}/{oggi.month}/{oggi.year}"
print(s)
