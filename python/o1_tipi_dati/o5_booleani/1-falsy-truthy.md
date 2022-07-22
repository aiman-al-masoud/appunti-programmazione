# Truthy and Falsy Values

Abbiamo già visto che `bool` è una sottoclasse di `int`, e che `False` corrisponde ad uno `0`. 

x = 0
# x = 1
# x = ""
# x = "ciao"
# x = {}
# x = {"a":1}
# x = []
# x = [""]

if x:
    print(f"x={x} è truthy")
else:
    print(f"x={x} è falsy")
