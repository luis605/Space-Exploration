'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *

from panda3d import *

from direct.gui.DirectLabel import DirectLabel

class TextBubble(Entity):
    def __init__(self, text="life are the memories that are created until the last one is made", parent_to=None):
        super().__init__()

        parent_node = parent_to
        self.text = text
        height = 8

        self.speech_bubble = DirectLabel(
            parent=parent_node,
            text=self.text,
            text_wordwrap=10,
            relief=None,
            text_scale=(.5, .5),
            pos=(0, 0, height),
            frameColor=(.3, 0.2, .3, .5),
            text_frame=(0, 0, 0, 1),
            text_bg=(1, 1, 1, .4),
            )

        self.speech_bubble.component('text0'
                ).textNode.set_card_decal(1)
        self.speech_bubble.set_billboard_point_eye()
