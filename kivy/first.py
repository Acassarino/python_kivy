"""
prima GUI

alex 06 Feb 2019
"""

import kivy
kivy.require('1.0.8')

from kivy.app           import App
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout

class First( BoxLayout ):

    def __init__( self ):
        super( First, self ).__init__( orientation='vertical' )
        self.l1 = Label( text="buonasera", font_size='28' )
        self.l2 = Label( text="buongiorno", color=[ 0.8, 0, 0, 1 ] )
        self.l3 = Label( text="e mo basta", font_size='32' )
        self.add_widget( self.l1 )
        self.add_widget( self.l2 )
        self.add_widget( self.l3 )

class FirstApp( App ):
    def build( self ):
        return First()

app = FirstApp()
app.run()
