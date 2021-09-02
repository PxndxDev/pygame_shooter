import pygame
import random
import animation


# créer une classe qui va gérer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # vérifier si son nouveau nombre de point de vie est inférieur ou égal à 0
        if self.health <= 0:
            # réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)
            self.game.add_score(self.loot_amount)

            # si la barrae d'événement est chargée à son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la méthode pour essayer de déclancher la pluie
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (32, 37, 30), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (75, 207, 17), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        # le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec un joueur
        else: 
            # infliger des dégats (au joueur)
            self.game.player.damage(self.attack)

# définir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(10)

# définir une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(20)
