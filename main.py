import pygame
from game import Game

pygame.init()

# Screen and background
SCREEN_SCALE = (1640, 780)
pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode(SCREEN_SCALE, pygame.FULLSCREEN)
background = pygame.transform.scale(pygame.image.load('assets/bg.jpg'), SCREEN_SCALE)

game = Game()

# Set up main menu
play_button = pygame.transform.scale(pygame.image.load('assets/play.png'), (400, 150))
play_button_rect = play_button.get_rect(center=screen.get_rect().center)
exit_button = pygame.transform.scale(pygame.image.load('assets/exit.png'), (400, 150))
exit_button_rect = exit_button.get_rect(center=screen.get_rect().center)
exit_button_rect.y += 200
save_pos_play = play_button_rect.x
save_pos_exit = exit_button_rect.x

# Running the game
running = True
y_background = 0
scroll_speed = 2
score = 0
font = pygame.font.Font(None, 36)
with open("best_score.txt", "r") as file:
    highscore = int(file.read())


def display_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    highscore_text = font.render("Highscore: " + str(highscore), True, (255, 255, 255))
    screen.blit(highscore_text, (10, 50))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            with open("best_score.txt", "w") as file:
                file.write(str(highscore))
            pygame.quit()
            break

        # Launch projectile
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile(70)
                game.player.launch_projectile(0)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if cursor is on play button
            if play_button_rect.collidepoint(event.pos):
                score = 0
                # Launch the game
                game.start()
            elif exit_button_rect.collidepoint(event.pos):
                running = False
                with open("best_score.txt", "w") as file:
                    file.write(str(highscore))
                # Quit the game
                pygame.quit()
                break

    if not running:  # Stop the game if closed
        break
    # Display background
    if game.is_playing:
        # Display background moving
        screen.blit(background, (0, y_background))
        screen.blit(background, (0, y_background - SCREEN_SCALE[1]))
        y_background = (y_background + scroll_speed) % SCREEN_SCALE[1]
        game.update(screen)
        display_score()
        score += 1
        # Display menu buttons
        play_button_rect.x += 1000
        exit_button_rect.x += 1000
    else:
        play_button_rect.x = save_pos_play
        exit_button_rect.x = save_pos_exit
        screen.blit(background, (0, 0))
        screen.blit(exit_button, exit_button_rect)  # Add play button
        screen.blit(play_button, play_button_rect)  # Add exit button
        game.player.all_projectiles.empty()
        game.player.all_projectiles.draw(screen)
        display_score()
        if score > highscore:
            highscore = score

    # Update background
    pygame.display.flip()
