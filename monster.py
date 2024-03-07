import pygame
import random


# Create a monster
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        size = random.randint(40, 90)
        self.game = game
        if size < 60:
            self.health = 1
            self.max_health = 1
        else:
            self.health = 2
            self.max_health = 2
        self.image = pygame.transform.scale(pygame.image.load('assets/alien2.png'), (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1400)
        self.rect.y = -600 + random.randint(0, 350)
        self.velocity = 3
        self.move = 0

    def respawn(self):
        self.rect.x = random.randint(0, 1500)
        self.rect.y = -120 + random.randint(0, 90)
        self.health = self.max_health

    def damage(self, amount):
        # Deal damage
        self.health -= amount
        if self.health <= 0:
            self.respawn()

    def forward(self):
        self.rect.y += self.velocity
        self.moving_right()
        if self.game.check_collision(self, self.game.all_players):
            self.game.player.damage()

        if self.rect.y > 850:
            self.velocity += 0.4
            self.respawn()

    def moving_right(self):
        if self.move < 80:
            self.move += 1
        else:
            self.rect.x += 0.5
