# Eccezioni 

Un’eccezione è un evento anomalo che provoca l’interruzione del normale flusso d'esecuzione di un programma

Se un'eccezione non viene catturata, il programma uscira dall'attuale blocco di codice, verso quello esterno. Se non viene catturata in nessun blocco di codice esterno, l'eccezione finirà per uscire il programma con un errore.


Se sospettiamo che del codice lancerà un'eccezione, possiamo gestirla tramite un try-except:

```python
try: # viene eseguito tutto solo se non solleva eccezioni
    1/0
except Exception as e: #viene eseguito solo in caso di eccezione
    print(e, type(e))
```

Vediamo un altro esempio con un tipo diverso di eccezione, 
specificamente catturato:

```python
duck = {}
try:
    duck.quack()
except AttributeError as e: # cattura solo eccezioni AttributeError
    print(e, type(e))
except Exception as e: # tutte le altre eccezioni
    print(e, type(e))
```


Non specificare il tipo di eccezione che si cattura nella clausola Except è una pratica sconsigliata, rischia di nascondere gli errori più che gestirli.




<!-- 
TODO: mettilo nel capitolo delle classi
# 
# Duck Typing: come altri linguaggi di scripting, Python esegue un metodo
# su un oggetto "se ne trova uno con lo stesso nome". Se invece quel nome 
# non viene trovato su un dato oggetto, viene sollevata un'eccezione 
# in runtime, al momento della chiamata, e non prima.
# 
# "If it looks like a duck, and it quacks like a duck, it's a duck".
#
#

 -->
