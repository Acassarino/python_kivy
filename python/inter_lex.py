"""
semplicissima interfaccia per utilizzare lex_stat

alex    13 Feb 2019
"""

import lex_stat

poesie  = {
	1: "poesie/alla_musa.txt",
	2: "poesie/alla_sera.txt",
	3: "poesie/a_se_stesso.txt",
	4: "poesie/a_silvia.txt",
	5: "poesie/autoritratto.txt",
	6: "poesie/a_zacinto.txt",
	7: "poesie/infinito.txt",
	8: "poesie/passero_solitario.txt",
	9: "poesie/ultimo_canto_saffo.txt"
}

n_poesie    = len( poesie )

print( "benvenuto nel programma per la statistica lessicale in poesie" )
print( "" )

def pr_poesie():
    for p in range( n_poesie ):
        print( p+1, ':\t', poesie[ p+1 ] ) 

def pr_words( p, f ):
    for w in p:
        print( w, ':\t', f[ w ] ) 

"""
while True:
    pr_poesie()
    p       = int( input( "scegli la tua poesia: " ) )
    fr      = lex_stat.freq( lex_stat.leggi( poesie[ p ] ) )
    less    = lex_stat.less( fr )
    most    = lex_stat.most( fr )
    print( "parole piu` frequenti:" )
    pr_words( most, fr )
    print( "" )
    print( "" )
    print( "parole meno frequenti:" )
    pr_words( less, fr )
    print( "" )
    print( "" )
"""
