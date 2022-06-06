'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *
from ursina.prefabs.health_bar import *

import threading

 

 


class SetHealth(Entity):
    def __init__(self):
        self.health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=100)
        self.t=self.loop(self.update, 0.01)


    def loop(self, func, sec):
      def wrapper():
        self.loop(func, sec)
        func()
      self.t = threading.Timer(sec, wrapper)
      self.t.start()
      return self.t
        
    def update(self):
        if self.health_bar_1.value <= 10:
            print("OI")
            
            from ursina.shaders import camera_grayscale_shader
            camera.shader = camera_grayscale_shader
            
            self.t.do_run = False




if __name__ == "__main__":
    print("oi")

    app = Ursina()
    EditorCamera()



    SetHealth()

    health_bar_1 = SetHealth().health_bar_1

    a = Entity(model='quad', color = color.red)

    def input(key):
        if key == '+' or key == '+ hold':
            health_bar_1.value += 10
        if key == '-' or key == '- hold':
            health_bar_1.value -= 10

    app.run()
