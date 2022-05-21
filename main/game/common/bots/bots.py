from ursina import *

from pandac.PandaModules import *
from panda3d import *

class AIPathFinder:
    def __init__(self, player):
        
        self.player = player
        self.radius = 30
        self.cam_x = 0
        self.persue = False
        #
        self.loadModels()
        self.setAI()
        


    def loadModels(self):
        # Seeker
        self.seeker = Entity(model = "cube", position = [0,0,140], scale=.3)

        # Target
##        self.target = loader.loadModel("models/arrow")
##        self.target.setColor(1,0,0)
##        self.target.setPos(self.player.position)
##        self.target.setScale(1)
##        self.target.reparentTo(render)

    def update(self, task):
        radius = 30
##        self.target.setPos(self.player.position)

        
        if self.player.getDistance(self.seeker) < radius:
            self.seeker.lookAt(self.player)  
            self.seeker.add_script(SmoothFollow(enabled = True, target=self.player, offset=[2, 1.5, 0], speed=.004))
        else:
            self.seeker.add_script(SmoothFollow(enabled = False, target=self.player, speed=0))


        return task.cont

    def setAI(self):
        taskMgr.add(self.update,"Follow")