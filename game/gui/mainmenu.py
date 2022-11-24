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





# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL) 

try:
    sys.path.insert(0, "../")
    from archivements.reset import Reset
    from main.GameSystem.sound import Sound
    from ursina.lights import DirectionalLight as Ursina_DirectionalLight
    from ursina.lights import AmbientLight as Ursina_AmbientLight

except Exception as e:
    print("Cannot load Game files - mainmenu.py\n",e)
    from game.archivements.reset import Reset



class MainMenu(Entity):
    def __init__(self, player, music, direc_light, pivot, amb_light, InventoryBar, exit_btn):
        super().__init__(
            parent = camera.ui
        )


        self.direc_light = direc_light
        self.pivot = pivot
        self.amb_light = amb_light

        self.music = music



        #font = loader.loadFont('arial.ttf')
        #font.setPixelsPerUnit(60)
        self.font = loader.loadFont("assets/arial.ttf")
        #self.font.setPixelsPerUnit(60)
        font = 'assets/arial.ttf'

        Text.default_font = font



        self.main = Entity(parent = self, enabled = True)

        self.main_menu = Entity(parent = self.main, enabled = True)
        self.settings = Entity(parent = self.main, enabled = False)

        self.graph_settings = Entity(enabled = False)
        self.audio_settings = Entity(parent = self.settings, enabled = False)
        self.control_settings = Entity(parent = self.settings, enabled = False)

        self.player = player
        self.exit_btn = exit_btn
        print("\n\n\n\n\n\n\n\n\n\n\n\n", exit_btn)
        

        self.inventoryBar = InventoryBar
        self.inventoryBar.visible = False


        self.player.disable()

        # Pause Game        
        application.paused = False



        # Text Properties
