"""
esempio di banners pubblicitari che compaiono automaticamente
a seconda del testo che uno sta scrivendo
"""

from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image     import Image
from kivy.config        import Config

Config.set( 'graphics', 'width', '550' )
Config.set( 'graphics', 'height', '400' )


img0    = "imgs/black.jpg"
imgs    = {
    "viagg"     : "imgs/low_cost.jpg",
    "banan"     : "imgs/chiquita.jpg",
    "auto"      : "imgs/bentley.jpg"
}

class Widg( BoxLayout ):

    def on_text( self, *args ):
        """
        questa funzione viene eseguita per ogni nuovo carattere che viene immesso nella finestra
        di testo, e nell'intero testo scritto viene verificato se compare una delle parole chiave
        del dizionario imgs, in caso positivo viene mostrata l'immagine corrispondente
        se una chiave corrisponde ad un banner appena utilizzato, non si fa nulla
        """
        self.s  = self.txt.text
        for k in imgs.keys():
            if k in self.ban:
                continue
            if k in self.s:
                self.img.source = imgs[ k ]
                self.ban.append( k )
                break


    def clear( self, *args ):
        """
        ripristina la finestra di testo e carica un'immagine neutrale nello spazio dei banners
        """
        self.txt.text   = ""
        self.img.source = img0
        self.ban        = []


    def __init__( self ):
        """
        inizializza la classe, che e` sottoclasse di BoxLayout, inserendo le componenti:
            - TextInput dove puo' essere sxcritto il testo
            - Image     dove verra` visualizzato il banner
            - Button    che serve a ripristinare l'interfaccia
        notare che la componente TextInput viene legata ("bind") all'evento "text", che corrisponde
        all'inserimento di un singolo carattere nella finestra di testo
        la variabile self.ban contiene l'elenco dei banner usati, inizialmente una lista vuota
        """
        super( Widg, self ).__init__( orientation='vertical', spacing=20 )
        self.ban    = []
        self.but    = Button( text='clear', font_size=24, bold=True, size_hint=( 1, 0.2 ) )
        self.txt    = TextInput( multiline=True, font_size=24 )
        self.img    = Image( source=img0 )
        self.txt.bind( text=self.on_text )
        self.but.bind( on_release=self.clear )
        self.add_widget( self.txt )
        self.add_widget( self.but )
        self.add_widget( self.img )

class banner( App ):
    def build( self ):
        return Widg()

if __name__ == '__main__':
    banner().run()
