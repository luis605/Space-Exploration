main_tree = "game/graphics/shaders/"

if __name__ == '__main__':
    main_tree = ""


vert = open(main_tree + 'myshader.vert', "r")
frag = open(main_tree + 'myshader.frag', "r")


from ursina import *; lit_with_shadows_shader = Shader(language=Shader.GLSL,
                                                       vertex = vert.read(),                                                       
                                                       fragment = frag.read(),
                                                       default_input = {
                                                           'texture_scale': Vec2(1,1),
                                                           'texture_offset': Vec2(0,0),
                                                           'shadow_color' : Vec4(0, .5, 1, .25),
                                                           }
                                                       )

from panda3d.core import Shader as Panda3dShader


lit_with_shadows_shader_p3d = Panda3dShader.load(Panda3dShader.SL_GLSL,
                                                       vertex = vert.read(),                                                       
                                                       fragment = frag.read(),
                                                 )


vert.close()
frag.close()

if __name__ == '__main__':
    from ursina import *
    from ursina.prefabs.primitives import *
    # window.size *= .5
    app = Ursina()
    shader = lit_with_shadows_shader
    Entity.default_shader = shader

    a = Entity(model='sphere', color=color.light_gray)
    Entity(model='cube', color=color.white, scale=(10,1,10), y=-2, texture='white_cube')
    Entity(model='cube', color=color.gray, scale=(5,1,10), x=-3.5, y=-1)


    # Enable shadows; we need to set a frustum for that.
    from ursina.lights import DirectionalLight
    # sun = DirectionalLight(y=10, rotation=(90+30,90,0))
    sun = DirectionalLight()
    sun.look_at(Vec3(-1,-1,-1))
    # sun._light.show_frustum()

    Sky(color=color.light_gray)
    EditorCamera()

    def update():
        a.x += (held_keys['d'] - held_keys['a']) * time.dt * 5
        a.y += (held_keys['e'] - held_keys['q']) * time.dt * 5
        a.z += (held_keys['w'] - held_keys['s']) * time.dt * 5


    app.run()
