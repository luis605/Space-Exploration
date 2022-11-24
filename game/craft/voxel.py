'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from ursina import *


class Voxel(Button):
    def __init__(self, model, game_data, position = (0,0,0), texture = blocks[block_id]):
        super().__init__(
            parent=voxel_scene,
            model=model,
            color=color.white,
            highlight_color=color.lime,
            texture=texture,
            position=position,
            origin_y=0.5,
            shader=lit_with_shadows_shader,
            collider="mesh"
        )

        self.game_data = self.game_data
        

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":

                if (blocks[block_id] == 5):
                    print("Lauching arrow")
                    player.arrow = duplicate(level.arrow, world_parent=level.bow, position=Vec3(-.2,0,0), rotation=Vec3(0,0,0))
                    player.arrow.animate('position', player.arrow.position+Vec3(0,0,-2), duration=.2, curve=curve.linear)

                else:
                    
                    model = cube

                    voxel = Voxel(model, position=self.position + mouse.normal, texture = blocks[block_id])
                    pos = self.position + mouse.normal
                    self.game_data.append([model, (pos.x,pos.y,pos.z),blocks[block_id]])

            if key == 'right mouse down':
                destroy(self)
