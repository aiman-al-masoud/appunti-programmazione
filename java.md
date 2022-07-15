<!-- https://it.wikipedia.org/wiki/Programmazione_orientata_agli_oggetti -->

# Programmazione Orientata Agli Oggetti
(Object Oriented Programming, OOP) è un paradigma di programmazione che permette di definire oggetti software in grado di interagire gli uni con gli altri attraverso lo scambio di messaggi. Un oggetto comprende sia dati (attributi) che istruzioni (metodi).

## Cenni Storici 
Il primo linguaggio di programmazione orientato agli oggetti fu il Simula (1967), seguito negli anni settanta da Smalltalk. L'Orietamento agli Oggetti diventò il paradigma di programmazione dominante negli anni novanta. 

## Classi e Oggetti

Una classe è il modello ("blueprint") con qui verranno creati (o "istanziati") degli oggetti. Un oggetto è un'istanza di una data classe, per esempio:

```java 
Gatto malachia = new Gatto();
Gatto silvestro = new Gatto();
```

`Gatto` è una classe, `malachia` e `silvestro` sono due istanze diverse (due oggetti) della stessa classe.


## Attributi e Metodi

Un **attributo** di un oggetto è un dato che lo caratterizza, un **metodo** invece è una funzione legata all'oggetto. La classe `Gatto`, per esempio, può prevedere gli attributi: `età`, `razza`, `sesso`, e un metodo `calcolaAreaTerritorio()` che usa i suddetti dati per compiere il calcolo e ritornare il valore.

Nelle classi più complesse, gli attributi stessi possono essere a loro volta degli oggetti.


<span id="I Meccanismi dell'OOP">

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

<span id="Basso Accoppiamento">

### Basso Accoppiamento: 
gli oggetti appunto si conoscono il meno possibile, questo per garantire sostituibilità di un implementazione con un'altra, e quindi buona modularità e manutenibilità.

# Java 

<!-- https://it.wikipedia.org/wiki/Java_(linguaggio_di_programmazione) -->

Java è un linguaggio di programmazione ad **alto livello**, **orientato agli oggetti** e a **tipizzazione statica**, che si appoggia sull'omonima piattaforma software di esecuzione, specificamente progettato per essere il più possibile indipendente dalla piattaforma hardware di esecuzione (tramite compilazione in **bytecode** prima e interpretazione poi da parte di una JVM).

Decifriamo un attimo i termini "gergali" in grassetto. 

* Alto livello: vuol dire semplicemente che è più comodo da usare che un linguaggio di più basso livello (per esempio assembly).
* Orientato agli Oggetti: vedi <a href="#I Meccanismi dell'OOP">I Meccanismi dell'OOP</a> 
* Tipizzazione Statica: vuol dire che una volta dicharata la variabile `x` di un certo tipo (per esempio `int`), è proibito riassegnarla con un valore di tipo diverso (per esempio `float`, `double` ecc...).

```java
int x = 1; // x è un int per sempre!
x = 2.1; // errore! errore! il compilatore si lamenta!
```

* Bytecode vedi <a href="#Java Virtual Machine (JVM)">Java Virtual Machine (JVM) </a>

<span id="Java Virtual Machine (JVM)">

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

## Spiegazione:

In Java, anche per il più semplice dei programmi, è necessario creare una classe (`Main`, in questo caso). La classe è pubblica (`public`), cioè visibile anche al di fuori del package dov'è definita (vedremo cosa vuol dire).

All'interno di questa classe, è presente il metodo speciale `main()`, il nome è importante. Questo metodo viene usato da Java come punto d'ingresso (entry point) al programma. Questo metodo è:

* pubblico `public`: visibile anche al di fuori della sua classe.

* statico `static`: legato alla classe, e non ad una sua istanza (vedremo meglio cosa vuol dire).

* void `void`: non ritorna alcun valore. È più simile ad una procedura che ad una funzione.

* prende `String[] args` come unico argomento. Questo è un array di stringhe, che rappresenta i parametri da linea di comando, quando si esegue il programma da una shell. Il primo elemento dell'array (`args[0]`) è il nome del programma.

All'interno del metodo `main()`, usiamo il metodo `println()` per stampare una stringa e andare a capo. 

