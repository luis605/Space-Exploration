'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from ursina import *


class Sound:
    def __init__(self):
        # Load sounds
        self.music = Audio('audio/lost_in_space.wav', pitch=1, loop=True, autoplay=False)
        print(self.music.clip)
        self.music.volume=0
        self.music_b = Audio(self.music.clip)
        self.music_b.volume = .3

        self.music.stop()
        self.music_b.stop()

        # Menu
        self.click = Audio('audio/effects/button.wav', pitch=1, loop=False, autoplay=False)
        print(self.click.clip)
        self.click.volume=0
        self.click_b = Audio(self.click.clip)
        self.click_b.volume = 1


    def others(self, player):
        self.player = player

        from direct.showbase import Audio3DManager
        audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)

        ###
        jumpSd = base.loader.loadSfx('assets/audio/effects/jump.mp3')
        menuSd = base.loader.loadSfx('assets/audio/effects/menu-pop.mp3')
        self.runningSd = loader.loadSfx('assets/audio/walk/grass_walk.wav')

        audio3d.attachSoundToObject(self.runningSd, self.player)

        self.runningSd.setLoop(True)
        self.runningSd.play()

        self.runningSd.stop()

        status = self.runningSd.status()
        print("Status: " + str(status))

        return self
