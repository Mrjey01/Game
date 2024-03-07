import pygame
from player import Player
from monster import Monster
from meteor import Meteor


class Game:

    def __init__(self):
        self.is_playing = False
        # Create player
        self.all_players = pygame.sprite.GroupSingle()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Create monster
        self.monster = Monster(self)
        self.meteor = Meteor(self)
        self.all_monsters = pygame.sprite.Group()
        self.all_meteors = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        for _ in range(10):
            self.spawn_monster()
        for _ in range(7):
            self.spawn_meteor()

    def game_over(self):
        # Restart the game, remove monster, projectiles and meteors, heal player, go to main menu
        self.is_playing = False
        self.all_monsters.empty()
        self.all_meteors.empty()
        self.player.all_projectiles.empty()

    def update(self, screen):
        # Display player
        self.all_players.draw(screen)

        # Display projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        # Display monster
        for monster in self.all_monsters:
            monster.forward()
        self.all_monsters.draw(screen)

        # Display meteor
        for meteor in self.all_meteors:
            meteor.forward()
        self.all_meteors.draw(screen)

        # Player movement
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move('right')
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move('left')

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def spawn_meteor(self):
        self.all_meteors.add(Meteor(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
