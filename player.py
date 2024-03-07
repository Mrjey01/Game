import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 1
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(pygame.image.load('assets/rocket/ShipA.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 600

    def damage(self):
        self.game.game_over()

    def launch_projectile(self, side):
        projectile = Projectile(self)
        projectile.rect.x = self.rect.x + side
        self.all_projectiles.add(projectile)

    def move(self, direction):
        if direction == 'right':
            self.rect.x += self.velocity
        elif direction == 'left':
            self.rect.x -= self.velocity
