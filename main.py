import pygame
from game import Game

pygame.init()

# Screen and background
SCREEN_SCALE = (1640, 780)
pygame.display.set_caption("Comet Fall")
SCREEN = pygame.display.set_mode(SCREEN_SCALE, pygame.FULLSCREEN)
BACKGROUND = pygame.transform.scale(pygame.image.load('assets/bg.jpg'), SCREEN_SCALE)
Y_BACKGROUND = 0
SCROLL_SPEED = 2

game = Game()

# Set up main menu
play_button = pygame.transform.scale(pygame.image.load('assets/play.png'), (400, 150))
play_button_rect = play_button.get_rect(center=SCREEN.get_rect().center)
exit_button = pygame.transform.scale(pygame.image.load('assets/exit.png'), (400, 150))
exit_button_rect = exit_button.get_rect(center=SCREEN.get_rect().center)
exit_button_rect.y += 200
save_pos_play = play_button_rect.x
save_pos_exit = exit_button_rect.x

# Running the game
RUNNING = True

# Score
SCORE = 0
FONT = pygame.font.Font(None, 36)
with open("best_score.txt", "r") as file:
    highscore = int(file.read())
    
def display_score():
    score_text = FONT.render("Score: " + str(SCORE), True, (255, 255, 255))
    SCREEN.blit(score_text, (10, 10))
    highscore_text = FONT.render("Highscore: " + str(highscore), True, (255, 255, 255))
    SCREEN.blit(highscore_text, (10, 50))


while RUNNING:
    for event in pygame.event.get():
        # Close the game
        if event.type == pygame.QUIT:
            RUNNING = False
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
                SCORE = 0
                # Play the game
                game.start()
            # Exit the game
            elif exit_button_rect.collidepoint(event.pos):
                RUNNING = False
                with open("best_score.txt", "w") as file:
                    file.write(str(highscore))
                # Quit the game
                pygame.quit()
                break

    if not RUNNING:  # Stop the game if closed
        break
    # Display background
    if game.is_playing:
        # Display background moving
        SCREEN.blit(BACKGROUND, (0, Y_BACKGROUND))
        SCREEN.blit(BACKGROUND, (0, Y_BACKGROUND - SCREEN_SCALE[1]))
        Y_BACKGROUND = (Y_BACKGROUND + SCROLL_SPEED) % SCREEN_SCALE[1]
        game.update(SCREEN)
        display_score()
        SCORE += 1
        # Hide menu buttons
        play_button_rect.x += 1000
        exit_button_rect.x += 1000
    else:
        play_button_rect.x = save_pos_play # Show menu buttons
        exit_button_rect.x = save_pos_exit
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(exit_button, exit_button_rect)  # Add play button
        SCREEN.blit(play_button, play_button_rect)  # Add exit button
        game.player.all_projectiles.empty()
        game.player.all_projectiles.draw(SCREEN)
        display_score()
        if SCORE > highscore:
            highscore = SCORE

    # Update background
    pygame.display.flip()
