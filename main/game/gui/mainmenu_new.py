'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


from ursina import *
#from ursina.prefabs.memory_counter import *

#from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *

from panda3d.core import *
from panda3d import *

from pandac.PandaModules import ClockObject
##from pandac.PandaModules import *


from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *
import sys


from panda3d.core import WindowProperties
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText

Text.default_resolution = 1080 * Text.size


# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)

try:
    from game.archivements.reset import Reset
    from game.main.world.lights.lights import Lights
    from game.main.GameSystem.inventory_bar import InventoryBar
except:
    print("Cannot load Game files - mainmenu.py")


class MainMenu(Entity):
    def __init__(self, player, pivot, direc_light, amb_light, music, esc_status):
        super().__init__(
            parent = camera.ui
        )

        self.direc_light = Lights().direc_light
        self.pivot = Lights().pivot
        self.amb_light = Lights().amb_light

        self.music = music



        #font = loader.loadFont('arial.ttf')
        #font.setPixelsPerUnit(60)
        self.font = loader.loadFont("../../assets/arial.ttf")
        #self.font.setPixelsPerUnit(60)
        font = '../../assets/arial.ttf'

        Text.default_font = font



        self.main = Entity(parent = self, enabled = True)
        self.main.disable()
        self.main.fade_in(value=1, duration=.5)

        self.main_menu = Entity(parent = self.main, enabled = True)
        self.main_menu.disable()
        self.main_menu.fade_in(value=1, duration=.5)

        self.settings = Entity(parent = self.main, enabled = False)

        self.graph_settings = Entity(enabled = False)
        self.audio_settings = Entity(parent = self.settings, enabled = False)

        self.player = player
        window.exit_button.visible = True

        self.inventoryBar = InventoryBar()
        self.inventoryBar.enabled = False

        self.player.disable()

        # Frames

        self.Frame_audio = DirectFrame(parent = self.audio_settings, frameColor=(0, 0, 0, 0.5),
                                       frameSize=(-1, 1, -1, 1),
                                       pos=(0, 0, 0))
            

        self.Frame_audio.hide()

        

        if esc_status == 0:
##            Frame_audio.show()
##            graphics.Frame.show()
            self.player.disable()
        elif esc_status == 1:
            self.player.enable()
