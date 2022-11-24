from ursina import *
import random as ra
import numpy as np

try:
    from game.main.GameSystem.inventory import inventory
except:
    import sys
    import os
    sys.path.append(os.path.join('..', 'main'))
    from GameSystem.inventory import inventory

if __name__ == '__main__':
    app = Ursina()


hotspots=[]
items=[]

# Inventory hotbar.
hotbar = Entity(model='quad',parent=camera.ui)
# Set the size and position.
hotbar.scale_y=0.08
hotbar.scale_x=0.68
hotbar.y=-0.45 + (hotbar.scale_y*0.5)
# Appearance.
#hotbar.color=color.yellow
hotbar.render_queue=0
hotbar.visible=False

# Inventory main panel.
iPan = Entity(model='quad',parent=camera.ui)
# Set the size and position.
iPan.rows=3
iPan.scale_y=hotbar.scale_y * iPan.rows
iPan.scale_x=hotbar.scale_x
iPan.basePosY=hotbar.y+(hotbar.scale_y*0.5)+(iPan.scale_y*0.5)
iPan.gap=hotbar.scale_y
iPan.y=iPan.basePosY+iPan.gap
# Appearance.
#iPan.color=color.light_gray
iPan.render_queue=0
iPan.visible=False

class Hotspot(Entity):
    # Fix size of hospot to height of hotbar.
    scalar=hotbar.scale_y*0.9
    # How many hotspots to fit across hotbar?
    rowFit=9
    def __init__(self):
        super().__init__()
        self.model=load_model('quad',use_deepcopy=True)
        self.parent=camera.ui
        self.scale_y=Hotspot.scalar
        self.scale_x=self.scale_y
        self.color=color.white
##        self.texture='brick'
        self.render_queue=1

        self.onHotbar=False
        self.visible=False
        self.occupied=False
        # What item are we hosting?
        self.item=None
    
    @staticmethod
    def toggle():
        if iPan.visible:
            iPan.visible=False
        else:
            iPan.visible=True
        # Toggle non-hotbar hotspots and their items.   
        for h in hotspots:
            # Gameplay mode? I.e. not visible?
            if not h.visible and not h.onHotbar:
                # Inventory mode.
                h.visible=True
                if h.item:
                    h.item.visible=True
                    # Enable item?
            elif not h.onHotbar:
                # Gameplay mode.
                h.visible=False
                if h.item:
                    h.item.visible=False
                    # Disable item?


class Item(Draggable):
    def __init__(self, texture):

        item_quant = texture
        if (texture.replace('.png', '') == '../../assets/images/items/wooden_planks'):
            item_quant = 'grass_cutter'

            
        super().__init__(
            text = "hi",
            text_origin=(-.5,.5),
        )

        print("Text", self.text)
        
        self.model=load_model('quad',use_deepcopy=True)
        self.scale_x=Hotspot.scalar*0.9
        self.scale_y=self.scale_x
        self.color=color.white
        self.texture=texture

        self.render_queue=2
        
        self.onHotbar=False
        self.visible=False
        self.currentSpot=None

    
    def fixPos(self):
        # Look through all the hotspots.
        # Find the unoccupied hotspot that is closest.
        # If found, copy that hotspot's position.
        # Set previous hotspot host to unoccupied.
        # Download item's blocktype info etc. into
        # host hotspot -- so that subject can use item.
        # !?! Can't find an available hotspot?
        # Return to current host position.

        closest=-1
        closestHotty=None
        for h in hotspots:
            if h.occupied: continue
            # Found a unoccupied hotspot :)
            # How close is it?
            dist=h.position-self.position
            # Find the magnitude - i.e. distance.
            dist=np.linalg.norm(dist)
            if dist < closest or closest == -1:
                # We have a new closest!
                closestHotty=h
                # Always remember to set current record!
                closest=dist
        # Finished iterating over hotspots.
        if closestHotty is not None:
            # We've found an available closest :)
            self.position=closestHotty.position
            # Update new host's information about item.
            closestHotty.occupied=True
            closestHotty.item=self
            # Update previous host-spot's status.
            if self.currentSpot:
                self.currentSpot.occupied=False
                self.currentSpot.item=None
            # Finally, update current host spot.
            self.currentSpot=closestHotty
        elif self.currentSpot:
            # No hotspot available? Just move back.
            self.position=self.currentSpot.position

    def drop(self):
        self.fixPos()

