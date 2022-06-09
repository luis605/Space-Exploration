from ursina import *


class MessageBox(Entity):
    def __init__(self, text):

        Text.default_resolution = 1080 * Text.size


        self.archivement_txt = Text(text, position=(-0.30,0.4,0), color = color.red)
        size = self.archivement_txt.size
        print(size)

        size = 0.07
        
        self.archivement_txt.create_background(padding=size*2, radius = size,  color = color.rgba(39, 62, 69, 255))





if __name__ == "__main__":

    app = Ursina()
    
    MessageBox("aaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaa ")

    app.run()
