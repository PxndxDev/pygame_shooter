import pygame
from projectile import Projectile
import animation

# créer une première classe qui va représenter notre joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def update_animation(self):
        self.animate()
  
    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (32, 37, 30), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (75, 207, 17), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        # démarrer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play("tir")

    def move_right(self):
        # si le joueur n'est pas en collision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity