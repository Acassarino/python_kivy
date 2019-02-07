# py_master
## piccoli progetti in `python` con interfaccia `kivi`

---

Questo repository raccoglie dei piccoli progetti scritti in linguaggio
`Python`, nel folder [python](./python), di cui alcuni che utilizzano
interfaccia uomo-macchine mediante `kivy`, nel folder [kivy](./kivy)

---

## requisiti

Per i progetti che usano solamente `python` e\` sufficiente installarlo, seguendo
le indicazioni relative al proprio sistema operativo, ecco qui alcuni dettagli.  

Nei sistemi operativi `linux` `python` risulta gia\` installato, non occorre
quindi fare nulla  

Per sistemi Mac si possono seguire due strade:
- usare [l'istallatore standard](https://www.python.org/downloads/mac-osx/)
- installare preventivamente [MacPorts](https://www.macports.org/) e poi usare
  MacPorts stesso per installare `python`, con il comando
  	sudo port install python35

Per i sistemi Windows occorre scaricare uno degli `executable installer` [dalla
distribuzione ufficiale Python](https://www.python.org/downloads/windows/),
usando la versione `x86` se il proprio computer e\` a 32 bit, oppure `x86-64` se
il proprio computer e\` a 64 bit (se non lo si sa, queste sono [le
indicazioni](https://www.computerhope.com/issues/ch001121.htm) per verificarlo).

---

Per usare `kivy` occorre installarlo, una volta avendo `python` funzionante.

Nei sistemi operativi `linux` basta eseguire:
	pip install kivy

Nei sistemi Mac si puo' usare lo stesso procedimento se python e\` stato
installato mediante MacPorts, altrimenti si puo' installare [Kivy come
applicazione](https://kivy.org/doc/stable/installation/installation-osx.html).


Per i sistemi Windows occorre [seguire questa
procedura](https://kivy.org/doc/stable/installation/installation-windows.html).

---

## strumenti utili

Non appena si transita da sperimentare pochi comangi python nell'interprete a
sviluppare piccoli progetti, diventa necessario utilizzare uno strumento per
scrivere file sorgenti.  
La soluzione minimale consiste nell'impiegare qualunque editor di testo, per
esempio in Windows il cosiddetto [blocco note](https://it.wikipedia.org/wiki/Blocco_note)

Risuta pero' decisamente vantaggioso utilizzare editor specializzati per la
programmazione, in cui vi sono ausili (colori, evidenziazione) per evitare di
sbagliare a scrivere comandi.

L'editor per programmazione piu' potente e universale e\` il
[vim](https://www.vim.org/), gia' installato in Linux, e disponibile per
qualunque sistema operativo, richiede un certo tempo per impadronirsi di tutte
le sue funzioni.

Un editor piu' semplice ed immediato da utilizzare, ma comunque molto potente,
per MacOs e\` [Sublime Text](https://www.sublimetext.com/), per Windows si
consiglia [Notepad++](https://notepad-plus-plus.org/)


---

## soluzione a possibili inconvenienti

Utenti Windows hanno facilmente difficolta' nell'importare in Python i file
sorgenti che hanno creato, perche' non viene trovata la directory dove si
trovano.

La soluzione migliore e\` di evitare di eseguire Python lanciandolo come
normalmente si eseguono i programmi, e invece seguire i seguenti passi:

- aprire un [terminale di
  comandi](https://www.memexcomputer.it/aprire-il-prompt-dei-comandi-di-windows/)

- tipicamente la finestra si trova gia' posizionata nella directory utente, e
  quindi laddove ci sono i file in python di interesse, in caso contrario usare
  il comando `cd` per cambiare directory

- invocare l'interprete python con il comando `py`
