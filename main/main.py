'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# ursina
from ursina import *

from ursina.prefabs.health_bar import *
from ursina.shaders import camera_grayscale_shader
from ursina.shaders import unlit_shader

from ursina.prefabs.button_list import *

from ursina.lights import DirectionalLight as Ursina_DirectionalLight
from ursina.lights import AmbientLight as Ursina_AmbientLight

# panda3d
from direct.showbase.DirectObject import DirectObject
from direct.task import Task
from direct.actor.Actor import Actor
from direct.filter.CommonFilters import CommonFilters
from direct.filter.FilterManager import FilterManager

from pandac.PandaModules import *
from direct.gui.DirectGui import *

from panda3d import *
from panda3d.core import Vec3, NodePath, TextNode
from panda3d.core import Shader as Panda3dShader
from panda3d.core import PointLight as Panda3dPointLight

# random, os, pickle, etc
import pickle # added
import os # added
import logging
import numpy as np
import tkinter as tk
import sys

from threading import *
from random import uniform
from time import perf_counter
from math import sin, cos


# game modules
from game.gui.mainmenu import MainMenu
from game.gui.crafting import Crafting
from game.gui.exit_btn import ExitButton

from game.archivements.firstTime import FirstTime
from game.archivements.ten_minutes import TenMinutes

from game.graphics.shaders.lit_with_shadows_shader import *
from game.graphics.shaders.basic_lighting_shader import *
from game.graphics.fog import MyFog

from game.main.world.generator.world_generator import *
from game.main.world.lights.lighting import Lights
from game.main.world.skybox import Skybox

from game.main.bots.bots import AIPathFinder

from game.main.GameSystem.oxygen import SetOxygen
from game.main.GameSystem.health import SetHealth
from game.main.GameSystem.messageBox import MessageBox
from game.main.GameSystem.reportError import ReportError
from game.main.GameSystem.rocket import *
from game.main.GameSystem.sound import Sound
from game.main.GameSystem.physics import *
from game.main.GameSystem.version import *
from game.main.GameSystem.inventory import inventory
from game.main.GameSystem.MiningSystem import PickUp, MiningSystem
from game.main.GameSystem.BuildingSystem import BuildingSystem

from game.main.player.first_person_controller import FirstPersonController

from game.main.WindowConf import WindowConf
from game.main.StartUp import StartUp
from game.main.SpashScreen import SpashScreenInit

from speak import TextBubble
thread1 = StartUp(1)
thread1.start()


from panda3d.core import loadPrcFile

loadPrcFile("Config.prc")
PStatClient.connect()

