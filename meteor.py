import pygame
import random


class Meteor(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        size = random.randint(100, 150)
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load('assets/asteroids/meteor1.png'), (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1500)
        self.rect.y = -500 + random.randint(0, 300)
        self.velocity = 3

    def respawn(self):
        self.rect.x = random.randint(0, 1500)
        self.rect.y = -120 + random.randint(0, 90)

    def forward(self):
        self.rect.y += self.velocity
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage()

        if self.rect.y > 850:
            self.velocity += 0.2
            self.respawn()