##            Frame_audio.hide()
##            Frame.hide()
            
        
#        application.paused = True

        def settings():
            #self.player.enable()
            #mouse.locked = True
            self.main_menu.disable()
            self.settings.enable()

        def conti():
            application.paused = False
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()
            self.Back_button.disable()
            self.inventoryBar.enabled = True


        def reset():
            application.paused = False
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()

            Reset()
            self.player.position = (0,0,2)



        def back():
            #self.player.enable()
            #mouse.locked = True
            self.main_menu.enable()
            self.settings.disable()
            self.graph_settings.disable()
            self.audio_settings.disable()
            self.Audio_back_button.visible = False
            
            self.Frame_audio.hide()
            self.graphics()
            self.entry.hide()

            self.Frame.hide()

            
        #Graphics
        graphics_button = Button(text = "G r a p h i c s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.settings)
        graphics_button.on_click = Func(self.graphics)


        #Audio
        audio_button = Button(text = "A u d i o", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.settings)
        audio_button.on_click = Func(self.audio)

        
        continue_button = Button(text = "C o n t i n u e", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.main_menu)
        settings_button = Button(text = "S e t t i n g s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        reset_button = Button(text = "R e s e t", color = color.red, scale_y = 0.1, scale_x = 0.3, position = Vec3(x = 0, y = -0.22, z = 1), parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.gray, scale_y = 0.1, scale_x = 0.3, position = Vec3(x = 0, y = -0.3, z = -3), parent = self.main_menu)
        quit_button.on_click = application.quit
        settings_button.on_click = Func(settings)
        continue_button.on_click = Func(conti)
        reset_button.on_click = Func(reset)


        # Back
        self.Back_button = Button(text = "Back", color = color.rgb(58, 58, 96), scale_y = 0.1, scale_x = 0.5, y = 0.2, parent = self.settings)
        self.Back_button.on_click = Func(back)

        # Audio Back
        self.Audio_back_button = Button(text = "<<", color = color.rgb(158, 158, 196), scale_y = 0.1, scale_x = 0.2, y = 0.2, x = -0.25, parent = self.main, visible = False)
        self.Audio_back_button.on_click = Func(back)

##        # Graphics Back
##        self.Graph_back_button = Button(text = "<<", color = color.rgb(158, 158, 196), scale_y = 0.1, scale_x = 0.2, y = 0.2, x = -0.25, parent = self.main, visible = False)
##        self.Graph_back_button.on_click = Func(back)



    def setResolution( self, w, h ):
        wp = WindowProperties()
        wp.setSize( w, h )
        wp.setFullscreen( True )
        import os
        if os.name == 'posix':
          base.openMainWindow()
          base.graphicsEngine.openWindows()
        base.win.requestProperties( wp )



    def graphics(self):
            self.settings.disable()
            self.graph_settings.enable()


            self.Frame = DirectFrame(frameColor=(0, 0, 0, 0.5),
                                    frameSize=(-1, 1, -1, 1),
                                    pos=(0, 0, 0))
                        


            
            v = [0]
            vs = [0]
            vr = [0]






            Title = OnscreenText(text = "[ Graphics ]",
                    parent = self.Frame,
                    bg=(0,0,0,0),
                    fg=(255,255,255,1),
                    scale = 0.1,
                    pos = (0, 0.8, 0.2),
                    font = self.font)

            Fps_Limit = OnscreenText(text = "[ FPS Limit ]",
                    parent = self.Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, 0.6, 0.2),
                    font = self.font)

            Fps_Limit = OnscreenText(text = "[ Resolution ]",
                    parent = self.Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, -0.6, 0.2),
                    font = self.font)


            #clear the text
            def clearText():
                self.entry.enterText('')



            def setText(textEntered):

                
                FPS = int(textEntered)
                print(FPS)
                globalClock = ClockObject.getGlobalClock()
                globalClock.setMode(ClockObject.MLimited)
                globalClock.setFrameRate(FPS)

                

            #add text entry
            self.entry = DirectEntry(text = "",
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
                    self.entry.show()
                else:
                    print("Fps Limit - DISABLED")
                    self.entry.hide()   

            # Add button
            buttons = [
                DirectRadioButton(parent = self.Frame,
                                  text='Enabled',
                                  variable=v,
                                  value=[0],
                                  scale=0.05,
                                  pos=(0, 0.4, 0),
                                  #boxGeom="image.jpg",
                                  command=setFpsONOFF),
                
                DirectRadioButton(parent = self.Frame,
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





            Shadows_Quality = OnscreenText(text = "[ Shadows Quality ]",
                    parent = self.Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, -0.05, 0.2),
                    font = self.font)




            def setShadows(status=None):
                #print (v)
                if vs == [0]:
                    print("Shadows Quality - HIGH")
                    self.pivot.shadows = True
                    Entity.shadows = True
                    self.direc_light.shadows = True
                    self.amb_light.shadows = True
                    
                elif vs == [1]:
                    print("Shadows Quality - Medium")
                    self.pivot.shadows = True
                    Entity.shadows = False
                    self.direc_light.shadows = True
                    self.amb_light.shadows = False

                elif vs == [2]:
                    print("Shadows Quality - NONE")
                    self.pivot.shadows = False
                    Entity.shadows = False
                    self.direc_light.shadows = False
                    self.amb_light.shadows = False

            # Add button
            ShadowState = [
                DirectRadioButton(parent = self.Frame,
                                  text='  High  ',
                                  variable=vs,
                                  value=[0],
                                  scale=0.05,
                                  pos=(0, -0.2, 0),
                                  #boxGeom="image.jpg",
                                  command=setShadows),
                
                DirectRadioButton(parent = self.Frame,
                                  text='Medium',
                                  variable=vs,
                                  value=[1],
                                  scale=0.05,
                                  pos=(0, -0.3, 0),
                                  command=setShadows),

                DirectRadioButton(parent = self.Frame,
                                  text='  None  ',
                                  variable=vs,
                                  value=[2],
                                  scale=0.05,
                                  pos=(0, -0.4, 0),
                                  command=setShadows),

            ]

            for button in ShadowState:
                button.setOthers(ShadowState)
                #hide






            Shadows_Quality = OnscreenText(text = "[ Shadows Quality ]",
                    parent = self.Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, -0.05, 0.2),
                    font = self.font)



    



                    
            def changeResolution():
                #print (v)
                wp = WindowProperties()


                    
                if vs == [0]:
                    print("Resolution - 1920, 1080")

                    w, h = 1024, 768 

                    props = WindowProperties() 
                    props.setFullscreen(1)
                    props.setSize(w, h) 

                    base.win.requestProperties(props)


                    
                elif vs == [1]:
                    print("Resolution - 800, 600")
                    w, h = 800, 600 

                    props = WindowProperties() 
                    props.setFullscreen(1)
                    props.setSize(w, h) 

                    base.win.requestProperties(props)
                    
                elif vs == [2]:
                    print("Resolution - 400, 300")
                    w, h = 400, 300 

                    props = WindowProperties() 
                    props.setFullscreen(1)
                    props.setSize(w, h) 

                    base.win.requestProperties(props)

            # Add button
            ResoBTN = [
                DirectRadioButton(parent = self.Frame,
                                  text='  High  ',
                                  variable=vs,
                                  value=[0],
                                  scale=0.05,
                                  pos=(0, -0.7, 0),
                                  #boxGeom="image.jpg",
                                  command=changeResolution),
                
                DirectRadioButton(parent = self.Frame,
                                  text='Medium',
                                  variable=vs,
                                  value=[1],
                                  scale=0.05,
                                  pos=(0, -0.8, 0),
                                  command=changeResolution),

                DirectRadioButton(parent = self.Frame,
                                  text='  Low  ',
                                  variable=vs,
                                  value=[2],
                                  scale=0.05,
                                  pos=(0, -0.9, 0),
                                  command=changeResolution),

            ]

            for button in ResoBTN:
                button.setOthers(ResoBTN)

















    def audio(self):
            self.settings.disable()
            self.Audio_back_button.show()
            self.Frame_audio.show()

            









                


            Title_audio = OnscreenText(text = "[ Audio ]",
                    parent = self.Frame_audio,
                    bg=(0,0,0,0),
                    fg=(255,255,255,1),
                    scale = 0.1,
                    pos = (0, 0.8, 0.2),
                    font = self.font)


                        
            def scale_box():
                ts_a_v = thin_slider.value
                print(ts_a_v)
                self.music.volume = ts_a_v


            thin_slider = ThinSlider(text='Music Volume: ', dynamic=True, on_value_changed=scale_box)

            thin_slider.label.origin = (0,0)
            thin_slider.label.position = (.25, .05)
            thin_slider.label.color = color.rgba(200,200,200, 1)

            thin_slider.x = -.15



            # Callback function to set  text
            def setAudio(status):
                if status:
                    print("Audio Enabled")
                    base.enableAllAudio()
                else:
                    print("Audio Disabled")
                    base.disableAllAudio()
                    

            # Add button
            audioEnabled = DirectCheckButton(text = "Enable Audio", scale=.05, pos = (0, -0.2, 0.2), command=setAudio)






if __name__ == "__main__":
    app = Ursina()

    player = EditorCamera()
    pivot = Lights().pivot
    direc_light = Lights().direc_light
    amb_light = Lights().amb_light

    music = Audio('audio/Art-Of-Silence_V2.mp3', pitch=1, loop=True, autoplay=True)
    print(music.clip)
    music.volume=0
    music_b = Audio(music.clip)
    music_b.volume = 0
        
    esc_status = 0
    
    MainMenu(player, pivot, direc_light, amb_light, music, esc_status)


    app.run()