*NB: Il metodo `println()` è un metodo statico, contenuto nell'oggetto `out`, a sua volta contenuto come attributo statico nella classe `System`. Di solito quando un metodo è molto generico e non ha bisogno di accedere allo stato di un oggetto particolare (come `println()` appunto), viene comodo dichiararlo come metodo statico di una classe, dato che in Java non esistono le funzioni.*


## Parametri "formali" vs "attuali"
I parametri formali di un metodo si riferiscono alla sua definizione, per esempio `println()` è definito sulle stringhe. I parametri attuali sono quelli passati al metodo durante una chiamata (per esempio la stringa particolare "Ciao Mondo!").


## Signature ("Firma") di un metodo
è rappresentata dal:
* nome
* valore di ritorno
* parametri formali
Non si possono avere due metodi con la stessa identica firma in una classe, altrimenti ci sarebbe un'ambiguità.

# Tipi Primitivi

In Java tutto è un oggetto... tranne i tipi primitivi! I tipi primitivi sono dei semplici valori, non hanno né attributi né metodi, e non possono avere `null` come valore. I tipi primitivi sono:

* int, long, short, byte
* float, double
* char 
* boolean

*NB: come in C, un char è circondato da apici singoli. `'a'` è un char e quindi un tipo primitivo, `"a"` è invece una stringa e quindi un oggetto.*

# Passaggio Parametri: "by value" vs "by reference"

In generale, una variabile è un puntatore ad una certa area della memoria RAM (nella cosiddetta regione di memoria "heap").

## Per passaggio "by value" (per valore) 
si intende che il metodo riceve una copia della variabile passata come argomento, e quindi, caschi il mondo, non modificherà mai l'originale.

## Per passaggio "by reference" (per riferimento) 
si intende invece che la variabile ricevuta dal metodo, punta proprio alla stessa area di memoria della variabile originale. 


In Java, una variabile di tipo primitivo è sempre e comunque passata by value. Per gli oggetti, invece, la cosa si complica un pochettino. La variabile oggetto non può essere riassegnata del tutto, ma l'istanza originale può eccome essere modificata. Vediamo meglio con degli esempi (in pseudo-codice):


## 1. Con Tipo Primitivo (int)

```java
// dentro la mia classe 'Oggetto'
void metodo(int x){
    x = 2; // questo modifica solo la x locale
    x+=1; // anche questo modifica solo la x locale
    // qui dentro x locale vale 3.
}

/* ... */

// dentro al main
int x = 1; // variabile globale
oggetto.metodo(x); // chiamo il metodo

// qua fuori x globale è rimasta = 1
```



## 2. Riassegno var Oggetto


```java

// dentro la mia classe 'Oggetto'
void metodo(ClasseArgomento arg){
    // questo riassegna solo la variabile locale
    arg = new ClasseArgomento("secondo");
}

/* ... */

// dentro al main
Argomento arg = new ClasseArgomento("primo");
oggetto.metodo(arg);

arg.chiSonoIo(); //sono il primo!

```

## 3. Modifico var Oggetto


```java

// dentro la mia classe 'Oggetto'
void metodo(ClasseArgomento arg){
    // questo invece può modificare l'originale!
    arg.setNome("MODIFICATO");
}

/* ... */

// dentro al main
ClasseArgomento arg = new ClasseArgomento("primo");
oggetto.metodo(arg);

arg.chiSonoIo(); //sono il MODIFICATO!

```


# Dichiariamo una classe

Ok, proviamo ora a creare una nuova classe partendo da zero.

La prima cosa da fare è creare un nuovo file di testo .java, e dichiarare una classe pubblica in questo modo che abbiamo già visto:

```java 
public class Persona{


}
```

Possiamo già così nel nostro `main()` creare nuovi oggetti di tipo `Persona`:

```java 
import Persona;

public class Main{

    public static void main(String[] args){

    Persona b1 = new Persona();
    Persona b2 = new Persona();
}
}
```

Constatiamo che i due oggetti puntano a due aree distinte della memoria, utilizzando l'operatore `==`, che sugli oggetti funziona come "operatore di identità". 

```java
b1 == b2; //false
```

`b1` e `b2` sono due riferimenti a due oggetti diversi in memoria. Ma posso sempre riassegnarne uno così:

```java 
b1 = b2;
```
Ora i riferimenti b1 e b2 puntano alla stessa area di memoria! Cioè il secondo oggetto `Persona` che avevamo creato, pertanto:

```java
b1==b2; //true
```

