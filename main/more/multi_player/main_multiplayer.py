# ursina
from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import *

from ursina.shaders import lit_with_shadows_shader
#from ursina.shaders.screenspace_shaders import camera_grayscale

from ursina.scripts.merge_vertices import *
from ursina.prefabs.button_list import *

# panda3d
from direct.showbase.DirectObject import DirectObject

from pandac.PandaModules import ClockObject
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d import *

# Perlin Noise
from perlin_noise import PerlinNoise
#from perlin_noise import *

# random, os, pickle, etc
from random import randint,randrange
import pickle # added
import os # added
from time import perf_counter
import numpy as np


# game modules
from mainmenu import MainMenu
#from mainmenu import *



# Vars                                  
key_f = 0
key_esc = 0
fly_key = 0

distance_mouse_create = 0




# Game
app = Ursina()


# Window configs
window.title = 'Space Exploration' # The window title
window.borderless = False
window.color = color.dark_gray 


# Fog
scene.fog_density=(0,75)
scene.fog_color=color.white


# Shadows and shaders
Entity.default_shader = lit_with_shadows_shader

# Perlin Noise
noise = PerlinNoise(octaves=3, seed=randint(1,1000000000))


# Optimization
voxel_scene = Entity(model=Mesh(vertices=[], uvs=[]), collider = 'mesh')



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


music = Audio('Art-Of-Silence_V2.mp3', pitch=1, loop=True, autoplay=True)
print(music.clip)
music.volume=1
music_b = Audio(music.clip)



pivot = Entity()
direc_light = Ursina_DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))
amb_light = Ursina_AmbientLight(parent=pivot, color = color.rgba(100, 100, 100, 0.1))





health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=100)


def update():

#    print(mouse.hovered_entity)



	
    if held_keys['g']:
        save_game()

    if held_keys['shift'] and held_keys['w']:
        player.speed=10
        


#    if held_keys['k']:
#        Rocket()
        




def input(key):
    
        global block_id, hand, key_f, key_esc, fly_key, distance_mouse_create
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
#            quit()
            player.enabled = False
            mainmenu = MainMenu(player, pivot, direc_light, amb_light, music_b)
        elif (key == 'escape' and key_esc == 1):
            key_esc = 0
            player.enabled = True
            MainMenu(player, pivot, direc_light, amb_light, music_b).main_menu.visible = False
            MainMenu(player, pivot, direc_light, amb_light, music_b).Frame.visible = False
#            MainMenu(player, pivot, direc_light, amb_light, music_b).main_menu.visible = False

            
            
        if key == 'w':
            player.speed=5

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
    Inventory().inventory_ui.disable()
    Inventory().item_parent.disable()
    Inventory().disable()
    print("Finished")
    player.enable()

    
def inventory_enable():

    inventory = Inventory()

    

    


class Inventory(Entity):
    def __init__(self):
        player.enabled = False
        super().__init__(
            parent = camera.ui
        )

        self.inventory_ui = Entity(parent = self,
            model = 'quad',
            scale = (.5, .8),
            origin = (-.5, .5),
            position = (-.3,.4),
            texture = 'white_cube',
            texture_scale = (5,8),
            color = color.dark_gray,
            enable = True
        )

        self.item_parent = Entity(parent=self.inventory_ui, scale=(1/5,1/8))
        
    def find_free_spot(self):                                                      
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]    
        for y in range(8):                                                         
            for x in range(5):                                                     
                if not (x,-y) in taken_spots:                                      
                    return (x,-y)                                                  


    def append(self, item):
        icon = Draggable(
            parent = Inventory().item_parent,
            model = 'quad',
            texture = item,
            color = color.white,
            origin = (-.5,.5),
            position = self.find_free_spot(),
            z = -.1,
            )
        name = item.replace('_', ' ').title()
        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0,0,0,.8)


        def drag():                                                     
            icon.org_pos = (icon.x, icon.y)                             

        def drop():
            icon.x = int(icon.x)
            icon.y = int(icon.y)



            '''if the spot is taken, swap positions'''
            for c in self.children:                                     
                if c == icon:                                           
                    continue                                            

                if c.x == icon.x and c.y == icon.y:                     
                    print('swap positions')                             
                    c.position = icon.org_pos                           


        icon.drag = drag                                                
        icon.drop = drop




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


##            print(player.position)
##            print(self.position)
##
##            p_pos = player.position
##            s_pos = self.position

##            print(p_pos - s_pos)

##            rocket.position(p_pos - s_pos)

            

            if key == "left mouse down":
                
                model = cube

                voxel = Voxel(cube, position=self.position + mouse.normal, texture = blocks[block_id])
                pos = self.position + mouse.normal
                game_data.append([cube, (pos.x,pos.y,pos.z),blocks[block_id]])



            if key == 'right mouse down':
                destroy(self)






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



    world = Generate_Terrain(50,#xsize
                             50,#ysize
                             5,#frequency(how frequently new mountains generate)
                             5,#amplitude(how high or low the mountains will be)
                             1,#octaves(how many mountains there will be)
                             300#seed(random number)
                            )
    #required command Generate_world which will create the model via given args
    model = world.Generate_World()

    #e = Entity(model=model,collider='mesh',texture='grass')
    e = Voxel(model, texture = 'grass.png')




def load_saved_game():
    saved_game = pickle.load(open("game_stage.pickle", "rb", -1))
    for data in saved_game:
#        print(data)#            rocket.animate_y(rocket.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)

        voxel = Voxel(data[2], data[0], texture = data[1])
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

player = FirstPersonController(model='assets/blend/player_test1.obj', collider='mesh', scale = 1, color=color.rgba(0,0,0,.3))
#player = FirstPersonController()
#EditorCamera()
window.exit_button.visible = False
Sky(texture=sky_texture)






class CarRepresentation(Entity):
    def __init__(self, car, position = (0, 0, 0), rotation = (0, 65, 0)):
        super().__init__(
            parent = scene,
            position = player.position,
            rotation = player.rotation,
            scale = (1, 1, 1)
        )

        self.text_object = None
        self.highscore = 0.0

class CarUsername(Text):
    def __init__(self, car):
        super().__init__(
            parent = car,
            text = "Guest",
            y = 10,
            scale = 10
        )

        self.username_text = "Guest"

    def update(self):
        self.text = self.username_text

        


app.run()