try:

    # Variables                                
    key_f = 0
    key_esc = 0
    key_walk = 0
    fly_key = 0
    game_data = []

    distance_mouse_create = 0
    distance_mouse = 0

    DEVELOPER_MESSAGES = False
    REALISM = True
    FAST_MODE = True
    
    cube = 'cube'
    sphere = 'sphere'


    world_mesh = None



    

    # Start Game
    app = Ursina()

    thread1.close()# thread1.root.destroy()





    SpashScreenInit()

    # Version
    if DEVELOPER_MESSAGES:
        print("game version: ", game_version)

    # Window Configurations
    WindowConf()
    
    # Sky
    Skybox()

    # Setting up player
    player = FirstPersonController(model='assets/blend/player_test1.obj',
                                   origin = (0, -.5, 0),
                                   collider='mesh',
                                   scale = 1,
                                   color=color.rgb(0,0,0),
                                   rotation = Vec3(0,0,0),
                                   position=(2,3,2),
                                   shader = lit_with_shadows_shader,
                                   )

    # Fog
    scene.fog_density = 0.005
    scene.fog_color = color.rgb(60,60,70)

    application.development_mode = False

    # Shadows and shaders (Disabled globaly for performance impact)
    ## Entity.default_shader = lit_with_shadows_shader




    # Optimization
    voxel_scene = Entity(model=Mesh(vertices=[], uvs=[]), collider = 'mesh')
    holo_scene = Entity(model=Mesh(vertices=[], uvs=[]), collider = 'mesh')
    steps=[]
    

    # Filters
    if (REALISM):
        filters = CommonFilters(base.win, base.cam)
        filters.setBlurSharpen(.9)
        filters.setGammaAdjust(1.5)
        filters.setSrgbEncode()
        filters.setExposureAdjust(0)
        filters.setBloom(blend=(0.1,0.1,0.9,0.0), maxtrigger=1.5, intensity=0.6)
        
    

    # Textures
    global blocks, world_textures, block_id, valid_placable_blocks, valid_items, grass_texture


    blocks = [
        0,
        load_texture("assets/grass.png"),
        load_texture("assets/soil.png"),
        load_texture("assets/stone.png"),
        load_texture("assets/wood.png")
    ]

    world_textures = [
        load_texture("assets/images/world_textures/ground_grass.png"),
    ]

    block_id = 1

    valid_placable_blocks = [
        "grass.png",
        "soil.png",
        "stone.png",
        "wood.png",
    ]

    valid_mining_items = ["tree"]

    valid_items = [
        "grass_cutter",
    ]



    grass_texture = load_texture("assets/blend/vegetation/grass/grass_texture.png")




    
    # Inventory <Ui>
    from game.gui.inventory import *

    inventory_box = iPan
    inventory_bar = Hotspot

    inventory_bar.toggle()
    inventory_bar.toggle()

    crafting_box = Crafting(inventory, inventory_box)
    

    crafting_box.visible = False
    inventory_box.visible = False
    
    # Inventory <System>
    mylist = inventory.mylist
##    inventory.addItem("Olá do Outro Lado do Mundo")
    inventory.addItem("0")

    
    for i in range(len(blocks)):
        if DEVELOPER_MESSAGES:
            print(blocks[i])
##        if str(blocks[i]) == "soil.png":
        add_item(texture = str(blocks[i]))
##        inventory_bar.append(str(blocks[i]))
##        inventory_box.append(str(blocks[i]))




    ## [ ASPECT ] ##
    # Lights
    pivot = Entity()
    direc_light = Ursina_DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45), shadow_map_resolution = Vec2(1024, 1024))
    amb_light = Ursina_AmbientLight(parent=pivot, color = color.rgb(100, 100, 100), shadows = True)



    # Sound
    from game.main.GameSystem import globalSound

    music = globalSound.music
    music_b = globalSound.music_b

    sound = Sound()
    runningSd = sound.others(player).runningSd

    # Setting up ExitButton
    window.exit_button.enabled = False
    exit_button = ExitButton(music, player)
    exit_button.enabled = True


    # MainMenu
    mainmenu = MainMenu(player, music_b, direc_light, pivot, amb_light, inventory_bar, exit_button)
    mainmenu.disable()



##    Entity.default_shader = None
            


            

##    # Anti Alising
##    render.setAntialias(AntialiasAttrib.MAuto)



    # Animations
    player_walk = FrameAnimation3d('assets/blend/player_walk.obj',fps=1)
    rocket_entity = []


    trees = Entity(name = "trees")
    tree_colliders = Entity()


    #BOTS
    if not (FAST_MODE):
        friend = AIPathFinder(player)
        friend_run = friend.run()
        friend_text = friend.Text()









    def update():

        global key_walk, start_time, new_direction


        
            
    def input(key):
        
            global block_id, hand, key_f, key_esc, key_walk, fly_key, distance_mouse_create, distance_mouse

            # Inventory access.
            inv_input(key,player,mouse)
            
            ## Debug Options ##
            if (key == '+'):  ## Vertices Count
                number = 0
                for e in scene.children:
                    number_of_vertices = e.node().nested_vertices
                    number += number_of_vertices

                print("Scene Vertex Count: ",number)
                vertex_count_text = Text(text=("Scene Vertex Count: ", str(scene.node().nested_vertices)), wordwrap=30)
                invoke(destroy, vertex_count_text, delay=10)
                print(f"You have {len(scene.entities)} in you game")


            if (key == 'f2'):  ## Generate Error
                logging.exception("Generating Error:\n")
                generating_error

            if key == 'g':
                save_game()



            if key == 'scroll up':
                distance_mouse_create += 1


            if key == 'scroll down':
                distance_mouse_create -= 1


            if key == 'k':
                Rocket(rocket)
                            
            if key == 'escape' and key_esc == 0:
                key_esc = 1

                
                key_esc = 0
                mainmenu.enable()


                
            if held_keys['shift'] and (key == 'w' or key == 'a' or key == 'd' or key == 's'):
                    player.speed=10
                    
            elif (key == 'w' or key == 'a' or key == 'd' or key == 's'):
                player.speed=5


                if player.grounded == True:
                    step = Entity(parent=steps, model='plane', texture = 'images/player/footsteps.png', position=player.position, rotation=player.rotation)
                    steps.append(step)
                        
                    for i in range(len(steps)):
                        if i >= 50:
                            a = i-50
                            destroy(steps[a])