Il primo oggetto che avevamo creato (quello che prima era puntato da `b1`), si dice "uscito dallo scope", dato che nessuna variabile punta più ad esso. Il **Garbage Collector** di Java sarà dunque autorizzato a rimuovere questo oggetto dalla memoria il prima possibile, per risparmiare risorse, dato che oramai è un peso inutile.


Ma torniamo alla nostra classe `Persona`, e proviamo a renderla un po' più utile:


```java 
public class Persona{

    private String nome;
    private int eta;
    private boolean sesso;

    /**
    * Questo è un costruttore (constructor).
    */
    public Persona(String nome, int eta, boolean sesso){
        this.nome = nome;
        this.eta = eta;
        this.sesso = sesso;   
    }

}
```


Abbiamo aggiunto 3 attributi dichiarati come privati (`private`), ed un costruttore publico.

## Costruttore
è un metodo speciale, che crea ed inizializza una nuova istanza di una classe. Da notare che il nome del costruttore deve essere uguale a quello della classe. Il costruttore si può poi invocare altrove nel modo in cui abbiamo già visto, con la parola chiave `new`:

```java 
Persona p = new Persona("Pinko", 33, true);
```

Anche prima stavamo usando un costruttore, ma senza nessun argomento. Quello era il costruttore di default, che Java inserice automaticamente se noi non facciamo niente. Adesso non risulta più possibile usarlo. Però possiamo sempre creare più costruttori, qualora desiderassimo inizializzare in modo diverso una classe.


## Keyword `this`

Il `this` è una parola chiave molto utile che fa riferimento all'istanza di un oggetto dal suo interno. Nel costruttore di sopra, l'abbiamo usata per disambiguare le coppie di variabili con lo stesso nome:

```java 
//...
public Persona(String nome /*ecc...*/ ){
    this.nome = nome;
}
```
Per Java, la variabile `this.nome` fa riferimento all'attributo `private String nome`, mentre `nome` e basta è solo un parametro del costruttore, dato che **le variabili locali nascondono quelle globali**.

Se avessimo scritto:

```java 
nome = nome;
```

Avremmo fatto un'operazione perfettamente ridondante. Ma soprattutto non avremmo inizializzato l'attributo (cosa di cui il compiler ci avrebbe avvertito). 

In alternativa ad usare `this`, potevamo semplicemente dare ad attributo e parametro nomi diversi, es:

```java 
//...
public Persona(String n /*ecc...*/ ){
    nome = n;
}
```

## Modificatori di Visibilità

Gli attributi che abbiamo dichiarato sono tutti `private`, cioè si possono vedere solo dall'interno della classe. Se proviamo a fare altrimenti, il compiler si lamenterà:

```java
// nel main
Persona p = new Persona("Pinko", 33, true);
p.nome = "Pinko Pallino"; //errore! l'attributo "nome" non è visibile dall'esterno!
```

A cosa servono gli attributi se nessuno può vederli? Beh, vengono utilizzati all'interno della classe. Dichiarare attributi privati può aiutare a  <a href="#Basso Accoppiamento">diminuire l'accoppiamento</a> fra le classi. Ovviamente, la classe deve avere qualche altro metodo o attributo che permette di fare uso diretto o indiretto di un membro privato della stessa.

## Getters & Setters

Sono dei metodi che di sovente si usano in Java per ottenere (get) e impostare (set) i valori degli attributi privati dall'esterno di una classe. Ovviamente devono essere metodi pubblici, cioè visibili dall'esterno della classe, eg:

```java 
public class Persona{

    private String nome;
    private int eta;
    private boolean sesso;

    /**
    * Questo è un costruttore (constructor).
    */
    public Persona(String nome, int eta, boolean sesso){
        this.nome = nome;
        this.eta = eta;
        this.sesso = sesso;   
    }

    /**
    * questo è un getter
    */
    public getNome(){
        return nome; //equivalente a this.nome
    }

   /**
    * questo è un setter
    */
    public setNome(String nome){
        return this.nome = nome; 
    }

}
```

La loro utilità sta nel "regolamentare" l'accesso e la modifica degli attributi: se volessimo potremmo controllare che il nome sia valido prima di assegnarlo, per esempio.

Negli IDE (Integrated Development Envinronment) odierni, spesso c'è la possibilità di generare automaticamente i getter e i setter. Per esempio su Eclipse basta fare:

```
click destro > Sorgente > Genera getters e setters
```

