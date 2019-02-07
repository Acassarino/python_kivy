"""
semplici regole grammaticali usando le classi
in modo gerarchico

alex    6 Feb 2019
"""

class parola( object ):
    def indovina_genere( self ):
        if self.stringa[ -1 ] == 'o':
            self.genere = 'M'
        if self.stringa[ -1 ] == 'a':
            self.genere = 'F'
        if self.stringa[ -1 ] == 'e':
            self.genere = None

    def __init__( self, n ):
        self.stringa  = n
        self.indovina_genere()

    def plurale( self ):
        if self.genere == 'M':
            return self.stringa[ : -1 ] + 'i'
        if self.genere == 'F':
            return self.stringa[ : -1 ] + 'e'

class nome( parola ):
    def __init__( self, n ):
        super( nome, self ).__init__( n )

class aggettivo( parola ):
    def __init__( self, n ):
        super( aggettivo, self ).__init__( n )

    def set_maschile( self ):
        self.stringa    = self.stringa[ : -1 ] + 'o'
        self.genere     = 'M'

    def set_femminile( self ):
        self.stringa    = self.stringa[ : -1 ] + 'a'
        self.genere     = 'F'

    def maschile( self ):
        return self.stringa[ : -1 ] + 'o'

    def femminile( self ):
        return self.stringa[ : -1 ] + 'a'

    def superla( self ):
        if self.genere == 'M':
            return self.stringa[ : -1 ] + 'issimo'
        if self.genere == 'F':
            return self.stringa[ : -1 ] + 'issima'
        return self.stringa
