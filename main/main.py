# ursina
from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import *

from ursina.shaders import lit_with_shadows_shader
#from ursina.shaders.screenspace_shaders import camera_grayscale

from ursina.prefabs.button_list import *

# panda3d
from direct.showbase.DirectObject import DirectObject
from direct.task import Task
from direct.actor.Actor import Actor
from direct.filter.CommonFilters import CommonFilters
from direct.filter.FilterManager import FilterManager

from pandac.PandaModules import *
from direct.gui.DirectGui import *

from panda3d import *

# random, os, pickle, etc
from random import randint,randrange
import pickle # added
import os # added
from time import perf_counter
import threading
from math import sin, cos


# game modules
from game.gui.mainmenu import MainMenu
from game.gui.inventory import Inventory

from game.archivements.firstTime import FirstTime

from game.common.SpashScreen import SpashScreenInit
from game.common.world.generator.world_generator import Generate_Terrain
from game.common.world.lights.lights import Lights
from game.common.bots.bots import AIPathFinder

# Vars                                  
key_f = 0
key_esc = 0
key_walk = 0
fly_key = 0

distance_mouse_create = 0






# Game
app = Ursina()


# Window configs
window.title = 'Space Exploration' # The window title
#window.borderless = False
window.color = color.dark_gray 
window.cog_button.enabled = False

window.exit_button.text = 'Exit'
window.exit_button.color = color.gray



def starting():

    SpashScreenInit()
#    level.bow.enabled = True



starting()
    
# Fog
myFog = Fog("Far Away Fog")
myFog.setColor(100,100, 100)
myFog.setExpDensity(1)
render.setFog(myFog)


# Shadows and shaders
Entity.default_shader = lit_with_shadows_shader

# Perlin Noise
#noise = PerlinNoise(octaves=3, seed=randint(1,1000000000))
seed=randint(1,1000000000)


# Optimization
voxel_scene = Entity(model=Mesh(vertices=[], uvs=[]), collider = 'mesh')




filters = CommonFilters(base.win, base.cam)
#filters.setBloom()



##manager = FilterManager(base.win, base.cam)
##tex = Texture()
##quad = manager.renderSceneInto(colortex=tex)
##quad.setShader(Shader.load("myfilter.sha"))
##quad.setShaderInput("tex", tex)



#removed load_texture
blocks = [
    0,
    load_texture("assets/grass.png"),
    load_texture("assets/soil.png"),
    load_texture("assets/stone.png"),
    load_texture("assets/wood.png")
]

block_id = 1


# Sky
sky_texture = load_texture("assets/skybox-4k.jpg")


cube = 'cube'
sphere = 'sphere'


# Load sounds
music = Audio('Art-Of-Silence_V2.mp3', pitch=1, loop=True, autoplay=True)
print(music.clip)
music.volume=0
music_b = Audio(music.clip)
music_b.volume = 0

from direct.showbase import Audio3DManager
audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)

###
jumpSd = base.loader.loadSfx('assets/audio/effects/jump.mp3')
menuSd = base.loader.loadSfx('assets/audio/effects/menu-pop.mp3')
runningSd = base.loader.loadSfx('assets/audio/walk/grass_walk.ogg.mp3')
runningSd.setLoop(True)
runningSd.setVolume(0.075)
runningSd.play()

status = runningSd.status()
print("Status: " + str(status))


# Lights
Lights()
pivot = Lights().pivot
direc_light = Lights().direc_light
amb_light = Lights().amb_light




health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=100)


def update():

#    print(mouse.hovered_entity)



	
    if held_keys['g']:
        save_game()

    if held_keys['shift']:
        player.speed=10
        



    
def input(key):
    
        global block_id, hand, key_f, key_esc, key_walk, fly_key, distance_mouse_create
        if key.isdigit():
            block_id = int(key)
            if block_id >= len(blocks):
                block_id = len(blocks) - 1
            Hand(texture = blocks[block_id])









        if key == 'scroll up':
            distance_mouse_create += 1
            print(distance_mouse_create)


        if key == 'scroll down':
            distance_mouse_create -= 1
            print(distance_mouse_create)


# AGORA fazer scroll na colocação de objetos (Camera e player em VOXEL)            

        
        if key == '+' or key == '+ hold':
            health_bar_1.value += 10
        if key == '-' or key == '- hold':
            health_bar_1.value -= 10

        if key == 'v':
            a.fade_out(duration=4, curve=curve.linear)

        if key == 'b':
            a.fade_in(value=1, duration=.5, delay=0, curve=curve.in_expo, resolution=None, interrupt='finish',)

        if key == 'k':
            Rocket()
                        
        if key == 'escape' and key_esc == 0:
            key_esc = 1
#            player.enabled = False
            #            quit()
            mainmenu = MainMenu(player, pivot, direc_light, amb_light, music_b, key_esc)
#        elif (key == 'escape' and key_esc == 1):
            key_esc = 0
            MainMenu(player, pivot, direc_light, amb_light, music_b, key_esc).main.enabled = False#            mainmenu = MainMenu(player, pivot, direc_light, amb_light, music_b, key_esc)
#            player.enable()
#            MainMenu(player, pivot, direc_light, amb_light, music_b, key_esc).main_menu.visible = False


            
            
        if key == 'w':
            player.speed=5


            runningSd.setPlayRate(1.0)
            runningSd.setTime(1)
            runningSd.play()

                    ##            if key_walk == 0:
##                key_walk = 1
##                grass_walk_b.resume()
##            else:
##                key_walk = 0
            
        if (key == 'j' and fly_key == 1):
            fly_key = 0
            print("Flying")
            fly()

        elif (key == 'j' and fly_key == 0):
            fly_key = 1
            print("Not Flying")
            notFly()

           
        if (key == 'f' and key_f == 0):
            key_f = 1
            print("Enabling")
            inventory_enable()
        elif (key == 'f' and key_f == 1):
            key_f = 0
            print("Disabling")
            inventory_close()







def fly():


    player.animate_y(rocket.y+3, 2, resolution=int(1//time.dt), curve=curve.out_expo)

            
def notFly():
    air_time = 0

    # if not on ground and not on way up in jump, fall
    player.y -= min(air_time, .05) * time.dt * 100
    air_time += time.dt * .25 * 0.9
    
        
def inventory_close():
    Inventory(player).inventory_ui.disable()
    Inventory(player).item_parent.disable()
    Inventory(player).disable()
    print("Finished")
    player.enable()

    
def inventory_enable():

    inventory = Inventory(player)

    

    


     
class Hand(Entity):
    def __init__(self, texture):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture=blocks[block_id],
            scale=0.2,
            rotation=Vec3(-10, -10, 10),
            position=Vec2(0.4, -0.4)
        )




game_data = []

class Voxel(Button):
    def __init__(self, model, position = (0,0,0), texture = blocks[block_id]):
        super().__init__(
            parent=voxel_scene,
            model=model,
            color=color.white,
            highlight_color=color.lime,
            texture=texture,
            position=position,
            origin_y=0.5,
            shader=lit_with_shadows_shader,
            collider="mesh"
        )
        

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if (blocks[block_id] == 5):
                    print("Lauching arrow")
                    player.arrow = duplicate(level.arrow, world_parent=level.bow, position=Vec3(-.2,0,0), rotation=Vec3(0,0,0))
                    player.arrow.animate('position', player.arrow.position+Vec3(0,0,-2), duration=.2, curve=curve.linear)

                else:
                    
                    model = cube

                    voxel = Voxel(model, position=self.position + mouse.normal, texture = blocks[block_id])
                    pos = self.position + mouse.normal
                    game_data.append([model, (pos.x,pos.y,pos.z),blocks[block_id]])

            if key == 'right mouse down':
                destroy(self)


class WorldMesh(Button):
    def __init__(self, model, position = (0,0,0), texture = blocks[block_id]):
        super().__init__(
            parent=voxel_scene,
            model=model,
            color=color.white,
            texture=texture,
            position=position,
            origin_y=0.5,
            shader=lit_with_shadows_shader,
            collider="mesh"
        )
        









class Rocket(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 5
        self.height = 2

        self.gravity = 1
        self.grounded = False
        self.jump_height = 2
        self.jump_up_duration = .5
        self.fall_after = .35 # will interrupt jump up
        self.jumping = False
        self.air_time = 0

        for key, value in kwargs.items():
            setattr(self, key ,value)


        # make sure we don't fall through the ground if we start inside it
        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            if ray.hit:
                self.y = ray.world_point.y
                
        self.go_up()

    def update(self):



            # gravity
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= self.height+.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity



    def go_up(self):

        rocket.shake(duration=.2, magnitude=1, speed=.05, direction=(1,1))


        self.grounded = False
        rocket.animate_y(rocket.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)



    def start_fall(self):
        rocket.y_animator.pause()
        self.jumping = False


    def land(self):
        # print('land')
        self.air_time = 0
        self.grounded = True










        









def save_game():
    print("Saving")
    with open("game_stage.pickle", "wb") as file_:
        pickle.dump(game_data, file_, -1)

def load_basic_game():



    world = Generate_Terrain(150,#xsize
                             150,#ysize
                             5,#frequency(how frequently new mountains generate)
                             5,#amplitude(how high or low the mountains will be)
                             1,#octaves(how many mountains there will be)
                             seed#seed(random number)
                            )
    #required command Generate_world which will create the model via given args
    model = world.Generate_World()

    game_data.append(world)


    #e = Entity(model=model,collider='mesh',texture='grass')
    world_model = WorldMesh(model, texture = 'grass.png')




def load_saved_game():
    saved_game = pickle.load(open("game_stage.pickle", "rb", -1))
    for data in saved_game:
        print(data)#            rocket.animate_y(rocket.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)

        try:
            voxel = Voxel(data[2], data[0], texture = data[1])
        except TypeError:
            world = Generate_Terrain(50,#xsize
                                     50,#ysize
                                     60,#frequency(how frequently new mountains generate)
                                     5,#amplitude(how high or low the mountains will be)
                                     1,#octaves(how many mountains there will be)
                                     seed#seed(random number)
                                    )
            model = world.Generate_World()
            world_model = WorldMesh(model, texture = 'grass.png')


        game_data.append(data)


if os.path.isfile("game_stage.pickle"):
    load_saved_game()
else:
    load_basic_game()
    save_game()


key_f = 0
#rocket = Voxel("1.blend", [0,0,0],None)
#rocket = Voxel(cube, [0,0,0],None)

rocket = Voxel('assets/blend/player_test1.obj', [0,0,0],None)

player = FirstPersonController(model='assets/blend/player_test1.obj', collider='mesh', scale = 1, color=color.rgba(0,0,0,.3), rotation = Vec3(0,0,0))

window.exit_button.visible = False
Sky(texture=sky_texture)



#ARCHIVEMENTS
FirstTime()
   

#BOTS
AIPathFinder(player)



app.run()