Meglio non esagerare però, perché a volte è inutile metterceli. Per esempio se l'attributo serve solo alla logica interna della classe, e non ci si deve accedere mai direttamente da fuori. Oppure se l'attributo è immutabile/costante (`final`), in questo caso getters e setters sono perfettamente inutili, e si potrebbe anche dichiarare l'attributo come `public`, per esempio:


```java 
public class Persona{

    public final String nome;
    public final int eta;
    public final boolean sesso;

    /**
    * Questo è un costruttore (constructor).
    */
    public Persona(String nome, int eta, boolean sesso){
        this.nome = nome;
        this.eta = eta;
        this.sesso = sesso;   
    }

}
```

Ovviamente, ci stiamo auto-imponendo il limite di non poter più cambiare gli attributi di un oggetto una volta inizializzato, che potrebbe non aver senso per tutti gli attributi:

```java
// buon compleanno, Pinko
p.eta += 1; //errore! eta è final!!!!!
```

*Chiaramente, c'è sempre l'opzione di creare ex novo una nuova istanza dell'oggetto immutabile, ogni volta che lo vorremmo mutare.*

Oltre a `public` e `private` esiste anche `protected`. `protected` vuol dire che i membri della classe saranno visibili all'interno dello stesso package, e alle sottoclassi definite ovunque. Infine, se non si dichiara esplicitamente la visibilità di una variabile, essa sarà visibile soltanto all'interno del proprio package.

## Naming Conventions

Le convenzioni di nomenclatura non sono regole sintattiche, ma servono a rendere il codice più familiare e leggibile agli estranei, e a sé stessi del futuro. In Italiano è "lecito" trascurare la punteggiatura e le maiuscole, ma se vogliamo farci capire, è molto meglio usarle. Similmente in Java è meglio seguire queste linee guida:

* Nomi di classi, interfacce ed enum: **PascalCase**
* Nomi di oggetti e metodi: **camelCase**
* Costanti (attributi `final`) e valori di enum: **CONSTANT_CASE**
* Nomi di Package: **lowercase**


# Le Stringhe 

Finora abbiamo intravisto l'utilizzo delle stringhe attraverso gli *string literals*, ovvero la notazione di stringa contenuta fra doppi apici, es:

```java
String s = "ciao mondo!";
```

*NB: in Java, come in C, gli apici singoli sono riservati al **singolo carattere**, per cui 'ciao mondo' dà un errore di compilazione.*

Quando usiamo questa notazione, Java **può** creare un nuovo oggetto di tipo `String`. Non è detto che ne crei uno nuovo, perché se usiamo la stessa stringa più di una volta, quello che ci verrà restituito è un riferimento allo stesso oggetto in memoria. Java infatti mantiene un così detto "pool" di stringhe ricilate.

es:
```java
String s = "ciao mondo!";
String s2 = "ciao mondo!";
s==s2; //true
```

Il confronto con `==` ritorna `true`, il che conferma che `s` ed `s2` puntano allo stesso oggetto in memoria.

Possiamo costringere Java a creare un nuovo oggetto `String`, usando il costruttore esplicitamente:

es:
```java
String s = "ciao mondo!";
String s2 = new String("ciao mondo!");
s==s2; //false
```

In questo caso `s` ed `s2` puntano a due oggetti distinti. Possiamo però svolgere il confronto logico usando il metodo `equals()`, es:

es:
```java
String s = "ciao mondo!";
String s2 = new String("ciao mondo!");
s==s2; //false
s.equals(s2); //true
```

## Concatenazione

Un modo semplice di concatenare le stringhe è attraverso l'operatore `+`, es:

```java 
String s = "ciao" + " mondo";
s; // "ciao mondo"
```

## Lunghezza 

```java 
int l = "ciao".lenght(); //4
```

## Estrarre singolo char

```java 
char c = "ciao".charAt(1); // 'i'
```
## Estrarre Sottostringa 

```java 
String sub = "ciao a tutti".substring(2, 5); // "ao"
```

## Parsing 

esistono diversi metodi standard per convertire le stringhe in valori numerici, un esempio con gli interi:

```java
int x = Integer.parseInt("112"); // 122
```

Va anche detto che le stringhe in Java sono immutabili. Tutte le operazioni che ci si possono svolgere con i metodi (`substring()`, `charAt()` ecc...) non modificano mai l'oggetto originale, ma ne creano uno nuovo (se non c'è già nello String Pool), e ritornano una nuova reference, come mostrato negli esempi.


