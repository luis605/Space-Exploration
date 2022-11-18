'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

## NOT IN USE
from ursina import *

def load_game():

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
