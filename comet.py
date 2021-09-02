import pygame
import random

# on créer une classe pour gérer cette comète
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # définir l'image associée à cette comète
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(-20, 950)
        self.rect.y = random.randint(-1500, -200)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play("meteorite")

        # vérifier si le nombre de comète est de 0
        if len(self.comet_event.all_comets) == 0:
            # l'event est fini
            print("event fini")
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les deux premiers monstres
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol :
        if self.rect.y >= 550:
            print("sol")
            self.remove()
    
        # si il n'y a plus de boule de feu sur le jeu
        if len(self.comet_event.all_comets) == 0:
            print("l'event est fini")
            # remettre la jauge au départ
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False

        # vérifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché")
            # retirer la boule de feu
            self.remove()
            # lui faire subir 20 points de dégats
            self.comet_event.game.player.damage(20)