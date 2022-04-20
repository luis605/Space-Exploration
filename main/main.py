# ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import *
from ursina.shaders import lit_with_shadows_shader
from ursina.scripts.merge_vertices import *

# panda3d
#from direct_s.filter.FilterManager import FilterManager
#from direct_s.filter.CommonFilters import CommonFilters
#from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import ClockObject
#from panda3d.core import LODNode
#from panda3d.core import CollisionTraverser
#from panda3d.core import CollisionHandlerPusher
#from panda3d.core import CollisionSphere, CollisionNode

# Perlin Noise
from perlin_noise import PerlinNoise

# random, os, pickle, etc
from random import randint,randrange
import pickle # added
import os # added
from time import perf_counter

# game modules
from mainmenu import MainMenu
#from inventory import *

key_f = 0


app = Ursina()




#filters = CommonFilters(base.win, base.cam)
#manager = FilterManager(win, cam)

window.borderless = False

scene.fog_density = 0.05
scene.fog_density = (5, 20)   # sets linear density start and end

window.color = color.dark_gray 

Entity.default_shader = lit_with_shadows_shader

noise = PerlinNoise(octaves=3, seed=randint(1,1000000000))


#lod = LODNode('LOD node 1')
#lod_np = NodePath(lod)
#lod_np.reparentTo(render)


#cTrav = CollisionTraverser()
#pusher = CollisionHandlerPusher()


#voxel_scene = Entity()

voxel_scene = Entity(model=Mesh(vertices=[], uvs=[]), collider = 'mesh')

#lod.addSwitch(50000.0, 0.0)
#voxel_scene.reparentTo(lod_np)

#voxel_scene.collider = 'mesh'


#removed load_texture
blocks = [
    0,
    load_texture("assets/grass.png"),
    load_texture("assets/soil.png"),
    load_texture("assets/stone.png"),
    load_texture("assets/wood.png")
]

block_id = 1

sky_texture = load_texture("assets/skybox-4k.jpg")


cube = 'cube'
sphere = 'sphere'


a = Audio('Art-Of-Silence_V2.mp3', pitch=1, loop=True, autoplay=True)
print(a.clip)
a.volume=1
b = Audio(a.clip)



pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))
AmbientLight(parent=pivot, color = color.rgba(100, 100, 100, 0.1))




#manager = FilterManager(base.win, base.cam)
#finalquad = manager.renderSceneInto()
#finalquad.setColor(0.95,0.9,1,1)

health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=100)


def update():

#    if held_keys['left mouse'] or held_keys['right mouse']:
#        Hand(block_id).active()
#    else:
#        Hand(block_id).passive()



	
    if held_keys['g']:
        save_game()

    if held_keys['shift'] and held_keys['w']:
        player.speed=10
        


    if held_keys['k']:
        Rocket()#voxel_scene.y += .1 * time.dt



key_f = 0


def input(key):
    
        global block_id, hand, key_f
        if key.isdigit():
            block_id = int(key)
            if block_id >= len(blocks):
                block_id = len(blocks) - 1
            Hand(texture = blocks[block_id])



        if key == '+' or key == '+ hold':
            health_bar_1.value += 10
        if key == '-' or key == '- hold':
            health_bar_1.value -= 10



                        
        if key == 'escape':
#            quit()
            player.enabled = False
            mainmenu = MainMenu(player)
            # application.pause

        if key == 'w':
            player.speed=5
        

           
        if (key == 'f' and key_f == 0):
            key_f = 1
            print("Enabling")
            inventory_enable()
        elif (key == 'f' and key_f == 1):
            key_f = 0
            print("Disabling")
            inventory_close()








        
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

#    def active(self):
#        self.position = Vec2(0.1, -0.5)
#        self.rotation = Vec3(90, -10, 0)

#    def passive(self):
#        self.rotation = Vec3(150, -10, 0)
#        self.position = Vec2(0.4, -0.4)



game_data = []

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = blocks[block_id], model = cube):
        super().__init__(
            parent=voxel_scene,
            model=model,
            color=color.white,
            highlight_color=color.lime,
            texture=texture,
            position=position,
            origin_y=0.5,
            shader=lit_with_shadows_shader,
            #collider="mesh"
        )
        #voxel_scene.model.vertices.extend(self.model.vertices)
        

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                
                model = cube

                voxel = Voxel(position=self.position + mouse.normal, texture = blocks[block_id])
                pos = self.position + mouse.normal
                game_data.append([(pos.x,pos.y,pos.z),blocks[block_id], model])

            if key == 'right mouse down':
                destroy(self)

#if key == 'escape':
#                quit()


class Rocket(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.speed = 0
        self.height = 30

        self.gravity = 0
        self.grounded = False
        self.jump_height = 20
        self.jump_up_duration = 5
        self.fall_after = 5.5 # will interrupt jump up
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

        if self.gravity:
            # gravity
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= self.height:
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
        rocket.animate_y(rocket.y+self.jump_height, self.jump_up_duration+0.1, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)



    def start_fall(self):
        rocket.y_animator.pause()
        self.jumping = False
        
def save_game():
    print("Saving")
    with open("game_stage.pickle", "wb") as file_:
        pickle.dump(game_data, file_, -1)

def load_basic_game():
#    for z in range(-20,15):
#        for x in range(-20,15):
            #for y in range(-4,4):
#                voxel = Voxel((x, 0, z))


    for z in range(50):
        for x in range(50):
            y = noise([x * 0.02,z * 0.02])
            y = math.floor(y * 7.5)
            voxel = Voxel(position=(x,y,z))

            game_data.append([(x, y, z),blocks[block_id], cube])

#    voxel_scene.collider = 'mesh' # call this only once after all vertices are set up


def load_saved_game():
    saved_game = pickle.load(open("game_stage.pickle", "rb", -1))
    for data in saved_game:
        #print(data)
        voxel = Voxel(data[0], texture = data[1])#, model = data[2])
        game_data.append(data)

#    voxel_scene.collider = 'mesh' # call this only once after all vertices are set up

if os.path.isfile("game_stage.pickle"):
    load_saved_game()
else:
    load_basic_game()
    save_game()


key_f = 0
rocket = Entity(model='cube', collider='box', color = color.red)

#player = FirstPersonController(model='cube', collider='box', z=-10, color=color.rgba(0,0,0,.3),)
player = FirstPersonController()
#EditorCamera()
window.exit_button.visible = False
Sky(texture=sky_texture)


#filters.setCartoonInk()



app.run()

