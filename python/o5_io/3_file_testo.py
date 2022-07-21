#
#
#
#

path = __file__
f = open(path, "r")
s = f.read()
f.close()
print(s)

# modo più sicuro, senza dover chiamare close():
with open(path, "r") as f:
    print(f.read())





# import json

# json.loads(s)


# import csv
# csv.reader()





