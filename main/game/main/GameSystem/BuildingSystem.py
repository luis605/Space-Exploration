'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *

class BuildingSystem(Entity):
    def __init__(self):
        super().__init__()
        self.output_value = 1

        for x in valid_placable_blocks:                    
            if str(blocks[block_id]) == x:
                if DEVELOPER_MESSAGES:
                    print("creating block hologram")
                
                model = 'cube'
                self.hologram = Hologram(model, position = mouse.world_point)

                self.block_update_task = taskMgr.add(self.taskFunc, "taskFunction")

    def taskFunc(self, task):
        print (self.output_value)
        
          
        mouse_point = mouse.world_point
        if DEVELOPER_MESSAGES:
            print(mouse_point)
        self.hologram.position = mouse_point

        if int(self.output_value) == 0:
            destroy(self.hologram)
            return task.done
        elif int(self.output_value) == 1:
            return task.cont
      

    def input(self, key):
        if key == 'left mouse down':
            self.output_value = 0

        
