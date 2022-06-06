'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

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
        self.seeker = Entity(model = "cube", position = [0,0,100], scale=.3)

        # Target
##        self.target = loader.loadModel("models/arrow")
##        self.target.setColor(1,0,0)
##        self.target.setPos(self.player.position)
##        self.target.setScale(1)
##        self.target.reparentTo(render)

    def update(self, task):
##        self.target.setPos(self.player.position)

        self.seeker.add_script(SmoothFollow(target=self.player, speed=.004, offset = (1,2,0)))
        
        if distance(self.player, self.seeker) < self.radius:
            #self.seeker.lookAt(self.player)
            pass
        else:
            pass
        
        return task.cont

    def setAI(self):
        self.seeker.add_script(SmoothFollow(enabled = True, target=self.player, offset=[2, 1.5, 0], speed=.004))
        taskMgr.add(self.update,"Follow")
