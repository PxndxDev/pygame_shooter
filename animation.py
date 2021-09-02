import pygame

# créer une nouvelle classe des animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # définir une méthode pour animer le sprite
    def animate(self, loop=False):

        # vérifier si l'animation est active pour cette entité
        if self.animation:

            # passer à l'image suivante
            self.current_image += 1

            # vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

                # vérifier si l'animation n'est pas en mode boucle
                if not loop:
                    # désactivation de l'animations
                    self.animation = False

        # modifier l'image de l'animation précédente par la suivante
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, self.size)

# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # récupérer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque fichier dans ce dossier pour les ajouter à la liste
    for _ in range(1, 24):
        image_path = path + str(_) + ".png"
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images

# définir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png, mummy2.png],
animations = {
  "mummy": load_animation_images("mummy"),
  "player": load_animation_images("player"),
  "alien": load_animation_images("alien")
}