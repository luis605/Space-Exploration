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
