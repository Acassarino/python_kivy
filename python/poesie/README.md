# py_master - python - poesie


## testi letterari per esempi di analisi del testo

Sono raccolte qui alcune poesie di Leopardi e di Foscolo, in formato testo, da
poter essere lette in programmi python per esercitare semplici analisi testuali.

Siccome i testi sono in lingua italiana, occorre fare attenzione alla presenza
delle lettere accentate, che non fanno parte del set di caratteris
[ASCII](https://en.wikipedia.org/wiki/ASCII) normalmente accettato da python
come stringa, ma occorre adottare la codifica
[Unicode](https://en.wikipedia.org/wiki/Unicode).

Quindi per aprire per esempio il file `passero_solitario.txt` anziche' usare la
funzione python `open` nel modo naturale:
	f = open( 'passero_solitario.txt', 'r' )

occorre aggiungere l'indicazione della codifica:
	f = open( 'passero_solitario.txt', 'r', encoding='utf-8' )
