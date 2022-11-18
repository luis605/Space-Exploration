'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


from ursina import *

from game.main.GameSystem.messageBox import MessageBox



class Crafting(Entity):
    def __init__(self, inventory, inventory_box):
        super().__init__(
            parent = camera.ui,
        )
        self.main = Entity(parent=self, enable=True)
        self.image_folder = "../../assets/images/craftingSystem/logo/"
        self.items_image_folder = "../../assets/images/items/"
        self.inventory = inventory
        self.inventory_box = inventory_box
        print(inventory_box)

        # [ Name - ( {Items needed to craft, quantity, texture}) ]
        self.tools_info = [
            ['grass_cutter',[{'wood': 1,}], self.items_image_folder+'wooden_planks.png'],
        ]

        # Main Options
        

        ToolsBTN = Button(
            parent = self.main,
            icon = self.image_folder + "main/tools.png",
            radius = .3,
            color = color.rgba(0,0,0,0),
            highlight_color = color.rgba(100,100,100,125),
            highlight_scale = 1.1,
            scale_y = 0.1,
            scale_x = 0.1,
            y = 0.2,
            x = -0.7,
        )
        
        ToolsBTN.on_click = Func(self.tools)

    def tools(self):
        print("Opening Tools Option")
        GrassCutterBTN = Button(
            parent = self.main,
            icon = self.image_folder + "main/tools.png",
            radius = .3,
            color = color.rgba(0,0,0,0),
            highlight_color = color.rgba(100,100,100,125),
            highlight_scale = 1.1,
            scale_y = 0.1,
            scale_x = 0.1,
            y = 0.3,
            x = -0.5,
        )
        
        GrassCutterBTN.on_click = Func(self.give_item, 'tools', 'grass_cutter')

    def give_item(self, tool_type, item):
        # Check item type (tools, )
        # Iterate through names and then through items quantities

        quantity_needed = []
        quantity_get = []
        item_name = []

        can_craft = True

        # TODO: Get items from inventory
        if (tool_type == 'tools'):
            try:
                for a in self.tools_info:
                    if (a[0] == item):
                        print("Item to Craft", a[0])
                        i = 0
                        for b in a[1][0]:
                            #print(list(a[1][0].values())[i])
                            quantity_needed.append(list(a[1][0].values())[i])
                            quantity_get.append(self.inventory.getQuantity(b))
                            item_name.append(b)
                            
                            print ("Quantity Needed of", b, "is",  quantity_needed[i])
                            print ("Quantity Got", "is", quantity_get[i])

                            if not (quantity_needed[i] <= quantity_get[i]):
                                can_craft = False
                                print("Not enough ITEMS")
                                missing_item = b
                                raise StopIteration
                            
                            #self.inventory.displayInventory(self.inventory)
                            i += 1

                        for x in quantity_needed:
                            print(x)
                            for y in range(x):
                                self.inventory.removeItem(item_name[x-1])
                            print(a[2])
                            print("ITEM", item)
                            self.inventory.addItem(a[0])
                            self.inventory_box.append(str(a[2]))
                            
            except StopIteration:
                MessageBox("Not Enough "+b)
        
if __name__ == "__main__":
    app = Ursina()

    Crafting()

    app.run()
