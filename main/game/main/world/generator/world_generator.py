# Perlin Noise
from perlin_noise import PerlinNoise
from ursina import *


class Generate_Terrain:
    def __init__(self,xSize=0,zSize=0,freq=0,amp=0,octaves=0,seed=300,colorise=False):
        self.freq = freq
        self.amp = amp
        self.xSize = zSize
        self.zSize = xSize
        self.vert = 0
        self.vertices = []
        self.triangles = []
        self.uvs = []
        self.colors = []
        self.colorise = colorise
        self.noise = PerlinNoise(octaves=octaves, seed=seed)
        self.Generate_Mesh()
    def Generate_Mesh(self):
        #generate Vertices
        for z in range(self.zSize+1):
            for x in range(self.xSize+1):
                y = self.noise([x/self.freq, z/self.freq])*self.amp
                self.vertices.append(Vec3(x,y,z))
                if self.colorise == True:
                    if y > 15:
                        self.colors.append(color.white)
                    if y in range(5,15):
                        self.colors.append(color.light_brown)
                    if y in range(-5,5):
                        self.colors.append(color.green)

        #generate Triangles
        for z in range(self.zSize):
            for x in range(self.xSize):
                self.triangles.append(self.vert+0)
                self.triangles.append(self.vert+1)
                self.triangles.append(self.vert+self.xSize + 1)
                self.triangles.append(self.vert+1)
                self.triangles.append(self.vert+self.xSize + 2)
                self.triangles.append(self.vert+self.xSize + 1)
                self.vert+=1
            self.vert += 1
        #generate uvs
        for z in range(self.zSize+1):
            for x in range(self.xSize+1):
                self.uvs.append(Vec2(x/self.xSize,z/self.zSize))
    def Generate_World(self):
        model = Mesh(vertices=self.vertices, triangles=self.triangles,uvs=self.uvs,colors=self.colors)
        print(self.colors)
        return model
