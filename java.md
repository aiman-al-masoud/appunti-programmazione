<!-- https://it.wikipedia.org/wiki/Programmazione_orientata_agli_oggetti -->

# Programmazione Orientata Agli Oggetti
(Object Oriented Programming, OOP) è un paradigma di programmazione che permette di definire oggetti software in grado di interagire gli uni con gli altri attraverso lo scambio di messaggi. Un oggetto comprende sia dati (attributi) che istruzioni (metodi).

## Cenni Storici 
Il primo linguaggio di programmazione orientato agli oggetti fu il Simula (1967), seguito negli anni settanta da Smalltalk. L'Orietamento agli Oggetti diventò il paradigma di programmazione dominante negli anni novanta. 

## Classi e Oggetti

Una classe è il modello ("blueprint") con qui verranno creati (o "istanziati") degli oggetti. Un oggetto è un'istanza di una data classe, per esempio:

```
Gatto malachia = new Gatto();
Gatto silvestro = new Gatto();
```

`Gatto` è una classe, `malachia` e `silvestro` sono due istanze diverse (due oggetti) della stessa classe.


## Attributi e Metodi

Un **attributo** di un oggetto è un dato che lo caratterizza, un **metodo** invece è una funzione legata all'oggetto. La classe `Gatto`, per esempio, può prevedere gli attributi: `età`, `razza`, `sesso`, e un metodo `calcolaAreaTerritorio()` che usa i suddetti dati per compiere il calcolo e ritornare il valore.

Nelle classi più complesse, gli attributi stessi possono essere a loro volta degli oggetti.


## I Meccanismi dell'OOP

Un linguaggio è detto orientato agli oggetti quando permette di implementare, usando la sintassi nativa del linguagio, i tre meccanismi di:

## 1 Incapsulamento 
La netta separazione fra **interfaccia** e **implementazione**. Gli oggetti sono come delle scatole nere, dall'esterno non si ha accesso ai dettagli implementativi. Questo aggiunge flessibilità e modularità: meno gli oggetti si conoscono fra loro, più è facile scambiarne le implementazioni.

*es: voglio **debuggare** un programma che dovrebbe ottenere dei dati remoti dal web, ma non voglio sprecare banda inutilmente durante i test. Allora, posso implementare la stessa interfaccia "ClientWeb" in due modi diversi. Una sarà l'implementazione che si connette effettivamente al servizio esterno, e la useranno gli utenti del prodotto finale. Un'altra sarà usata a scopo di testing, e pescherà i dati da un file in locale, o li genererà in modo casuale. Per il resto del programma, i "ClientWeb" sono una scatola nera!*


## 2 Ereditarietà
Permette di estendere le funzionalità delle classi definendo delle sottoclassi.

*es: se ho già la classe `Felino` che ha il metodo `salta()`, non voglio dover ri-scrivere il codice (duplicandolo) quando definisco la classe `Gatto`. Posso allora estendere la classe `Felino`, ereditando il codice già pronto.*

## 3 Polimorfismo
Due oggetti di tipo diverso possono avere un'interfaccia in comune. Chi li chiama dall'esterno può non vedere la differenza, ma gli oggetti si comporteranno comunque in modo leggermente diverso. 

*es: ho due tipi di prodotti diversi nell'inventario, che richiedono due formule diverse per il calcolo del loro prezzo. Posso creare due classi che implementano la stessa interfaccia "Acquistabile", con un metodo calcolaPrezzo(). La Cassa che farà la sommatoria dei prezzi per arrivare al totale, non sa che ciascun tipo di prodotto calcola internamente in modo diverso il proprio prezzo.* 


## ***Generalmente***, gli ogetti devono avere

### Alta Coesione: 
una classe ha un compito ben preciso, fa solo un certo tipo di cose correlate, e non troppe! "Separation of concerns", non vogliamo che la macchinetta del caffè abbia anche la funzionalità "contatta presidente degli Stati Uniti".

### Basso Accoppiamento: 
gli oggetti appunto si conoscono il meno possibile, questo per garantire sostituibilità di un implementazione con un'altra, e quindi buona modularità e manutenibilità.

# Java 

<!-- https://it.wikipedia.org/wiki/Java_(linguaggio_di_programmazione) -->

Java è un linguaggio di programmazione ad **alto livello**, **orientato agli oggetti** e a **tipizzazione statica**, che si appoggia sull'omonima piattaforma software di esecuzione, specificamente progettato per essere **il più possibile indipendente dalla piattaforma hardware di esecuzione** (tramite compilazione in **bytecode** prima e interpretazione poi da parte di una JVM).

## Java Virtual Machine (JVM) 

Il codice in linguaggio Java viene compilato in così detto 'bytecode', che non è altro che un tipo di codice macchina (zeri e uni), ma non per una macchina fisica, bensì per la Macchina Virtuale Java (JVM). La JVM, che dev'essere installata sul computer che esegue il bytecode, converte quest'ultimo in codice macchina "vero e proprio" (nativo), per esempio in codice macchina x86, se si sta eseguendo il programma su un tipico PC. 

Il vantaggio di questo schema, è che il programmatore può scrivere il codice una volta, compilarlo in bytecode, e distribuirlo. Gli utenti possono trovarsi su svariate piattaforme (Windows, Mac, Linux ...) e il programma funzionerà comunque, a patto che la JVM sia correttamente installata su tutti i dispositivi. 

Oggigiorno, esistono addirittura svariati altri linguaggi oltre a Java che possono eseguire sulla JVM. Questo è reso possibile proprio grazie al fatto che la JVM ragiona in termini di bytecode. Basta dunque scrivere un compilatore che converta codice di alto livello in bytecode, e qualsiasi nuovo linguaggio può essere integrato nell'ambiente Java. Esempi di linguaggi che fanno proprio questo sono: Kotlin (il nuovo linguaggio di scelta per programmare su Android), Scala (il linguaggio di Spark), Clojure (un linguaggio funzionale, dialetto del famoso Lisp) ecc...

# Ciao Mondo!

```
public class Main{

    public static void main(String[] args){
        System.out.println("Ciao mondo!");
    }

}
```





