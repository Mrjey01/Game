import pygame
from game import Game
pygame.init()

SCREEN_SCALE = (1540, 780)
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode(SCREEN_SCALE)
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, SCREEN_SCALE)

y_background = 0

game = Game()

running = True
while running:
    if y_background < 780:
        screen.blit(background, (0, y_background))
        screen.blit(background, (0, y_background - 780))
    else:
        screen.blit(background, (0, y_background))
        y_background = 0
    y_background += 0.5
    screen.blit(game.player.image, game.player.rect)
    # recupérer les projectile du joueur
    for projectile2 in game.player.all_projectiles:
        projectile2.move()
    
    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)
    
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
            
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            if game.pressed.get(pygame.K_SPACE):
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False