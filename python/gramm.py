"""
collezione di semplici funzioni di grammatica italiana

alex    30 Jan 2019
"""

vocali  = 'aioue'

def c_e_g( n ):
    """
    gestisce i casi particolari 'cia', 'gia', etc
    """
    if n[ -4 ] in vocali:
        return n
    return n[ : -2 ] + n[ -1 ]

def plurale( n ):
    """
    restituisce il plurale di un nome o aggettivo
    """
    acca    = ''
    if n[ -2 ] in 'cg':
        acca = 'h'
    if n[ -3 : -1 ] == 'ci':
        n   = c_e_g( n )
    if n[ -3 : -1 ] == 'gi':
        n   = c_e_g( n )
    if n[ -1 ] == 'a':
        return n[ : -1 ] + acca + 'e'
    if n[ -1 ] == 'o':
        return n[ : -1 ] + acca + 'i'
    if n[ -1 ] == 'e':
        return n[ : -1 ] + acca + 'i'