##                            steps[a].enabled = False
                            #steps[a].fade_out(value=0, duration=.05)
               
            if (key == 'f' and key_f == 0):
                key_f = 1
                if DEVELOPER_MESSAGES:
                    print("Enabling Inventory")
                inventory_enable()
            elif (key == 'f' and key_f == 1):
                key_f = 0
                if DEVELOPER_MESSAGES:
                    print("Disabling Inventory")
                inventory_close()




            if key == 'left mouse down':
                BuildingSystem.output_value = 0
                hit_info = raycast(camera.world_position, camera.forward)
                if isinstance(hit_info.entity, WorldMesh):
                    model = cube
                    if DEVELOPER_MESSAGES:
                        print("Creating Entity - on Voxel")
                    Voxel(model, position=mouse.world_point, texture = blocks[block_id])
                elif isinstance(hit_info.entity, Voxel):
                    model = cube
                    if DEVELOPER_MESSAGES:
                        print("Creating Entity - on Terrain")
                    Voxel(model, position=hit_info.entity.position + hit_info.normal, texture = blocks[block_id])

                    
            if key == 'right mouse down':
                hit_info = raycast(camera.world_position, camera.forward)
                if isinstance(hit_info.entity, Voxel):
                    destroy(hit_info.entity)


            if key == 'scroll up':
                
                distance_mouse += 0.2

                if distance_mouse >= 5:
                    distance_mouse = 5

                player.camera_pivot.y = distance_mouse


            if key == 'scroll down':
                distance_mouse -= 0.2

                if distance_mouse <= -5:
                    distance_mouse = -5

                player.camera_pivot.y = distance_mouse



            if key == 'o':
                player.camera_pivot.z = -1.5  # move the camera behind the player model
                player.camera_pivot.y = 3.5  # move the camera a little higher

            if key == 'm':
                player.camera_pivot.z = 0  # move the camera behind the player model
                player.camera_pivot.y = 0  # move the camera a little higher


            if key == "t":  # Teleport to Position Function
                def submit():
                    teleport_position = eval(position_field.text)

                    print(teleport_position)
                    player.enable()
                    player.position = teleport_position
                    destroy(position_field)
                    destroy(button)
                    
                player.disable()

                position_field = InputField(y=-.12, limit_content_to='0123456789,- ', color=color.gray.tint(-.4))
                button = Button('Teleport', scale=.1, color=color.cyan.tint(-.4), y=-.26, on_click=submit).fit_to_text()


  
            
    def inventory_close():
        inventory_bar.toggle()
        inventory_box.disable()
        player.enable()

        
    def inventory_enable():
        inventory_bar.toggle()
        inventory_box.enable()
        player.disable()




         
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



            
    class Hologram(Button):
        def __init__(self, model, position = mouse.world_point, color = color.rgba(68, 156, 255, 77)):
            super().__init__(
                parent=holo_scene,
                model=model,
                color=color,
                position=position,
                origin_y=0.5,
                collider=None
            )
            
