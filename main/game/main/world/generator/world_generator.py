'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


# Perlin Noise
import noise
from PIL import Image, ImageDraw
from ursina import *

import random
import numpy as np


class Generate_Terrain_Noise:
    def __init__(self):
        shape = (1024,1024)
        scale = .5
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        seed = np.random.randint(0,100)

        world = np.zeros(shape)

        # make coordinate grid on [0,1]^2
        x_idx = np.linspace(0, 1, shape[0])
        y_idx = np.linspace(0, 1, shape[1])
        world_x, world_y = np.meshgrid(x_idx, y_idx)

        # apply perlin noise, instead of np.vectorize, consider using itertools.starmap()
        world = np.vectorize(noise.pnoise2)(world_x/scale,
                                world_y/scale,
                                octaves=octaves,
                                persistence=persistence,
                                lacunarity=lacunarity,
                                repeatx=1024,
                                repeaty=1024,
                                base=seed)

        # here was the error: one needs to normalize the image first. Could be done without copying the array, though
        img = np.floor((world + .5) * 255).astype(np.uint8) # <- Normalize world first
        Image.fromarray(img, mode='L').save("PerlinNoise.png", "PNG")



class WorldMesh(Entity):
    def __init__(self, texture='PerlinNoise', position=(0,-30,0), generate_noise = False, shader = None):
        if generate_noise:
            Generate_Terrain_Noise()
        super().__init__(
            model=Terrain('PerlinNoise', skip=8),
            scale=(470, 20, 470),
            texture_scale=(30,30),
            position=position,
            texture=texture,
            collider = 'mesh',
            shader = shader,
        )

        # [ Optimise ] #
        ## Chucking

        grid = [[None for z in range(80)] for x in range(80)] # make 2d array of entities 
        x_slices = 80 
        z_slices = 80 
        self.model.generated_vertices = [v+Vec3(.5,0.5) for v in self.model.generated_vertices]


class CreateSampleEntities():
    def __init__(self):
        self.collider = 'cube'
        self.model = 'cube'
        self.scale = 8
        self.cast_shadows = True
        self.trees = Entity()

        for i in range(100):
            self.generate()

    def generate(self):
        tree_position_x = random.uniform(0, 100)
        tree_position_z = random.uniform(0, 100)
        tree_vec3_ray = Vec3(tree_position_x, 10, tree_position_z)
        
        direction=(0,-1,0)

        new_origin=Vec3(LVector3f(tree_vec3_ray)+LVector3f(0,3,0))-LVector3f(direction)

        a = Entity(model='cube', color = color.blue, position = tree_vec3_ray)
        b = Entity(model='cube', color = color.red, position = new_origin)
        

        hit_info = raycast(tree_vec3_ray, direction=direction, ignore=())
        
        tree_collider = Entity(name="tree", model=self.collider, color = color.rgba(0,0,0,0.5), position=(hit_info.world_point), collider=self.collider)

        tree = Entity(parent=self.trees, model=self.model, name="tree", color = color.random_color(), position=(hit_info.world_point))
        if (self.cast_shadows):
            tree_collider.shader = lit_with_shadows_shader
            
if __name__ == '__main__':
    from ursina.shaders import lit_with_shadows_shader
    import random
    game = Ursina()
    
    pivot = Entity()
    direc_light = DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45), shadow_map_resolution = Vec2(5024, 5024))

    EditorCamera()
    #Generate_Terrain()

    WorldMesh(generate_noise = True)
##    CreateSampleEntities()
    game.run()

##
##class Generate_Terrain:
##    def __init__(self,xSize=0,zSize=0,freq=0,amp=0,octaves=0,seed=300,colorise=False):
##        self.freq = freq
##        self.amp = amp
##        self.xSize = zSize
##        self.zSize = xSize
##        self.vert = 0
##        self.vertices = []
##        self.triangles = []
##        self.uvs = []
##        self.colors = []
##        self.colorise = colorise
##        self.noise = PerlinNoise(octaves=octaves, seed=seed)
##        self.collider = 'mesh'
##        self.Generate_Mesh()
##    def Generate_Mesh(self):
##        #generate Vertices
##        for z in range(self.zSize+1):
##            for x in range(self.xSize+1):
##                y = self.noise([x/self.freq, z/self.freq])*self.amp
##                self.vertices.append(Vec3(x,y,z))
##                if self.colorise == True:
##                    if y > 15:
##                        self.colors.append(color.white)
##                    if y in range(5,15):
##                        self.colors.append(color.light_brown)
##                    if y in range(-5,5):
##                        self.colors.append(color.green)
##
##        #generate Triangles
##        for z in range(self.zSize):
##            for x in range(self.xSize):
##                self.triangles.append(self.vert+0)
##                self.triangles.append(self.vert+1)
##                self.triangles.append(self.vert+self.xSize + 1)
##                self.triangles.append(self.vert+1)
##                self.triangles.append(self.vert+self.xSize + 2)
##                self.triangles.append(self.vert+self.xSize + 1)
##                self.vert+=1
##            self.vert += 1
##        #generate uvs
##        for z in range(self.zSize+1):
##            for x in range(self.xSize+1):
##                self.uvs.append(Vec2(x/self.xSize,z/self.zSize))
##    def Generate_World(self, collider='mesh'):
##        model = Mesh(vertices=self.vertices, triangles=self.triangles,uvs=self.uvs,colors=self.colors)
##        print(self.colors)
##        return model