##        Text.default_resolution = 1080 * Text.size
##        Text.default_color = color.black
##        Entity.default_color = color.black

        def settings():
            #self.player.enable()
            #mouse.locked = True
            self.main_menu.disable()
            self.settings.enable()

        def conti():
            self.disable()
            self.main_menu.disable()
            self.Back_button.disable()
            self.inventoryBar.enabled = True

            self.inventoryBar.visible = True

            self.exit_menu_button.visible = False


        def reset():
            self.disable()
            self.main_menu.disable()
            self.exit_menu_button.visible = False
            self.inventoryBar.visible = True

            Reset()

            self.player.land()
            self.player.position = (0,0,2)



        def back(to_settings = False):
            #self.player.enable()
            #mouse.locked = True
            self.main_menu.enable()
            self.settings.disable()
            self.graph_settings.disable()
            self.audio_settings.disable()
            self.control_settings.disable()

            if (to_settings):
                self.main_menu.disable()
                self.settings.enable()

            ## Frames
            ## Audio
            
            try:
                self.Frame_audio.hide()
                self.entry.hide()
            except:
                pass
            
            try:
                self.thin_slider.hide()
                self.audioEnabled.hide()
            except:
                pass

            ## Graphics

            try:
                self.Frame.hide()
            except:
                pass

            ## Control

            try:
                self.ControlFrame.hide()
            except:
                pass
            
            
            self.settings_back_button.visible = False        
            self.exit_menu_button.visible = True


        def exit_menu():
            print("Closing MainMenu")
            application.paused = False

            self.main.enabled = False
            self.main_menu.enabled = False
            self.exit_menu_button.visible = False
            self.inventoryBar.visible = True
            
            Sound().others(player).click.play()

            self.player.enable()


            
        #Graphics
        graphics_button = Button(text = "G r a p h i c s", text_color = color.black, color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.settings)
        graphics_button.on_click = Func(self.graphics)


        #Audio
        audio_button = Button(text = "A u d i o", text_color = color.black, color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.settings)
        audio_button.on_click = Func(self.audio)

        #Controllers
        controller_button = Button(text = "C o n t r o l l e r s", text_color = color.black, color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.22, parent = self.settings)
        controller_button.on_click = Func(self.controllers)

        
        continue_button = Button(text = "C o n t i n u e", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = 0.02, parent = self.main_menu)
        settings_button = Button(text = "S e t t i n g s", color = color.gray, scale_y = 0.1, scale_x = 0.3, y = -0.1, parent = self.main_menu)
        reset_button = Button(text = "R e s e t", color = color.red, scale_y = 0.1, scale_x = 0.3, position = Vec3(x = 0, y = -0.22, z = 1), parent = self.main_menu)
        quit_button = Button(text = "Q u i t", color = color.gray, scale_y = 0.1, scale_x = 0.3, position = Vec3(x = 0, y = -0.3, z = -3), parent = self.main_menu)
        quit_button.on_click = application.quit
        settings_button.on_click = Func(settings)
        continue_button.on_click = Func(conti)
        reset_button.on_click = Func(reset)

        # Exit Main Menu
        self.exit_menu_button = Button(text = "X", color = color.red, scale_y = 0.1, scale_x = 0.1, y = 0.2, x = -0.45, parent = self.main, visible = True)
        self.exit_menu_button.on_click = Func(exit_menu)


        # Back
        self.Back_button = Button(text = "Back", color = color.rgb(58, 58, 96), scale_y = 0.1, scale_x = 0.5, y = 0.2, parent = self.settings)
        self.Back_button.on_click = Func(back)

        
        # Settings Back
        self.settings_back_button = Button(use_tags=False, text = "Back", color = color.rgb(158, 158, 196), scale_y = 0.1, scale_x = 0.2, y = 0.2, x = -0.25, parent = self.main, visible = False)
        self.settings_back_button.on_click = Func(back, to_settings = True)



    def controllers(self):
        
        self.exit_menu_button.visible = False
        self.settings.disable()
        self.settings_back_button.show()
        self.control_settings.enable()

        self.ControlFrame = DirectFrame(frameColor=(0, 0, 0, 0.5),
                                    frameSize=(-1, 1, -1, 1),
                                    pos=(0, 0, 0))



        Title = OnscreenText(text = "[ Controllers ]",
                parent = self.ControlFrame,
                bg=(0,0,0,0),
                fg=(255,255,255,1),
                scale = 0.1,
                pos = (0, 0.8, 0.2),
                font = self.font)

        




    def change_controller(self, init_key, replace_with_key):
        input_handler.rebind(init_key, replace_with_key)

            
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
        self.exit_menu_button.visible = False
        self.settings_back_button.visible = True
        
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

        Shadows_Quality = OnscreenText(text = "[ Shadows Quality ]",
                parent = self.Frame,
                bg=(0,0,0,0),
                fg=(200,200,200,1),
                scale = 0.05,
                pos = (0, -0.05, 0.2),
                font = self.font)
        
##        Resolution_Quality = OnscreenText(text = "[ Resolution ]",
##                parent = self.Frame,
##                bg=(0,0,0,0),
##                fg=(200,200,200,1),
##                scale = 0.05,
##                pos = (0, -0.6, 0.2),
##                font = self.font)


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
                            parent = self.Frame,
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














