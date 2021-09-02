import pygame
from comet_event import CometFallEvent
from player import Player
from monster import Monster
from monster import Mummy
from monster import Alien
from sounds import SoundManager

# créer une seconde classe Game
class Game:

    def __init__(self):
        # définir si notre jeu a commencé ou non
        self.is_playing = False
        # générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'événement de cette pluie de comète
        self.comet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        # mettre le score à 0
        self.font = pygame.font.SysFont("Bauhaus 93", 40)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # remettre le jeu à neuf, retirer tous les monstres, remettre tout à nickel
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.score = 0
        self.sound_manager.play("game_over")

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # appliquer l'affichage du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie
        self.player.update_health_bar(screen)

        # actualiser la barre d'événement du jeu
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres de la partie
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # récupérer les comètes de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)
    
        # appliquer l'ensemble des images de mon groupe de météorites
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 917:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -37:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))