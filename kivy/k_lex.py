"""
stupida GUI che rende una parola maiuscola
"""

from kivy.app               import App
from kivy.uix.button        import Button
from kivy.uix.label         import Label
from kivy.uix.textinput     import TextInput
from kivy.uix.boxlayout     import BoxLayout
from kivy.uix.filechooser   import FileChooserListView
from kivy.uix.listview      import ListView
from kivy.config            import Config

#Config.set( 'graphics', 'width', '250' )
#Config.set( 'graphics', 'height', '300' )

path    = "../python/poesie"

import  lex_stat

class Widg( BoxLayout ):

    def on_text( self, *args ):
        print( "text entered" )
        self.s  = self.t.text

    def on_conv( self, *args ):
        words   = []
        for f in self.f.selection:
            print( 'doing file', f )
            words   += lex_stat.leggi( f )
        freq    = lex_stat.freq( words )
        less    = lex_stat.less( freq )
        items   = []
        for w in less:
            items.append( w + ':   ' + str( freq[ w ] ) )
        self.lles.item_strings = items
        most    = lex_stat.most( freq )
        items   = []
        for w in most:
            items.append( w + ':   ' + str( freq[ w ] ) )
        self.lmos.item_strings = items

    def on_files( self, *args ):
        print( 'selected files' )
        self.lsel.item_strings = self.f.selection
            

    def __init__( self ):
        super( Widg, self ).__init__( orientation='vertical', spacing=20 )
        self.s  = ""
        self.txt    = TextInput( multiline=False, font_size=24 )
        self.bsel   = Button( text='select files', font_size=24, background_color= [ 0.8, 0.2, 0.1, 1 ] )
        self.bfrq   = Button( text='compute frequency', font_size=24, background_color= [ 0.2, 0.8, 0.1, 1 ] )
        self.lsel   = ListView( item_strings=[ "" ] )
        self.lles   = ListView( item_strings=[ "" ] )
        self.lmos   = ListView( item_strings=[ "" ] )
        self.f  = FileChooserListView( path=path, filters=[ '*.txt' ], multiselect=True )
        self.bsel.bind( on_release=self.on_files )
        self.bfrq.bind( on_release=self.on_conv )
        self.bb = BoxLayout( size_hint= ( 1, 0.2 ) )
        self.ff = BoxLayout()
        self.lm = BoxLayout( size_hint= ( 1, 0.6 ) )
        self.ff.add_widget( self.f )
        self.ff.add_widget( self.lsel )
        self.bb.add_widget( self.bsel )
        self.bb.add_widget( self.bfrq )
        self.lm.add_widget( self.lles )
        self.lm.add_widget( self.lmos )
        self.add_widget( self.lm )
        self.add_widget( self.bb )
        self.add_widget( self.ff )

class bu( App ):
    def build( self ):
        return Widg()

if __name__ == '__main__':
    bu().run()
