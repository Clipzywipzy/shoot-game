import pygame
import random

pygame.init()

# Set up the game window
screen_info = pygame.display.Info()
window_size = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(window_size, pygame.FULLSCREEN)
pygame.display.set_caption("B1ock Sh00ter")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Game states
MENU = 0
GAME = 1
END = 2
DRAWING = 3
SETTINGS = 4

# Player variables
player_w = 75
player_h = 75
player_x = window_size[0] // 2 - player_w // 2
player_y = window_size[1] - player_h
player_spd = 5

# Bullet variables
bullet_w = 5
bullet_h = 15
bullet_x = 0
bullet_y = window_size[1] - player_h
bullet_spd = window_size[0] // 500
bullet_stt = "ready"

# Block variables
blocks = []
block_w = 75
block_h = 75
block_spd = 2
block_tm = pygame.time.get_ticks()

# Score and font
score = 3
fnt = pygame.font.Font(None, 36)

# Tutorial steps and font
tutorial_steps = [
    "Use the left and right arrow keys to move the player.",
    "Press SPACE to shoot bullets at the falling blocks.",
    "Destroy blocks to score points. Avoid letting them hit the player.",
    "Click on blocks with the mouse to destroy them and earn additional points.",
    "Have fun and aim for a high score!"
]
tutorial_step_index = 0
tutorial_font = pygame.font.Font(None, 24)
show_tutorial = True

# Drawing app colors
drawing_colors = [RED, GREEN, BLUE]
current_color_index = 0

# Drawing app variables
drawing = False
prev_mouse_pos = (0, 0)

# Menu variables
menu_selection = 1
menu_difficulty = 4000  # Default difficulty (in milliseconds)
menu_color = RED  # Default block color

# Game state
game_state = MENU

def draw_menu():
    screen.fill(BLACK)
    title_text = fnt.render("B1ock Sh00ter", True, RED)
    start_text = fnt.render("1. Start Game", True, WHITE)
    settings_text = fnt.render("2. Settings", True, WHITE)
    screen.blit(title_text, (window_size[0] // 2 - title_text.get_width() // 2, window_size[1] // 2 - 100))
    screen.blit(start_text, (window_size[0] // 2 - start_text.get_width() // 2, window_size[1] // 2 - 50))
    screen.blit(settings_text, (window_size[0] // 2 - settings_text.get_width() // 2, window_size[1] // 2))

def draw_game():
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (player_x, player_y, player_w, player_h))
    if bullet_stt == "fire":
        pygame.draw.rect(screen, RED, (bullet_x, bullet_y, bullet_w, bullet_h))
    for block in blocks:
        pygame.draw.rect(screen, menu_color, (block[0], block[1], block_w, block_h))

    score_text = fnt.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # Display tutorial steps
    tutorial_text = tutorial_font.render(tutorial_steps[tutorial_step_index], True, RED)
    screen.blit(tutorial_text, (10, window_size[1] - 30))

def draw_end():
    screen.fill(BLACK)
    end_text = fnt.render("Game Over", True, RED)
    restart_text = fnt.render("Press Enter to Restart", True, WHITE)
    credit_text = fnt.render("End Credits: Brent Cessna", True, RED)
    screen.blit(end_text, (window_size[0] // 2 - end_text.get_width() // 2, window_size[1] // 2 - 50))
    screen.blit(credit_text, (window_size[0] // 2 - credit_text.get_width() // 2, window_size[1] // 2))
    screen.blit(restart_text, (window_size[0] // 2 - restart_text.get_width() // 2, window_size[1] // 2 + 50))

def draw_drawing_app():
    screen.fill(BLACK)
    drawing_text = fnt.render("Drawing App", True, RED)
    back_text = fnt.render("Press Enter to Go Back", True, WHITE)
    color_text = fnt.render("Click to Change Color", True, WHITE)
    current_color = drawing_colors[current_color_index]
    pygame.draw.rect(screen, current_color, (window_size[0] - 40, 10, 30, 30))
    screen.blit(drawing_text, (window_size[0] // 2 - drawing_text.get_width() // 2, window_size[1] // 2 - 100))
    screen.blit(back_text, (window_size[0] // 2 - back_text.get_width() // 2, window_size[1] // 2))
    screen.blit(color_text, (10, 10))

def draw_settings():
    screen.fill(BLACK)
    settings_text = fnt.render("Settings", True, RED)
    back_text = fnt.render("Press Enter to Go Back", True, WHITE)
    difficulty_text = fnt.render("1. Change Difficulty", True, WHITE)
    color_text = fnt.render("2. Change Block Color", True, WHITE)
    screen.blit(settings_text, (window_size[0] // 2 - settings_text.get_width() // 2, window_size[1] // 2 - 100))
    screen.blit(back_text, (window_size[0] // 2 - back_text.get_width() // 2, window_size[1] // 2))
    screen.blit(difficulty_text, (window_size[0] // 2 - difficulty_text.get_width() // 2, window_size[1] // 2 - 50))
    screen.blit(color_text, (window_size[0] // 2 - color_text.get_width() // 2, window_size[1] // 2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == DRAWING:
                if event.key == pygame.K_RETURN:
                    game_state = MENU
            elif game_state == MENU:
                if event.key == pygame.K_1:
                game_state = GAME
                elif event.key == pygame.K_2:
                    game_state = SETTINGS
            elif game_state == SETTINGS:
                if event.key == pygame.K_RETURN:
                    game_state = MENU

    if game_state == MENU:
        draw_menu()

    elif game_state == GAME:
        # Game logic
        # ...

        draw_game()

    elif game_state == END:
        draw_end()

    elif game_state == DRAWING:
        draw_drawing_app()

    elif game_state == SETTINGS:
        draw_settings()

    pygame.display.update()

pygame.quit()
