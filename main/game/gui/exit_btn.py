'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *
from ursina.window import instance as window
from panda3d.core import GraphicsWindow


class ExitButton(Button):
    def __init__(self, **kwargs):
        super().__init__(
            name = 'exit_button',
            eternal = True,
            origin = (.5, .5),
            # text_origin = (-.5,-.5),
            position = window.top_right,
            z = -999,
            scale = (.05, .025),
            color = color.red.tint(-.2),
            text = 'x',
            **kwargs)


    def on_click(self):
        print("Exiting - Space Exploration")

        if window.windowed_position is not None:
            window.fullscreen = not window.fullscreen

        print("Finishing Application")
        base.destroy()
#        application.quit()


    def input(self, key):
        if held_keys['shift'] and key == 'q' and not mouse.right:
            self.on_click()


if __name__ == '__main__':

    '''
    This is the button in the upper right corner.
    You can click on it or press Shift+Q to close the program.
    To disable it, set window.exit_button.enabled to False
    '''
    app = Ursina()
    app.run()
