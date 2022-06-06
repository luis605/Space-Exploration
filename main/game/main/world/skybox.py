from ursina import *

class Skybox(Entity):
    def __init__(self):
        # Sky
        self.sky_texture = load_texture("assets/skybox-4k.jpg")
        Sky(texture=self.sky_texture)
