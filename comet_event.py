import pygame
from comet import Comet

# créer une classe pour gérer cet événement à interval régulier
class CometFallEvent:
  
    # lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 8
        self.fall_mode = False

        # définir un groupe de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()
        self.game = game

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 20
        for i in range(1, 20):
            # apparaitre une première boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'événement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True # activer l'événement

    def update_bar(self, surface):

        # ajouter du pourcentage à la barre
        self.add_percent()

        # barre noir en arrière plan
        pygame.draw.rect(surface, (32, 37, 30), [
        0, # l'axe des abcisses
        surface.get_height() - 20, # l'axe des ordonnées
        surface.get_width(), # longueur de la fenêtre
        20 # l'épaisseur de la barre
        ])
        # barre rouge jauge d'event
        pygame.draw.rect(surface, (232, 31, 31), [
        0, # l'axe des abcisses
        surface.get_height() - 20, # l'axe des ordonnées
        (surface.get_width() / 100) * self.percent, # longueur de la fenêtre
        20 # l'épaisseur de la barre
        ])
