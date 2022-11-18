'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *


class MessageBox(Entity):
    def __init__(self, text):

        Text.default_resolution = 1080 * Text.size


        self.message_box = Text(text, position=(-0.30,0.4,-100), color=color.red)
        size = self.message_box.size
        #print(size)

        size = 0.07
        
        self.message_box.create_background(padding=size*2, radius = size,  color = color.rgba(39, 62, 69, 255))

        self.message_box.fade_out(value=0, duration=0,)
        self.message_box.fade_in(value=1, duration=1.5,)
        self.message_box.background.fade_out(value=0, duration=0,)
        self.message_box.background.fade_in(value=1, duration=.5,)

        self.message_box.fade_out(value=0, duration=1, delay=5)
        self.message_box.background.fade_out(value=0, duration=1, delay=5.5)

        destroy(self.message_box, delay=7)




if __name__ == "__main__":

    app = Ursina()
    
    MessageBox("Hello World ")

    app.run()
