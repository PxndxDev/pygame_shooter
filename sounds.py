import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("C:\\Users\\eloua\\OneDrive\\Bureau\\Python\\shooter-pygame\\assets\\sounds\\click.ogg"),
            "game_over": pygame.mixer.Sound("C:\\Users\\eloua\\OneDrive\\Bureau\\Python\\shooter-pygame\\assets\\sounds\\game_over.ogg"),
            "meteorite": pygame.mixer.Sound("C:\\Users\\eloua\\OneDrive\\Bureau\\Python\\shooter-pygame\\assets\\sounds\\meteorite.ogg"),
            "tir": pygame.mixer.Sound("C:\\Users\\eloua\\OneDrive\\Bureau\\Python\\shooter-pygame\\assets\\sounds\\tir.ogg")
        }

    def play(self, name="click"):
        self.sounds[f"{name}"].play()