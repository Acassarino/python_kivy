# py_master kivy

## piccoli progetti in python con interfaccia kivi

Il file [first_first.py](first_first.py) e\` uno dei piu' semplici script
possibili utilizzanti `kivy`, viene utilizzato `BoxLayout`, che organizza i
componenti semplicement come box allineati in verticale oppure in orizzontale,
e viene inserito in `BoxLayout` un solo coomponente, di tipo `Label`, che
visualizza una scritta.

Nel file [first.py](first.py) lo stesso script viene leggermente sviluppato,
inserendo tre componenti `Label`, e usando altri argomenti in aggiunta a `text`
per cambiare l'apparenza della scritta. Viene inoltre cambiata l'orientazione in
`BoxLayout` da orizzontale (il suo default) in verticale.

---


Il file [first_but.py](first_but.py) introduce il componente `Button` e mostra
come abbinarlo (`bind`) ad un comportamento. L'esempio consiste nel rendere in
maiuscola una stringa, e questo implica un'ulteriore novita\`, i componenti
`TextInput`, finestre in cui si puo' inserire del testo.


Nel file [k_gramm.py](k_gramm.py) i `Button` trovano un impiego piu'
sofisticato, in abbinamento al modulo [cgramm1](../python/cgramm1.py) sviluppato
nella sezione [python](../python/README.md).
Si sono inoltre curati vari aspetti grafici, impostando colori, dimensione
complessiva del widget, dimensioni relative dei componenti.
