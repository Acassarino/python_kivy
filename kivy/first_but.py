"""
stupida GUI che rende una parola maiuscola
"""

from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Upper( BoxLayout ):

    def on_conv( self, *args ):
        print( 'converting...' )
        self.l.text  = self.t.text.upper()

    def __init__( self ):
        super( Upper, self ).__init__()
        self.s  = ""
        self.b  = Button( text='convert' )
        self.t  = TextInput( multiline=False )
        self.l  = Label( text="" )
        self.b.bind( on_release=self.on_conv )
        self.add_widget( self.t )
        self.add_widget( self.b )
        self.add_widget( self.l )

class UpperApp( App ):
    def build( self ):
        return Upper()

if __name__ == '__main__':
    app = UpperApp()
    app.run()
