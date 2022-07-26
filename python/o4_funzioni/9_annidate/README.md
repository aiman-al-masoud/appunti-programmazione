# Funzioni Annidate


#
# Si possono annidare funzioni dentro ad altre
# funzioni.
#
#
#

def outer():
    def inner():
        pass

outer()


# 
# Tecnica che si può usare per creare e ritornare
# nuove funzioni
#

def get_finder(regex):

    def finder(text):
        import re
        return re.findall(regex, text)

    return finder

f = get_finder(r"\d+")

print(f("3 4"))


#
# Closures ... 
#


