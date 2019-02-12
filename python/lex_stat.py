"""
semplice analisi lessicale statistica
su testi

alex    13 Feb 2019
"""

stop_words  = [
    'nel', 'nella', 'nello', 'del', 'della', 'degli', 'che', 'mio', 'mia', 'tuo', 'tua', 'non',
    'quel', 'quello', 'quella'
]

non_alpha   = [ '.', ',', ':', ';', '!', '?', "'", '"' ]

def clean( s ):
    """
    elimina dalla stringa "s" i segni di punteggiatura
    """
    for c in non_alpha:
        s   = s.replace( c, " " )
    return s

def leggi( p ):
    """
    legge la poesia contenuta nel file "p" e restituisce una lista con tutte le
    parole significative
    """
    f   = open( p, 'r', encoding='utf-8' )
    s   = f.read()
    s   = clean( s )
    l   = s.split()
    words   = []
    for w in l:
        w   = w.lower()
        if w in stop_words:
            continue
        if len( w ) > 2:
            words.append( w )
    return words


def freq( words ):
    """
    da una lista di parole calcola la loro frequenza, restituita in un dizionario
    """
    d   = {}
    for w in words:
        if w in d.keys():
            d[ w ]  = d[ w ] + 1
        else:
            d[ w ]  = 1
    return d


def less( freq, n=5 ):
    """
    restituisci le n parole meno frequenti, usando la frequenza 'freq'
    """
    s   = sorted( freq, key=freq.get )
    return s[ : n ]


def most( freq, n=5 ):
    """
    restituisci le n parole piu` frequenti, usando la frequenza 'freq'
    """
    s   = sorted( freq, key=freq.get, reverse=True )
    return s[ : n ]