##        def changeResolution():
##            #print (v)
##            wp = WindowProperties()
##
##
##                
##            if vs == [0]:
##                print("Resolution - 1920, 1080")
##
##                w, h = 1920, 1080 
##
##                props = WindowProperties() 
##                props.setSize(w, h) 
##
##                base.win.requestProperties(props)
##
##
##                
##            elif vs == [1]:
##                print("Resolution - 800, 600")
##                w, h = 800, 600 
##
##                props = WindowProperties() 
##                props.setSize(w, h) 
##
##                base.win.requestProperties(props)
##                
##            elif vs == [2]:
##                print("Resolution - 400, 300")
##                w, h = 400, 300 
##
##                props = WindowProperties() 
##                props.setSize(w, h) 
##
##                base.win.requestProperties(props)
##
##        # Add button
##        ResoBTN = [
##            DirectRadioButton(parent = self.Frame,
##                              text='  High  ',
##                              variable=vs,
##                              value=[0],
##                              scale=0.05,
##                              pos=(0, -0.7, 0),
##                              #boxGeom="image.jpg",
##                              command=changeResolution),
##            
##            DirectRadioButton(parent = self.Frame,
##                              text='Medium',
##                              variable=vs,
##                              value=[1],
##                              scale=0.05,
##                              pos=(0, -0.8, 0),
##                              command=changeResolution),
##
##            DirectRadioButton(parent = self.Frame,
##                              text='  Low  ',
##                              variable=vs,
##                              value=[2],
##                              scale=0.05,
##                              pos=(0, -0.9, 0),
##                              command=changeResolution),
##
##        ]
##
##        for button in ResoBTN:
##            button.setOthers(ResoBTN)

        F11_to_fullscreen = OnscreenText(text = "[ To enter fullscreen mode press: [f11] ]",
                parent = self.Frame,
                bg=(0,0,0,0),
                fg=(200,200,200,1),
                scale = 0.03,
                pos = (0, -0.98, 0),
                font = self.font)















    def audio(self):
        self.exit_menu_button.visible = False
        self.settings.disable()
        self.settings_back_button.show()

        self.Frame_audio = DirectFrame(frameColor=(0, 0, 0, 0.5),
                                frameSize=(-1, 1, -1, 1),
                                pos=(0, 0, 0))
            


    







            


        Title_audio = OnscreenText(text = "[ Audio ]",
                parent = self.Frame_audio,
                bg=(0,0,0,0),
                fg=(255,255,255,1),
                scale = 0.1,
                pos = (0, 0.8, 0.2),
                font = self.font)


                    
        def scale_box():
            ts_a_v = self.thin_slider.value
            print(ts_a_v)
            self.music.volume = ts_a_v


        self.thin_slider = ThinSlider(text='Music Volume: ', dynamic=True, on_value_changed=scale_box)

        self.thin_slider.label.origin = (0,0)
        self.thin_slider.label.position = (.25, .05)
        self.thin_slider.label.color = color.rgba(200,200,200, 1)

        self.thin_slider.x = -.15



        # Callback function to set  text
        def setAudio(status):
            if status:
                print("Audio Enabled")
                base.enableAllAudio()
            else:
                print("Audio Disabled")
                base.disableAllAudio()
                

        # Add button
        self.audioEnabled = DirectCheckButton(text = "Enable Audio", scale=.05, pos = (0, -0.2, 0.2), command=setAudio)



    def disable(self):
        application.paused = False
        self.player.enable()
        self.main.enabled = False
        self.main_menu.enabled = False
        self.exit_menu_button.visible = False
        self.inventoryBar.visible = True
        self.exit_btn.visible = False

        try:
            self.Frame_audio.hide()
        except:
            pass
        
        try:
            self.Frame.hide()
        except:
            pass

        
    def enable(self):
        application.paused = True
        self.player.disable()
        self.main.enabled = True
        self.main_menu.enabled = True
        self.exit_menu_button.visible = True
        self.inventoryBar.visible = False
        self.exit_btn.visible = True

        try:
            self.Frame_audio.show()
        except:
            pass
        
        try:
            self.Frame.show()
        except:
            pass




if __name__ == "__main__":
    app = Ursina()

    player = EditorCamera()
    player.disable()


    # Lights
    pivot = Entity()
    direc_light = Ursina_DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45), shadow_map_resolution = Vec2(1024, 1024))
    amb_light = Ursina_AmbientLight(parent=pivot, color = color.rgb(100, 100, 100), shadows = True)


    music = Audio('Art-Of-Silence_V2.mp3', pitch=1, loop=True, autoplay=True)
    print(music.clip)
    music.volume=0
    music_b = Audio(music.clip)
    music_b.volume = 0
        
    esc_status = Entity()

    InventoryBar = Entity(model='quad',parent=camera.ui)

    
    main_menu = MainMenu(player, pivot, direc_light, amb_light, music, InventoryBar, esc_status)
    main_menu.disable()
    main_menu.enable()
    
    


    app.run()
