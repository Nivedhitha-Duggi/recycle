import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recycle Game")

# Load images
backgrounds = ["assets/bg1.png", "assets/bg2.png", "assets/bg3.png"]
player_img = pygame.image.load("assets/player.png")
bottle_img = pygame.image.load("assets/bottle.png")
thorn_img = pygame.image.load("assets/thorn.png")

pygame.mixer.music.load("assets/bakground.mp3")

# Scale images
player_img = pygame.transform.scale(player_img, (80, 80))
bottle_img = pygame.transform.scale(bottle_img, (40, 40))
thorn_img = pygame.transform.scale(thorn_img, (40, 40))

# Define the player
player = player_img.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))

# Initialize variables
clock = pygame.time.Clock()
level = 0
score = 0
lives = 3
bottle_target = [20, 15, 10]
fall_speed = [5, 7, 10]  # Speed increases with each level
items = []
player_name = ""
game_summary = ""

def reset_level():
    """Reset the items for a new level."""
    global items
    items = []

def create_item():
    """Create a new falling item (bottle or thorn)."""
    x_pos = random.randint(0, SCREEN_WIDTH - 40)
    item_type = random.choice(["bottle", "thorn"])
    item = {
        "type": item_type,
        "rect": bottle_img.get_rect(topleft=(x_pos, -40)) if item_type == "bottle" else thorn_img.get_rect(topleft=(x_pos, -40))
    }
    items.append(item)

def move_items():
    """Move items down the screen."""
    for item in items:
        item["rect"].y += fall_speed[level]
    items[:] = [item for item in items if item["rect"].y < SCREEN_HEIGHT]

def check_collision():
    """Check for collisions between the player and items."""
    global score, lives
    for item in items[:]:
        if player.colliderect(item["rect"]):
            if item["type"] == "bottle":
                score += 1
            elif item["type"] == "thorn":
                lives -= 1
            items.remove(item)

def draw_text(text, x, y, size=36, color=WHITE):
    """Draw text on the screen."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def get_player_name():
    """Display a screen to take the player's name."""
    global player_name
    input_active = True
    user_text = ""

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_name = user_text
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        screen.fill(BLACK)
        draw_text("Enter Your Name:", 250, 200, 50, WHITE)
        pygame.draw.rect(screen, GRAY, pygame.Rect(250, 300, 300, 50))
        draw_text(user_text, 260, 310, 40, BLACK)
        pygame.display.flip()

def show_summary():
    """Display the game summary."""
    global game_summary
    screen.fill(BLACK)
    draw_text("Game Over", 300, 150, 60, WHITE)
    draw_text(f"Player: {player_name}", 300, 250, 50, WHITE)
    draw_text(f"Levels Completed: {level}", 300, 320, 50, WHITE)
    draw_text(f"Final Score: {score}", 300, 390, 50, WHITE)
    draw_text("Press Q to Quit", 300, 460, 40, WHITE)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()

# Main Game Loop
get_player_name()
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 8
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += 8

    # Create items periodically
    if random.randint(1, 30) == 1:
        create_item()

    # Move and check collisions
    move_items()
    check_collision()

    # Check for game over or level progression
    if lives <= 0:
        running = False
    elif score >= bottle_target[level]:
        level += 1
        if level == len(backgrounds):
            running = False
        else:
            reset_level()
            score = 0
    elif len(items) > 50:  # Too many uncollected items (optional rule)
        running = False

    # Draw game screen
    screen.blit(pygame.image.load(backgrounds[level]), (0, 0))
    screen.blit(player_img, player)
    for item in items:
        img = bottle_img if item["type"] == "bottle" else thorn_img
        screen.blit(img, item["rect"])
    draw_text(f"Level: {level + 1}", 10, 10)
    draw_text(f"Score: {score}/{bottle_target[level]}", 10, 50)
    draw_text(f"Lives: {lives}", 10, 90)

    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()
show_summary()
pygame.quit()
sys.exit()

