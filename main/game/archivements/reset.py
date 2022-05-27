from ursina import *


class Reset:
    def __init__(self):
        file = open("temp.txt", "a+")
        file.write("blabla is nothing.")
        file.close();

        def check_string():
            with open('temp.txt') as temp_f:
                datafile = temp_f.readlines()
            for line in datafile:
                if "reset" in line:
                    return True # The string is found
                else:
                    file = open("temp.txt", "a+")
                    file.write("reset")
                    return False  # The string does not exist in the file


        if check_string():
            print('True')
        else:
            print('False')
            self.on()


    def on(self):


        new_arc = Audio('new_archivement.wav', pitch=1, loop=False, autoplay=True)
        print(new_arc.clip)
        new_arc.volume=1
        new_arc_b = Audio(new_arc.clip)


        self.archivement = Entity(parent=camera.ui, model='quad', texture='assets/path31.png', scale=.08, position=(0.8,0.4,0))
        self.archivement.texture.set_pixel(0, 2, color.blue)
        self.archivement.texture.apply()

        self.archivement_txt =Text('<red>Reseted', position=(0.60,0.4,0), color = color.red)
        size = self.archivement_txt.size 
        self.archivement_txt.create_background(padding=size*2, radius=size, color=color.yellow)



        s = Sequence(
            15,
            Func(print, 'one'),
            Func(self.off)
            )

        s.start()

    def off(self):
        print("ooooooooooooooooO")
        self.archivement_txt.visible = False
        self.archivement.visible = False
