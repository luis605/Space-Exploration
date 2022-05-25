from ursina import *
from ursina.prefabs.health_bar import *


class SetHealth:
    def __init__(self):
        self.health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=100)
