"""
GUI leggermente meno stupida, per mostrare il plurale di un nome
"""

from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.config        import Config

Config.set( 'graphics', 'width', '250' )
Config.set( 'graphics', 'height', '300' )

from gramm              import plurale

class Widg( BoxLayout ):

    def on_plu( self, *args ):
        self.l.text  = plurale( self.t.text )

    def __init__( self ):
        super( Widg, self ).__init__( orientation='vertical', spacing=20 )
        self.s  = ""
        self.b  = Button( text='plurale', font_size=24, background_color= [ 0.8, 0.2, 0.1, 1 ], size_hint=( 1., 0.6 ) )
        self.t  = TextInput( multiline=False, font_size=24 )
        self.l  = Label( text="", font_size=24 )
        self.b.bind( on_release=self.on_plu )
        self.add_widget( self.t )
        self.add_widget( self.l )
        self.add_widget( self.b )

class bu( App ):
    def build( self ):
        return Widg()

if __name__ == '__main__':
    bu().run()
