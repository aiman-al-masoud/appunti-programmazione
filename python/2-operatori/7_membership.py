#
# Viene usato per verificare l'appartenenza 
# di un oggetto ad un altro, o ad un "insieme".
#
#

18 in [1, 4, 0, 18, 3] # True

"dica" in "abdicazione" # True

"gatto" in {"gatto":"miao", "cane":"bau"} # True


class Foresta:
    def __init__(self):
        self.l = ["cinghiale", "gufo", "lince"]

    def __contains__(self, o):
        return o in self.l

f = Foresta()
"cinghiale" in f # True
"leone" in f # False