##    class WorldMesh(Button):
##        def __init__(self, model, position = (0,0,0), texture = blocks[block_id]):
##            super().__init__(
##                parent=voxel_scene,
##                model=model,
##                color=color.white,
##                texture='grass',
##                position=position,
##                origin_y=0.5,
##                shader=lit_with_shadows_shader,
##                collider="mesh"
##            )


            

















    def save_game():
        print("Saving")
        with open("game_stage.pickle", "wb") as file_:
            pickle.dump(game_data, file_, -1)



    def load_basic_game():



##        world = Generate_Terrain(150,#xsize
##                                 150,#ysize
##                                 5,#frequency(how frequently new mountains generate)
##                                 5,#amplitude(how high or low the mountains will be)
##                                 1,#octaves(how many mountains there will be)
##                                 seed#seed(random number)
##                                )

        global world_mesh
        world_mesh = WorldMesh(generate_noise = True, shader = lit_with_shadows_shader)
        game_data.append(world_mesh)
        
        if DEVELOPER_MESSAGES:
            print("world", world_mesh)





    def load_saved_game():
        saved_game = pickle.load(open("game_stage.pickle", "rb", -1))
        for data in saved_game:
            if DEVELOPER_MESSAGES:
                print(data)#            rocket.animate_y(rocket.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)

            try:
                voxel = Voxel(data[2], data[0], texture = data[1])
            except TypeError:
##                world = Generate_Terrain(170,#xsize
##                                         170,#ysize
##                                         60,#frequency(how frequently new mountains generate)
##                                         5,#amplitude(how high or low the mountains will be)
##                                         1,#octaves(how many mountains there will be)
##                                         seed,#seed(random number)
##    
##                                         )
##                model = world.Generate_World()
                global world_mesh
                world_mesh = WorldMesh(texture = world_textures[0], shader = lit_with_shadows_shader)
                
                #world_model = WorldMesh(model, texture = 'grass.png')


            game_data.append(data)

    if os.path.isfile("game_stage.pickle"):
        load_saved_game()
    else:
        load_basic_game()
        save_game()

    print(world_mesh)



    vegetation_data = []

    vegetation_lod_i = 0


    lod = []
    lod_np = []

    no_shader = Panda3dShader.load(Panda3dShader.SL_GLSL,
                     vertex="no_shader.vert",
                     fragment="no_shader.frag")

    def Vegetation(lod_bool = False, model = None, model_medium = None, model_low = None, instance_to_collider = None, instance_model_to = None, collider = None, entity_texture = None, entity_color = None, cast_shadows = False):
            global vegetation_lod_i

            if (model == None):
                return


            tree_position_x = random.uniform(-world_mesh.scale_x/2,world_mesh.scale_x/2)
            tree_position_z = random.uniform(-world_mesh.scale_z/2,world_mesh.scale_z/2)
            tree_vec3_ray = Vec3(tree_position_x, 10, tree_position_z)
            
            direction=(0,-1,0)

            new_origin=Vec3(LVector3f(tree_vec3_ray)+LVector3f(0,3,0))-LVector3f(direction)
##
##            a = Entity(model='cube', color = color.blue, position = tree_vec3_ray)
##            b = Entity(model='cube', color = color.red, position = new_origin)
##            

            hit_info = raycast(tree_vec3_ray, direction=direction, ignore=())
            
            

            if hit_info and str(hit_info.entity) == "world_mesh":
                if DEVELOPER_MESSAGES:
                    print("HIT")

                    print(hit_info.world_point)

                for i in vegetation_data:
                    if i == hit_info.point:
                        Vegetation(model, texture)
                    else:
                        continue

                if (lod_bool):


                    """
                    DEBUG PSEUDOCODE:
                    create Entity called tree_collider

                    


                    """
                    if (collider != None):  # Check if should create collider
                        tree_collider = Entity(name=("tree"+str(vegetation_lod_i)), model=collider, color = color.rgba(0,0,0,0), position=(hit_info.world_point), collider="mesh")
