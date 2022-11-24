'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *

from pandac.PandaModules import *
from panda3d import *
from direct.gui.DirectLabel import DirectLabel

from speak import TextBubble


class AIPathFinder:
    def __init__(self, player):
        self.player = player
        self.radius = 30
        self.cam_x = 0
        self.persue = False

        
    def run(self):
        
        self.loadModels()
        self.setAI()

    def Text(self):
        self.bubbleText = TextBubble(text="Hello World", parent_to=self.seeker)##        text.setFrameColor(0, 0, 1, 1)

        return self.bubbleText

        
##        cardmaker = CardMaker('text')
##        card = NodePath(cardmaker.generate())
##        tnp = card.attachNewNode(text)
##        card.setEffect(DecalEffect.make())
##
##        card.setBillboardAxis()
##        card.setBillboardPointWorld()
##        card.setBillboardPointEye()
##
##        card.reparent_to(render)
##        card.setScale(.1, .1, .1)
##        card.setPos(player.x, player.y+2, player.z)

    def loadModels(self):
        # Seeker
        self.seeker = Entity(model = "cube", position = [0,0,100], scale=.3)


    def update(self, task):
        if distance(self.player, self.seeker) < self.radius:
            self.seeker.add_script(SmoothFollow(target=self.player, speed=.004, offset = (1,2,0)))
            self.seeker.lookAt(self.player)
            self.seeker.smooth_follow.speed=.004
        else:
            #print(self.seeker.scripts)
            pass
##            if ('smooth_follow' in self.seeker.scripts):
##                self.seeker.scripts.remove("SmoothFollow")
##                print("REMOVING SMOOTH FOLLOW")
##            else:
##                for item in self.seeker.scripts:
##                    print(item)
        
        return task.cont

    def setAI(self):
        self.seeker.add_script(SmoothFollow(enabled = True, target=self.player, offset=[2, 1.5, 0], speed=.004))
        taskMgr.add(self.update,"Follow")


    #
