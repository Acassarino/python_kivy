# py_master - python


## piccoli progetti in python

Il file [gramm.py](gramm.py) contiene delle semplici regole grammaticali della
lingua italiana riguardo il plurale dei nomi, il file [cgramm.py](cgramm.py) ha
lo stesso scopo, ma utilizza le classi.

[cgramm1.py](cgramm1.py) esemplifica come impiegare le classi in modo
gerarchico, con una classe al alto livello `parola`, e poi due sue sottoclassi,
`nome` e `aggettivo`.

Il file [intergramm.py](intergramm.py) rappresenta una semplicissima interfaccia
per utilizzare in modo interattivo le funzioni in [cgramm1.py](cgramm1.py).
Questo e\` un programma completo, che non va eseguito all'interno
dell'interprete, ma direttamente, per esempio con il comando:
	python intergramm.py

oppure, in Windows con:
	py intergramm.py

sempre in Windows e\` possibile eseguilo anche semplicemente cliccando sulla sua
icona.

---

Il file [lex_stat.py](lex_stat.py) fornisce una primo semplice esempio di
[analisi semantica
distribuzionale](https://en.wikipedia.org/wiki/Distributional_semantics),
ovvero di analisi dei testi basati sulla distribuzione statistica dellle parole.

Sono prese come esempio [alcune famose poesie italiane](poesie/README.md)

Analogamente a [intergramm.py](intergramm.py), anche per [lex_stat.py](lex_stat.py)
si e\` scritta una semplicissima interfaccia: [inter_lex.py](inter_lex.py).
