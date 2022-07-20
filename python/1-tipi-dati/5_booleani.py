# Booleani
#
# Vero o falso.
#
#


x = True
y = False

if x:
    print("condizione soddisfatta")


# AND

x and y 


# OR

x or y

# XOR

x != y


# FALSY AND TRUTHY VALUES

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


# SHORTCIRCUITING

# catena di or non esegue tutta, ma si ferma non appena trova un 
# valore truthy:
x = False or None or 0 or 2 or 1
print(x) # 2


# catena di and si ferma non appena trova un valore falsy

x = True and 1 and "ciao" and 0 and None 
print(x) # 0