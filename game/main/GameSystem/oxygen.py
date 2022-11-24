'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *
from ursina.prefabs.health_bar import *

from direct.task import Task


if __name__ == '__main__':
    from health import SetHealth
else:
    from game.main.GameSystem.health import SetHealth

class SetOxygen(HealthBar):
    def __init__(self, healthBar):
        super().__init__(position = (-.48 * window.aspect_ratio, -.42),
                         bar_color=color.blue.tint(-.25),
                         roundness=.2,
                         value=50,
                         )
        
        print("Setting up oxygen")
        self.healthBar = healthBar

        

        taskMgr.add(self.drainO2, 'Drain Life')

    
    def drainO2(self, task):
        
        if self.value >= .2:
            self.value -= 0.0005
        else:
            self.healthBar.value -= 0.1

        return Task.cont
    
        #return Task.cont
            
if __name__ == '__main__':
    app = Ursina()
    health_bar = SetHealth()
    SetOxygen(health_bar)

    app.run()
