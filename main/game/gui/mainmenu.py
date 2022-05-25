from ursina import *
#from ursina.prefabs.memory_counter import *

#from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from direct.gui.DirectGui import *

from panda3d.core import *
from panda3d import *

from pandac.PandaModules import ClockObject
from pandac.PandaModules import *


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

from game.archivements.reset import Reset



class MainMenu(Entity):
    def __init__(self, player, pivot, direc_light, amb_light, music, esc_status):
        super().__init__(
            parent = camera.ui
        )



        #font = loader.loadFont('arial.ttf')
        #font.setPixelsPerUnit(60)
        self.font = loader.loadFont("../../assets/arial.ttf")
        #self.font.setPixelsPerUnit(60)
        font = '../../assets/arial.ttf'

        Text.default_font = font


        self.wp = WindowProperties()



        self.main = Entity(parent = self, enabled = True)

        self.main_menu = Entity(parent = self.main, enabled = True)
        self.settings = Entity(parent = self.main, enabled = False)

        self.graph_settings = Entity(parent = self.settings, enabled = False)
        self.audio_settings = Entity(parent = self.settings, enabled = False)

        self.player = player
        window.exit_button.visible = True


        self.player.disable()
            




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


        def reset():
            application.paused = False
            self.player.enable()
            mouse.locked = True
            self.main_menu.disable()

            Reset()
            self.player.position = (0,0,2)

        def graphics():
            self.settings.disable()

            Frame = DirectFrame(frameColor=(0, 0, 0, 0.5),
                                     frameSize=(-1, 1, -1, 1),
                                     pos=(0, 0, 0))
            
            v = [0]
            vs = [0]
            vr = [0]






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

            Fps_Limit = OnscreenText(text = "[ Resolution ]",
                    parent = Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, -0.6, 0.2),
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





            Shadows_Quality = OnscreenText(text = "[ Shadows Quality ]",
                    parent = Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, -0.05, 0.2),
                    font = self.font)




            def setShadows(status=None):
                #print (v)
                if vs == [0]:
                    print("Shadows Quality - HIGH")
                    pivot.shadows = True
                    Entity.shadows = True
                    direc_light.shadows = True
                    amb_light.shadows = True
                    
                elif vs == [1]:
                    print("Shadows Quality - Medium")
                    pivot.shadows = True
                    Entity.shadows = False
                    direc_light.shadows = True
                    amb_light.shadows = False

                elif vs == [2]:
                    print("Shadows Quality - NONE")
                    pivot.shadows = False
                    Entity.shadows = False
                    direc_light.shadows = False
                    amb_light.shadows = False

            # Add button
            ShadowState = [
                DirectRadioButton(parent = Frame,
                                  text='  High  ',
                                  variable=vs,
                                  value=[0],
                                  scale=0.05,
                                  pos=(0, -0.2, 0),
                                  #boxGeom="image.jpg",
                                  command=setShadows),
                
                DirectRadioButton(parent = Frame,
                                  text='Medium',
                                  variable=vs,
                                  value=[1],
                                  scale=0.05,
                                  pos=(0, -0.3, 0),
                                  command=setShadows),

                DirectRadioButton(parent = Frame,
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
                    parent = Frame,
                    bg=(0,0,0,0),
                    fg=(200,200,200,1),
                    scale = 0.05,
                    pos = (0, -0.05, 0.2),
                    font = self.font)



    



                    
            def changeResolution():
                #print (v)


                    
                if vs == [0]:
                    print("Resolution - 1920, 1080")
                    window.size = window.fullscreen_size * .5
##                    self.setResolution, extraArgs = [ 1920, 1080 ]


                    window.windowed_size = 0.3
                    window.update_aspect_ratio()
                    
                elif vs == [1]:
                    print("Resolution - 800, 600")
                    window.windowed_size = 0.1
                    window.update_aspect_ratio()

                elif vs == [2]:
                    print("Resolution - 400, 300")



            # Add button
            ResoBTN = [
                DirectRadioButton(parent = Frame,
                                  text='  High  ',
                                  variable=vs,
                                  value=[0],
                                  scale=0.05,
                                  pos=(0, -0.7, 0),
                                  #boxGeom="image.jpg",
                                  command=changeResolution),
                
                DirectRadioButton(parent = Frame,
                                  text='Medium',
                                  variable=vs,
                                  value=[1],
                                  scale=0.05,
                                  pos=(0, -0.8, 0),
                                  command=changeResolution),

                DirectRadioButton(parent = Frame,
                                  text='  Low  ',
                                  variable=vs,
                                  value=[2],
                                  scale=0.05,
                                  pos=(0, -0.9, 0),
                                  command=changeResolution),

            ]

            for button in ResoBTN:
                button.setOthers(ResoBTN)


        def audio():
            self.settings.disable()

            





            Frame_audio = DirectFrame(frameColor=(0, 0, 0, 0.5),
                                           frameSize=(-1, 1, -1, 1),
                                           pos=(0, 0, 0))



                


            Title_audio = OnscreenText(text = "[ Audio ]",
                    parent = Frame_audio,
                    bg=(0,0,0,0),
                    fg=(255,255,255,1),
                    scale = 0.1,
                    pos = (0, 0.8, 0.2),
                    font = self.font)


                        
            def scale_box():
                ts_a_v = thin_slider.value
                print(ts_a_v)
                music.volume = ts_a_v


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




            
        #Graphics
        graphics_button = Button(text = "G r a p h i c s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.settings)
        graphics_button.on_click = Func(graphics)


        #Audio
        audio_button = Button(text = "A u d i o", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.settings)
        audio_button.on_click = Func(audio)

        
        continue_button = Button(text = "C o n t i n u e", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.main_menu)
        settings_button = Button(text = "S e t t i n g s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        reset_button = Button(text = "R e s e t", color = color.red, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.34, parent = self.main_menu)
        quit_button.on_click = application.quit
        settings_button.on_click = Func(settings)
        continue_button.on_click = Func(conti)
        reset_button.on_click = Func(reset)




    def setResolution( self, w, h ):
        wp = WindowProperties()
        wp.setSize( w, h )
        wp.setFullscreen( True )
        import os
        if os.name == 'posix':
          base.openMainWindow()
          base.graphicsEngine.openWindows()
        base.win.requestProperties( wp )


                    

