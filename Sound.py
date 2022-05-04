from pygame import mixer

class Sound():
    def __init__(self) -> None:
        mixer.pre_init(22050, -16, 1, 64)
        mixer.init()
        self.bgm = mixer.Sound('./bgm.mp3')
        self.bgm.set_volume(0.08)
        self.shoot = mixer.Sound('./pewpew.wav')
        self.shoot.set_volume(0.4)
        self.alien_explosion = mixer.Sound('./explosion.wav')
        self.alien_explosion.set_volume(0.4)
        self.levelUp = mixer.Sound('./powerUp.wav')
        self.levelUp.set_volume(0.5)
        self.scored = mixer.Sound('./scored.wav')
        self.scored.set_volume(0.2)
        self.revived = mixer.Sound('./revived.wav')
        self.revived.set_volume(0.4)