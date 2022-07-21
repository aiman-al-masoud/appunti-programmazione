#
# Finally
# La clausola finally viene eseguita sempre e comunque (sia in caso
# di errore che non), e potrebbe servire per chiudere una risorsa 
# aperta in precedenza, cosa che si può fare anche nell'except, 
# o automaticamente in alcuni casi col with statement.
#
# Else
# La clausola else dopo except contiene codice da eseguire solo
# se è andato tutto bene e non ci sono state eccezioni (potrebbe anche 
# stare direttamente nel try). 
#
#

x = int(input())

try:
    1/x
except:
    print("eccezione!")
else:
    print("tutto bene!")
finally:
    print("finally...")


