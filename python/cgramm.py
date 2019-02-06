"""
semplici regole grammaticali usando le classi

alex    30 Jan 2019
"""

class nome:
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
