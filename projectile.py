import pygame


class Projectile1(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.y = player.rect.y

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity
        
        # Check if projectile touch
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # Deal damage
            monster.damage(self.player.attack)

        # Check if projectile is inside the screen
        if self.rect.y < -20:
            self.remove()
