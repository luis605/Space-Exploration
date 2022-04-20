from ursina import *

from direct.gui.DirectGui import *
from panda3d.core import TransparencyAttrib
from panda3d import *
from pandac.PandaModules import ClockObject


class MainMenu(Entity):
    def __init__(self, player):
        super().__init__(
            parent = camera.ui
        )

        #font = loader.loadFont('arial.ttf')
        #font.setPixelsPerUnit(60)
        self.font = loader.loadFont("arial.ttf")
        #self.font.setPixelsPerUnit(60)
        font = 'arial.ttf'

        Text.default_font = font
        Text.default_resolution = 16*2


        self.main_menu = Entity(parent = self, enabled = True)
        self.settings = Entity(parent = self, enabled = False)
        self.graph_settings = Entity(parent = self, enabled = False)

        self.player = player
        window.exit_button.visible = True

        def settings():
            #self.player.enable()
            #mouse.locked = True
            self.main_menu.disable()
            self.settings.enable()

        def conti():
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()


        def reset():
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()

        def graphics():
            self.settings.disable()

            v = [0]



                
            Frame = DirectFrame(frameColor=(0, 0, 0, 0.5),
                                  frameSize=(-1, 1, -1, 1),
                                  pos=(0, 0, 0))

            Title = OnscreenText(text = "[ Graphics ]",
                    parent = Frame,
                    bg=(0,0,0,0),
                    fg=(255,255,255,1),
                    scale = 0.1,
                    pos = (0, 0.8, 0.2),
                    font = self.font)

            Fps_Limit = OnscreenText(text = "[ FPS Limit ]",
                    parent = Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, 0.6, 0.2),
                    font = self.font)


            #clear the text
            def clearText():
                entry.enterText('')

            def setText(textEntered):

                
                FPS = int(textEntered)
                print(FPS)
                globalClock = ClockObject.getGlobalClock()
                globalClock.setMode(ClockObject.MLimited)
                globalClock.setFrameRate(FPS)

                

            #add text entry
            entry = DirectEntry(text = "",
                                command=setText,
                                scale=.05,
                                width=3,
                                pos=(-0.1, 0.15, 0),
                                initialText="Type Fps Limit",
                                numLines = 1,
                                focus=1,
                                focusInCommand=clearText)



            def setFpsONOFF(status=None):
                #print (v)
                if v == [0]:
                    print("Fps Limit - ENABLED")
                    entry.show()
                else:
                    print("Fps Limit - DISABLED")
                    entry.hide()   

            # Add button
            buttons = [
                DirectRadioButton(parent = Frame,
                                  text='Enabled',
                                  variable=v,
                                  value=[0],
                                  scale=0.05,
                                  pos=(0, 0.4, 0),
                                  #boxGeom="image.jpg",
                                  command=setFpsONOFF),
                
                DirectRadioButton(parent = Frame,
                                  text='Disabled',
                                  variable=v,
                                  value=[1],
                                  scale=0.05,
                                  pos=(0, 0.3, 0),
                                  command=setFpsONOFF),

            ]

            for button in buttons:
                button.setOthers(buttons)
                #hide


                


        #Graphics
        graphics_button = Button(text = "G r a p h i c s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.settings)
        graphics_button.on_click = Func(graphics)

        
        continue_button = Button(text = "C o n t i n u e", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.main_menu)
        settings_button = Button(text = "S e t t i n g s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        reset_button = Button(text = "R e s e t", color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.34, parent = self.main_menu)
        quit_button.on_click = application.quit
        settings_button.on_click = Func(settings)
        continue_button.on_click = Func(conti)
        reset_button.on_click = Func(reset)
