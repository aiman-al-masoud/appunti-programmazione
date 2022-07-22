# Shortcircuting

Cosa succede se si concatenana una sfilza di valori booleani (o falsy/truthy) tramite gli operatori `and` o `or`?

# catena di or non esegue tutta, ma si ferma non appena trova un 
# valore truthy:
x = False or None or 0 or 2 or 1
print(x) # 2


# catena di and si ferma non appena trova un valore falsy

x = True and 1 and "ciao" and 0 and None 
print(x) # 0


# all()
# any()

