'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *

from game.main.SpashScreen import SpashScreenInit



from ursina import *
#from ursina.prefabs.memory_counter import *

#from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *

from panda3d.core import *
from panda3d import *


from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
import sys


from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText

Text.default_resolution = 1080 * Text.size




app = Ursina()



class StartMenu(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )





        #font = loader.loadFont('arial.ttf')
        #font.setPixelsPerUnit(60)
        self.font = loader.loadFont("../../assets/arial.ttf")
        #self.font.setPixelsPerUnit(60)
        font = '../../assets/arial.ttf'

        Text.default_font = font


        self.main = Entity(parent = self, enabled = True)

        self.main_menu = Entity(parent = self.main, enabled = True)
        self.new_game = Entity(parent = self.main, enabled = True)
        self.saved_game = Entity(parent = self.main, enabled = True)



        window.exit_button.visible = False


            



#        application.paused = True

        def back():
            #self.player.enable()
            #mouse.locked = True
            self.main_menu.enable()

        def new_game():

            global app

            self.main_menu.disable()

            base.destroy()

            import main
            app.run()


        def load_game():

            self.main_menu.disable()


        # Back
        NewGame_button = Button(text = "Back", color = color.gray, scale_y = 0.1, scale_x = 0.5, y = 0.2, parent = self.main)
        NewGame_button.on_click = Func(back)
        
        # New Game
        NewGame_button = Button(text = "N e w   G a m e", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.new_game)
        NewGame_button.on_click = Func(new_game)


        # Load Game
        LoadGame_button = Button(text = "L o a d   G a m e", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.saved_game)
        LoadGame_button.on_click = Func(load_game)

        # Exit
        quit_button = Button(text = "Q u i t", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.34, parent = self.main_menu)
        quit_button.on_click = application.quit




    def setResolution( self, w, h ):
        wp = WindowProperties()
        wp.setSize( w, h )
        wp.setFullscreen( True )
        import os
        if os.name == 'posix':
          base.openMainWindow()
          base.graphicsEngine.openWindows()
        base.win.requestProperties( wp )


                    


def starting():
    SpashScreenInit()
    mainmenu = StartMenu()

starting()

if __name__ == '__main__':

        app.run()