##                        if (instance_to_collider != None):  # Check if can instance
##                            tree_collider.instanceTo(instance_to_collider)
                            
                    lod.append(LODNode('vegetation_node' + str(vegetation_lod_i)))
                    lod_np.append(NodePath(lod[vegetation_lod_i]))
                    lod_np[vegetation_lod_i].setPos(hit_info.world_point)

                    tree_low_detail = loader.loadModel(model_low)
                    lod[vegetation_lod_i].addSwitch(500.0, 90.0)
                    tree_low_detail.reparentTo(lod_np[vegetation_lod_i])

                    tree_medium_detail = loader.loadModel(model_medium)
                    lod[vegetation_lod_i].addSwitch(90.0, 30.0)
                    tree_medium_detail.reparentTo(lod_np[vegetation_lod_i])

                    tree_high_detail = loader.loadModel(model)
                    lod[vegetation_lod_i].addSwitch(30.0, 0.0)
                    tree_high_detail.reparentTo(lod_np[vegetation_lod_i])

                    if (cast_shadows == True):
                        lod_np[vegetation_lod_i].setShader(lit_with_shadows_shader_p3d)
                    if (entity_color != None):
                        lod_np[vegetation_lod_i].setColor(entity_color)
    ##                if (entity_texture != None):
    ##                    tex = loader.load3DTexture(entity_texture)
    ##                    lod_np[vegetation_lod_i].setTexture(tex)

                    if (instance_model_to != None):
                        lod_np[vegetation_lod_i].instanceTo(instance_model_to)
                    lod_np[vegetation_lod_i].reparentTo(render)
                    if (collider != None):
                        lod_np[vegetation_lod_i].instanceTo(tree_collider)
                    
                    vegetation_lod_i += 1

                else:

                    tree_collider = Entity(name="tree", model=collider, color = color.rgba(0,0,0,0), position=(hit_info.world_point), collider="mesh")
                    if (instance_to_collider != None):
                        tree_collider.instanceTo(instance_to_collider)
                        
                    tree = Entity(parent=trees, model=model, name="tree", color = entity_color, texture = entity_texture, position=(hit_info.world_point))
#                    if (cast_shadows):
                    tree_collider.shadows = False

                    vegetation_data.append(hit_info.world_point)
                    game_data.append(tree)
                    game_data.append(tree_collider)


            else:
                #if DEVELOPER_MESSAGES:
                    print("Didn't hit")

    tree_colliders = NodePath("Trees Collider")
    trees_instance = render.attachNewNode("Trees Instancing")

    
    for i in range(1,55):
        Vegetation(lod_bool = True,
                   model = 'assets/blend/vegetation/trees/tree.obj',
                   model_medium = 'assets/blend/vegetation/trees/tree_medium.obj',
                   model_low = 'assets/blend/vegetation/trees/tree_low.obj',
                   collider = "assets/blend/vegetation/trees/tree_collider.obj",
                   instance_to_collider = tree_colliders,
                   instance_model_to = None, #trees_instance,
                   entity_texture = None,
                   entity_color = color.red,
                   cast_shadows = True,
                   )

    bush2_colliders = Entity()
    for i in range(1,55):
        Vegetation(lod_bool = True,
                   model = 'assets/blend/vegetation/bush/bush2.obj',
                   model_medium = 'assets/blend/vegetation/bush/bush2_medium.obj',
                   model_low = 'assets/blend/vegetation/bush/bush2_low.obj',
                   instance_to_collider = bush2_colliders,
                   entity_texture = None,
                   collider = False,
                   entity_color = color.rgb(92, 0, 109),
                   cast_shadows = False,
                   )

    for i in range(1,100):
        Vegetation(model = 'assets/blend/vegetation/grass/grass_1.gltf', entity_texture = grass_texture, entity_color = color.green)

        
##
##    rocket = Voxel('assets/blend/player_test1.obj', [10,10,0],None)
##
##
##    EditorCamera()



    #ARCHIVEMENTS
    FirstTime()
    TenMinutes()
       


    # Game System
    health_bar = SetHealth()
    SetOxygen(health_bar)


    MiningSystem(player, inventory, add_item, valid_mining_items, vegetation_lod_i, lod_np)








    
except Exception as e:
    logging.exception(e)
    mouse.locked = False
    ReportError(e)

app.run()
