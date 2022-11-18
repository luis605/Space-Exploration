'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


from ursina import *
import logging

'''
1.) [ DONE ] Create an Entity
2.) [ DONE ] Rotate it when player is near
3.) [ DONE ] If player is very near, destroy Entity and add item to inventory
'''
class PickUp(Entity):
    def __init__(self, player, inventory, add_item_to_inventory, item_name, model='cube', texture=None, position=(0,0,0)):
        super().__init__(
            model='cube', texture=texture, position = position
        )
        self.player = player
        self.inventory = inventory
        self.add_item_to_inventory = add_item_to_inventory
        self.item_name = item_name
        
    def update(self):
        # Rotate when player is near
        if (distance(self, self.player) > 50):
            return

        self.rotation_y += 25 * time.dt


        # If player is very near, then procede to collection
        if (distance(self, self.player) < 2):
            destroy(self)
            print("NAME", self.item_name)
            self.inventory.addItem(self.item_name)
            
            self.add_item_to_inventory(self.item_name)



'''
1.) [ DONE ] If key 'c' pressed:
    - [ DONE ] Check if mouse is houvering an entity, otherwise, return
    - [ DONE ] If mouse.hovered_entity is a valid block to mine, otherwise, return
    - Starts Mining:
        - [ DONE ] Check if player is in a certain distance to allow mining, otherwise, return
        - [ DONE ] Remove Entity
        - [ DONE ] Create PickUp at the entity position (x,y) and z (raycast.hit_position.z)
        
'''
class MiningSystem(Entity):
    def __init__(self, player, inventory, add_item_to_inventory, valid_mining_items, vegetation_lod_i, lod_np):
        super().__init__()
        self.pickup_enabled = False

        self.player = player
        self.inventory = inventory
        self.add_item_to_inventory = add_item_to_inventory
        self.valid_mining_items = valid_mining_items
        self.vegetation_lod_i = vegetation_lod_i
        self.lod_np = lod_np
        
    def input(self, key):
        # Check If Mining System was called
        if not (key == 'c'): return

    
        hovered_entity = mouse.hovered_entity
        if (hovered_entity == None):
            print("Error: Cannot mine due to a not detection of an Entity")
            return


        for i in range(len(self.valid_mining_items)):
            try:
                if not (str(self.valid_mining_items[i]) == str(hovered_entity.name[0:4])):
                    return
                
                else:
                    print("MINING")

                    if not (distance(hovered_entity.position, self.player) < 15):
                        return

                    else:
                        x = hovered_entity.world_x
                        z = hovered_entity.world_z

                        name = hovered_entity.name
                        if (name[0:4] == "tree"):
                            name = "wood"


                        try:
                            for i in range(self.vegetation_lod_i):
                                if (str(hovered_entity.name.replace('tree', '')) == str(self.lod_np[i]).replace('render/vegetation_node', '')):
                                    print("REMOVING 2")
                                    hovered_entity.removeNode()
                                    self.lod_np[i].removeNode()

                        except Exception as e:
                            logging.exception(e)

                        self.hit_information = raycast(Vec3(x, 10, z), direction=Vec3(0,-1,0), distance=100, debug=True)
                        print(self.hit_information.world_point)
                        
                        self.pickup_enabled = True
                        PickUp(self.player, self.inventory, self.add_item_to_inventory, name, model='cube', texture='grass', position = self.hit_information.world_point)
                                
            except Exception as e:
                logging.exception(e)


            
                        
            