# L'Ereditarietà in Java

L'ereditarietà permette di riciclare le funzionalità di classi esistenti, usandole come base per creare nuove classi specializzate; per esempio, molti dei metodi e degli attributi della classe `Persona`, potrebbero tornarci utili nel caso decidessimo di creare la classe `Studente`, visto che uno `Studente` è una `Persona` con qualcosa in più. La classe `Studente` si direbbe allora una **sottoclasse** di `Persona`. La classe `Persona`: la **superclasse** di `Studente`. 



Torniamo alla nostra classe `Persona`, definita in questo modo:


```java 
public class Persona{

    protected String nome; 
    protected int eta;
    protected boolean sesso;

    public Persona(String nome, int eta, boolean sesso){
        this.nome = nome;
        this.eta = eta;
        this.sesso = sesso;   
    }

    public String toString(){
        return nome+" ha "+eta+" anni ed è un"+(sesso?" maschio": "a femmina")
    }

    public void festeggiaCompleanno(){
        eta++;
    }
}
```

Abbiamo fatto alcune modifiche, nello specifico:

* Attributi resi `protected`.
* Implementato metodo `toString()` che produce una rappresentazione testuale dell'oggetto.
* Creato il metodo `festeggiaCompleanno()` che aumenta l'età della persona di un anno.


Ora pensiamo al nostro studente, immaginiamo che uno studente abbia bisogno, oltre ai dati di `Persona`, di avere una matricola. Allora potremmo fare così:

```java
public class Studente extends Persona{ // keyword extends

    String matricola;

    /**
    * nuovo costruttore
    */
    public Studente(String nome, int eta, boolean sesso, String matricola){
        super(nome, eta, sesso); // chiamo vecchio costruttore di superclasse
        this.matricola = matricola;
    }
}
```

Cos'è successo? `Studente` ha ereditato tutti i metodi e gli attributi di `Persona`, dato che abbiamo avuto l'accortezza di dichiarali `public` e `protected`. Possiamo usarli **come su un'istanza di `Persona`**:

```java 
Studente stud  = new Studente("Pinko", 20, true, "PNK000");
stud.festeggiaCompleanno() // aumenta eta di uno
stud.toString(); // "Pinko ha 21 anni ed è un maschio"
```

*NB: Studente **non** ha ereditato il costruttore della superclasse, perché ce ne ha fatto definire uno nuovo, col nuovo parametro `matricola`; ma siamo stati in grado di sfruttare quello di `Persona` (usando la keyword `super`), per assegnare `nome`, `eta` e `sesso`, senza dover riscrivere del codice identico.*


## Overriding 

Supponiamo che uno studente non si limiti a festeggiare il suo compleanno aumentando la sua età di un anno, 




## Classcasting 

Ma `stud` **è** proprio un'istanza di `Persona` (oltre ad essere ovviamente un'istanza di `Studente`). Questo vuol dire che possiamo anche *dimenticarci* che `stud` è uno `Studente`, e trattarlo da `Persona` qualunque:

```java
Persona p = stud;
```

Questo si chiama **Upcasting**, ed è sempre valido. Esso consiste nel fare riferimento ad un oggetto di una sottoclasse come se fosse della superclasse. Dopotutto, una formica è anche un insetto, un albero è anche una pianta ecc...

L'operazione inversa invece si chiama **Downcasting**, e consiste nel **provare** a fare riferimento ad un oggetto generale in modo più specifico: 

```java
Studente s = (Studente) p;
```

Se l'oggetto `p` è un'istanza di `Studente` questa conversione funzionerà a dovere. Se no, lancerà un errore (`ClassCastException`), che deve essere gestito in runtime. Non tutte le persone sono studenti, non tutte le piante sono alberi, ecc...







## Ereditarietà Multipla
In Java una classe può ereditare direttamente **da una sola** superclasse, vale a dire che l'ereditarietà multipla è **proibita**. Questo onde evitare situazioni in cui una classe eredita da due superclassi due metodi diversi ma con lo stesso nome e signature, il che sarebbe causa di ambiguità.

Invece, l'ereditarietà concatenata è lecita, per esempio: `Gatto` eredita da `Felino` che eredita a sua volta da `Mammifero` che eredita da `Vertebrato` ecc ... 


Overloding, Overriding, Class casting
















