'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *
from ursina.prefabs.health_bar import *

from direct.task import Task



class SetHealth(HealthBar):
    def __init__(self):
        super().__init__(bar_color=color.lime.tint(-.25), color=color.red, roundness=.5, value=100, animation_duration=.20)
        self.text_entity.enabled = False
        text = Text(text="Health", parent=self, position = (0,3,0))
        
        taskMgr.add(self.drain, 'Drain Life')
        
    def drain(self, task):
        if self.value <= 10:
            print("Warning- Low Health")
            return Task.done
        else:
            self.value -= 0.0005
            return Task.cont
            



if __name__ == "__main__":
    print("oi")

    app = Ursina()
    EditorCamera()



    health_bar = SetHealth()


    a = Entity(model='quad', color = color.red)

    app.run()
