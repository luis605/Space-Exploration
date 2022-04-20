from ursina import *


class Inventory(Entity):
    def __init__(self):
        player.enabled = False
        super().__init__(
            parent = camera.ui
        )

        self.inventory_ui = Entity(parent = self,
            model = 'quad',
            scale = (.5, .8),
            origin = (-.5, .5),
            position = (-.3,.4),
            texture = 'white_cube',
            texture_scale = (5,8),
            color = color.dark_gray,
            enable = True
        )

        self.item_parent = Entity(parent=self.inventory_ui, scale=(1/5,1/8))
        
    def find_free_spot(self):                                                      
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]    
        for y in range(8):                                                         
            for x in range(5):                                                     
                if not (x,-y) in taken_spots:                                      
                    return (x,-y)                                                  


    def append(self, item):
        icon = Draggable(
            parent = Inventory().item_parent,
            model = 'quad',
            texture = item,
            color = color.white,
            origin = (-.5,.5),
            position = self.find_free_spot(),
            z = -.1,
            )
        name = item.replace('_', ' ').title()
        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0,0,0,.8)


        def drag():                                                     
            icon.org_pos = (icon.x, icon.y)                             

        def drop():
            icon.x = int(icon.x)
            icon.y = int(icon.y)



            '''if the spot is taken, swap positions'''
            for c in self.children:                                     
                if c == icon:                                           
                    continue                                            

                if c.x == icon.x and c.y == icon.y:                     
                    print('swap positions')                             
                    c.position = icon.org_pos                           


        icon.drag = drag                                                
        icon.drop = drop


