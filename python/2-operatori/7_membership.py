#
# Viene usato per verificare l'appartenenza 
# di un oggetto ad un altro, o ad un "insieme".
#
#

18 in [1, 4, 0, 18, 3] # True

"dica" in "abdicazione" # True

"gatto" in {"gatto":"miao", "cane":"bau"} # True


# Si può overridare implementando il metodo speciale
# __contains__() di una nuova classe.

class Foresta:
    def __contains__(self, o):
        return o in ["cinghiale", "gufo", "lince"]

f = Foresta()
"cinghiale" in f # True
"leone" in f # False


