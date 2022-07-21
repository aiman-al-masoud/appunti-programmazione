# Escape Chars

Caratteri speciali, da trattare con cautela. Per esempio: gli **apici**, che servono a creare le stringhe; non possono essere usati così come capita all'interno di una stringa, o confondono l'interprete circa la fine della medesima. Bisogna precederli da una **backslash**:

```python
s = 'ho detto: \'ciao mondo!\''
```

Oppure usare apici misti:

```python
s = "ho detto 'ciao mondo!'"
```

Oppure questa sintassi, se si vogliono usare sia apici singoli che doppi:

```python
s = '''
    Ho detto: "ciao!", oppure: 'ciao!'
    '''
```

Invece, per tutti gli atri caratteri speciali, bisogna usare la **backslash**.

Qui una lista di alcuni caratteri speciali comuni:
 	

<table >

<tr><td>\a</td> <td> Alert/bell (suona un alert se stampato!) </td></tr>
<tr><td>\n 	</td> <td> New-line (accapo) </td></tr>
<tr><td>\r</td> <td> Carriage return </td></tr>
<tr><td>\t</td> <td> Horizontal tab </td></tr>
<tr><td>\'</td> <td> Single quotation mark </td></tr>
<tr><td>\"</td> <td> Double quotation mark </td></tr>
<tr><td>\\</td> <td> Backslash  </td></tr>

<table>


<style>
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
</style>



