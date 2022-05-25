from ursina import *
from ursina.prefabs.health_bar import *

from direct.task.Task import Task


from game.main.GameSystem.health import SetHealth

class SetOxygen:
    def __init__(self):
        print("Setting up oxygen")

        self.oxygen = HealthBar(position = (-.48 * window.aspect_ratio, -.42), bar_color=color.blue.tint(-.25), roundness=.2, value=50)

        print("Setting up taskMgr to exygen")

        # Tasks
        taskMgr.add(self.update, 'updateOxygen')

        
    def update(self, task):
        #self.oxygen.value -= 0.00005

        if self.oxygen.value <= 0:
            self.oxygen.value = 0
                #SetHealth().health_bar_1.value -= 0.01
        else:
            self.oxygen.value -= 0.5

            
