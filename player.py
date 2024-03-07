import pygame
from projectile1 import Projectile1
from projectile2 import Projectile2

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/rocket/F1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 600
        
    def launch_projectile(self):
        self.all_projectiles.add(Projectile1(self))
        self.all_projectiles.add(Projectile2(self))
        
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
