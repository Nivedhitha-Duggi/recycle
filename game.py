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

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recycle Game")

# Load images
backgrounds = ["assets/bg1.png", "assets/bg2.png", "assets/bg3.png"]
player_img = pygame.image.load("assets/player.png")
bottle_img = pygame.image.load("assets/bottle.png")
thorn_img = pygame.image.load("assets/thorn.png")

# Initialize mixer for background music
pygame.mixer.init()
pygame.mixer.music.load("assets/bakground.mp3")  # Ensure correct path and file name
pygame.mixer.music.play(-1)  # Loop music infinitely


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

def draw_game():
    """Draw the game screen."""
    screen.blit(pygame.image.load(backgrounds[level]), (0, 0))
    screen.blit(player_img, player)
    for item in items:
        img = bottle_img if item["type"] == "bottle" else thorn_img
        screen.blit(img, item["rect"])
    draw_text(f"Level: {level + 1}", 10, 10)
    draw_text(f"Score: {score}/{bottle_target[level]}", 10, 50)
    draw_text(f"Lives: {lives}", 10, 90)

def draw_text(text, x, y):
    """Draw text on the screen."""
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Game loop
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
        print("Game Over! You ran out of lives.")
        running = False
    elif score >= bottle_target[level]:
        level += 1
        if level == len(backgrounds):
            print("Congratulations! You completed all levels!")
            running = False
        else:
            print(f"Level {level} completed! Get ready for Level {level + 1}!")
            reset_level()
            score = 0
    elif len(items) > 50:  # Too many uncollected items (optional rule)
        print("Game Over! Too many items missed.")
        running = False

    # Draw everything
    draw_game()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
