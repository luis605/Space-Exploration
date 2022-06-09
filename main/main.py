'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# ursina
from ursina import *

from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import *
from ursina.shaders import camera_grayscale_shader

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
from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape


# random, os, pickle, etc
import pickle # added
import os # added
from threading import *
import logging
import numpy as np
import sys

from random import randint,randrange
from time import perf_counter
from math import sin, cos


# game modules
from game.gui.mainmenu import MainMenu
from game.gui.inventory import Inventory

from game.archivements.firstTime import FirstTime
from game.archivements.ten_minutes import TenMinutes

from game.graphics.shaders.lit_with_shadows_shader import *
from game.graphics.fog import MyFog

from game.main.world.generator.world_generator import Generate_Terrain
from game.main.world.lights.lights import Lights
from game.main.world.skybox import Skybox

from game.main.bots.bots import AIPathFinder

from game.main.GameSystem.oxygen import SetOxygen
from game.main.GameSystem.health import SetHealth
from game.main.GameSystem.messageBox import MessageBox
from game.main.GameSystem.reportError import ReportError
from game.main.GameSystem.rocket import *
from game.main.GameSystem.sound import Sound
from game.main.GameSystem.inventory_bar import InventoryBar
from game.main.GameSystem.physics import *
from game.main.GameSystem.version import *

from game.main.WindowConf import WindowConf
from game.main.StartUp import StartUp

thread1 = StartUp(1)
thread1.start()

try:
        
    # Variables                                
    key_f = 0
    key_esc = 0
    key_walk = 0
    fly_key = 0
    game_data = []

    distance_mouse_create = 0

    cube = 'cube'
    sphere = 'sphere'

    # Start Game
    app = Ursina()

    thread1.close()# thread1.root.destroy()
    
    print("game version: ", game_version)


    # Window Configurations
    WindowConf()
    
    # Sky
    Skybox()

    #Setting up player
    player = FirstPersonController(model='assets/blend/player_test1.obj',
                                   collider='mesh',
                                   scale = 1,
                                   color=color.rgba(0,0,0,.3),
                                   rotation = Vec3(0,0,0),
                                   position=(2,3,2))



    # Fog
    MyFog()

    # Shadows and shaders
    Entity.default_shader = lit_with_shadows_shader

    # Perlin Noise
    seed=randint(1,1000000000)


    # Optimization
    voxel_scene = Entity(model=Mesh(vertices=[], uvs=[]), collider = 'mesh')



    # Filters
    filters = CommonFilters(base.win, base.cam)
##    filters.setHighDynamicRange()
##    filters.setInverted()

    # Inventory
    inventory = InventoryBar()
    
    blocks = [
        0,
        load_texture("assets/grass.png"),
        load_texture("assets/soil.png"),
        load_texture("assets/stone.png"),
        load_texture("assets/wood.png")
    ]

    for i in range(len(blocks)):
        print(blocks[i])
        inventory.append(str(blocks[i]))
    block_id = 1


    #Sound
    sound = Sound(player)

    runningSd = sound.runningSd
    music = sound.music
    music_b= sound.music_b


    # Lights
    Lights()
    pivot = Lights().pivot
    direc_light = Lights().direc_light
    amb_light = Lights().amb_light



    # Animations
    player_walk = FrameAnimation3d('assets/blend/player_walk.obj',fps=1)
    rocket_entity = []

    # Oxygen
    oxygen = SetOxygen().oxygen


    trees = Entity()


    def Vegetation():
            tree_position_x = random.randrange(3,50)
            tree_position_y = random.randrange(3,50)
            tree_vec3 = Vec3(tree_position_x, 0, tree_position_y)
            
            origin = tree_vec3  # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
            hit_info = raycast(origin , tree_vec3, ignore=(player,), distance=.5, debug=False)
            if not hit_info.hit:
                print(dir(hit_info.distance))
                print(hit_info.point)
                tree = Entity(parent=trees, model='assets/blend/vegetation/tree.obj', color = color.red, position=(tree_vec3))#, collider="mesh")
                game_data.append(tree)
            else:
                print("HIT")

    for i in range(1,25):
        Vegetation()
        
    
    def update():

    #    print(mouse.hovered_entity)

        global key_walk, start_time, new_direction




##
##        steps = Entity(parent=steps, model='plane', color = color.red, position=player.position, rotation=player.rotation)









        if held_keys['g']:
            save_game()

        if held_keys['shift']:
            player.speed=10
            

        if held_keys['w'] and key_walk == 0:
            key_walk = 1

            runningSd.setPlayRate(1.0)
            runningSd.setTime(1)
            runningSd.play()
        elif held_keys['w'] and key_walk == 1:
            key_walk = 0

            runningSd.setPlayRate(1.0)
            runningSd.setTime(1)
            runningSd.stop()


        
            
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

            


##
##            if key == 'v':
##                a.fade_out(duration=4, curve=curve.linear)
##
##            if key == 'b':
##                a.fade_in(value=1, duration=.5, delay=0, curve=curve.in_expo, resolution=None, interrupt='finish',)


            if key == 'k':
                Rocket(rocket)
                            
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
        print("oi")
        
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

                        # If block attach to other block, then save it on rocket_entity (Colliding)
                        game_data.append([model, (pos.x,pos.y,pos.z),blocks[block_id]])

                        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
                        hit_info = raycast(origin , self.position, ignore=(self,), distance=.5, debug=False)

                        if not hit_info.hit:
                            print("Ok")#if [model, (pos.x,pos.y,pos.z)]
                        else:
                            print("hoho")
                            rocket_entity.append([model, (pos.x,pos.y,pos.z),blocks[block_id]])
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
        print("world", world)
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
                world = Generate_Terrain(70,#xsize
                                         70,#ysize
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


    #rocket = Voxel("1.blend", [0,0,0],None)
    #rocket = Voxel(cube, [0,0,0],None)

    rocket = Voxel('assets/blend/player_test1.obj', [10,10,0],None)

    window.exit_button.visible = False

##    EditorCamera()



    #ARCHIVEMENTS
    FirstTime()
    TenMinutes()
       

    #BOTS
    AIPathFinder(player)


    # Game System
    SetOxygen()
    SetHealth()

except Exception as e:
    print(e)
    logging.exception(e)
    try:
        player.enabled = False
    except:
        pass
    ReportError(e)

try:
    app.run()
except Exception as e:
    print(e)
    ReportError(e)
