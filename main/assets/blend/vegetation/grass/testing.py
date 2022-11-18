from ursina import *
from ursina.prefabs import *

app = Ursina()

grass = Entity(model = 'grass_1.gltf')

EditorCamera()
app.run()
