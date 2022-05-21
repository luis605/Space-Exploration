from ursina import *



class SpashScreenInit:
    def __init__(self):
        spash_screen_image = Entity(parent=camera.ui, model='quad', texture='assets/images/loading_screen/main_image.png', scale_x=1.777)
        spash_screen_image.fade_out(delay=1.5, duration=1, curve=curve.linear)
