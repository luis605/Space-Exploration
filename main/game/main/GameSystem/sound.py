from ursina import *


class Sound:
    def __init__(self, player):

        self.player = player

        # Load sounds
        self.music = Audio('audio/Art-Of-Silence_V2.mp3', pitch=1, loop=True, autoplay=True)
        print(self.music.clip)
        self.music.volume=0
        self.music_b = Audio(self.music.clip)
        self.music_b.volume = 0

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
