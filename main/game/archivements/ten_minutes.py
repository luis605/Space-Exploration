from ursina import *
from direct.task.Task import Task

import time



 
class TenMinutes(Entity):

    def __init__(self):

        file = open("temp.txt", "a+")
        #file.write("blabla is nothing.")
        file.close();

        def check_string():
            with open('temp.txt') as temp_f:
                datafile = temp_f.readlines()
            for line in datafile:
                if "ten minutes" in line:
                    return True # The string is found
                else:
                    return False  # The string does not exist in the file


        if check_string():
            print('True')
        else:
            print('False')

            self.start_on()






    def count_time(self, task):
        if task.time < 2.0:
            return Task.cont

        print('Done')
        
        file = open("temp.txt", "a+")
        file.write("ten minutes")

        self.on()
        
        return Task.done
        
        
    def start_on(self):
        self.start_time = time.perf_counter()
        print("10 Minutes", self.start_time)

        # Tasks
        taskMgr.add(self.count_time, 'countTime')



    def on(self):
##
##
##        new_arc = Audio('new_archivement.wav', pitch=1, loop=False, autoplay=True)
##        print(new_arc.clip)
##        new_arc.volume=1
##        new_arc_b = Audio(new_arc.clip)


        self.archivement = Entity(parent=camera.ui, model='quad', texture='assets/path31.png', scale=.08, position=(0.8,0.4,0))
        self.archivement.texture.set_pixel(0, 2, color.blue)
        self.archivement.texture.apply()

        self.archivement_txt =Text('<red>First Time', position=(0.60,0.4,0), color = color.red)
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

        

if __name__ == "__main__":
    TenMinutes()
