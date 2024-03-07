import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 30
        self.image = pygame.transform.scale(pygame.image.load('assets/projectile.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.y = player.rect.y

    def move(self):
        self.rect.y -= self.velocity

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.kill()
            monster.damage(self.player.attack)

        # Check if projectile is inside the screen
        if self.rect.bottom <= 0:
            self.kill()
