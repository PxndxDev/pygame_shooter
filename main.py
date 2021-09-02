import pygame
import math
from game import Game
pygame.init()

# définir une clock
clock = pygame.time.Clock()
FPS = 120


# générer la fenêtre de notre jeu
pygame.display.set_caption("Shooter Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger le fond d'écran
background = pygame.image.load('assets/bg.jpg')

# importer et charger la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer notre bouton pour lancer la partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.95)

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vraie
while running:

    # appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, -200))

    # vérifier si notre jeu a commencé ou non
    if game.is_playing:
        # déclancher les instructions de la partie
        game.update(screen)
    # vérifier si notre jeu n'a pas commencé
    else: 
        # ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'événement est la fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si la touche espace est entrée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # lancer le jeu
                    game.start()
                    # jouer le son
                    game.sound_manager.play("click")


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton "jouer"
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()
                # jouer le son
                game.sound_manager.play("click")

    # fixer le nombre de FPS sur ma clock
    clock.tick(FPS)