# Hotspots for the hotbar.
for i in range(Hotspot.rowFit):
    bud=Hotspot()
    bud.onHotbar=True
    bud.visible=True
    bud.y=hotbar.y
    padding=(hotbar.scale_x-bud.scale_x*Hotspot.rowFit)*0.5
    bud.x=  (   hotbar.x-hotbar.scale_x*0.5 +
                Hotspot.scalar*0.5 + 
                padding +
                i*bud.scale_x
            )
    hotspots.append(bud)

# Hotspots for the main inventory panel.
for i in range(Hotspot.rowFit):
    for j in range(iPan.rows):
        bud=Hotspot()
        bud.onHotbar=False
        bud.visible=False
        # Position.
        padding_x=(iPan.scale_x-Hotspot.scalar*Hotspot.rowFit)*0.5
        padding_y=(iPan.scale_y-Hotspot.scalar*iPan.rows)*0.5
        bud.y=  (   iPan.y+iPan.scale_y*0.5 -
                    Hotspot.scalar*0.5 -
                    padding_y -
                    Hotspot.scalar * j
                )
        bud.x=  (   iPan.x-iPan.scale_x*0.5 +
                    Hotspot.scalar*0.5 +
                    padding_x +
                    i*Hotspot.scalar
                )
        hotspots.append(bud)
# Main inventory panel items.
def add_item(texture = 'grass.png'):
    # Append item to inventory db
    inventory.addItem(texture.replace('.png', ''))

    # Create draggable item inside inventory menu
    bud=Item(texture)
    bud.onHotbar=True
    bud.visible=True
    bud.x=ra.random()-0.5
    bud.y=ra.random()-0.5
    bud.fixPos()
    items.append(bud)

    Hotspot.toggle()

for i in range(8):
    add_item()
##    
##for i in range(8):
##    inventory.addItem('grass')
##
##    bud=Item('grass.png')
##    bud.onHotbar=True
##    bud.visible=True
##    bud.x=ra.random()-0.5
##    bud.y=ra.random()-0.5
##    bud.fixPos()
##    items.append(bud)

# Make sure non-hotbar items are toggled off (invisible).
# Call this twice so that main inventory panel is
# invisible at the start, but that items inherit their
# non-hotbar status.
Hotspot.toggle()
Hotspot.toggle()


key_f = 1

def inv_input(key,subject,mouse):
    try:
        wnum = int(key)
        if wnum > 0 and wnum < 10:
            # Make sure no hotspots are highlighted.
            for h in hotspots:
                h.color=color.white
            # Adjust wnum to list indexing (1=0).
            wnum-=1
            hotspots[wnum].color=color.black
            # Is this hotspot occupied with an item?
            if hotspots[wnum].occupied:
                # Set subject's new blocktype from this item.
                subject.blockType=hotspots[wnum].item.blockType
                
    except:
        pass
        

def toggle_inventory(key, subject):
    global key_f
    # Pause and unpause, ready for inventory.
    if key=='f' and key_f == 0:
        key_f = 1
        # Inventory mode.
        Hotspot.toggle()
        iPan.disable()
        subject.disable()
    elif key=='f' and key_f == 1:
        key_f = 0
        # Gameplay mode.
        Hotspot.toggle()
        iPan.enable()
        subject.enable()

    
if __name__ == '__main__':
##    for i in range(8):
##        add_item_to_inventory('grass', texture='grass')
##        

    subject = Entity()
    def input(key):
        toggle_inventory(key, subject)
    app.run()
