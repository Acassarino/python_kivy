"""
semplicissima interfaccia per utilizzare cgramm1

alex    6 Feb 2019
"""

import cgramm1

print( "benvenuto nel programma per la gramamtica italiana" )
print( "" )

while True:
    na  = input( "vuoi nome o aggettivo? <1/0>: " )
    if na == 1:
        n   = raw_input( "dammi un nome: " )
        p   = cgramm1.nome( n )
        print( "1   -> plurale" )
        print( "2   -> genere" )
        s   = input( "cosa vuoi? " )
        if s == 1:
            print( p.plurale() )
        if s == 2:
            print( "il genere e` ", p.genere )
    if na == 0:
        a   = raw_input( "dammi un aggettivo: " )
        p   = cgramm1.aggettivo( a )
        print( "1   -> plurale" )
        print( "2   -> superlativo" )
        s   = input( "cosa vuoi? " )
        if s == 1:
            print ( p.plurale() )
        if s == 2:
            print ( p.superla() )
    print( "" )
    print( "" )
