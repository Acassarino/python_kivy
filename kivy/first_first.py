"""
primissima GUI

alex 06 Feb 2019
"""

import kivy

from kivy.app           import App
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout

class First( BoxLayout ):

    def __init__( self ):
        super( First, self ).__init__()
        self.l  = Label( text="buonasera" )
        self.add_widget( self.l )

class FirstApp( App ):
    def build( self ):
        return First()

app = FirstApp()
app.run()
