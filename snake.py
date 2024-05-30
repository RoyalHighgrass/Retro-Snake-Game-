import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define game constants
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Define the snake's initial position and direction
snake_x = WINDOW_WIDTH // 2
snake_y = WINDOW_HEIGHT // 2
snake_dx = SNAKE_SIZE
snake_dy = 0
snake_segments = [(snake_x, snake_y)]

# Generate the initial food position
food_x = random.randrange(SNAKE_SIZE, WINDOW_WIDTH - SNAKE_SIZE, SNAKE_SIZE)
food_y = random.randrange(SNAKE_SIZE, WINDOW_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)

# Initialize the score
score = 0

# Game loop
running = True
paused = False
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_p:
                paused = not paused
            elif not paused:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if snake_dy == 0:  # Prevent the snake from moving back onto itself
                        snake_dx = 0
                        snake_dy = -SNAKE_SIZE
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if snake_dy == 0:  # Prevent the snake from moving back onto itself
                        snake_dx = 0
                        snake_dy = SNAKE_SIZE
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if snake_dx == 0:  # Prevent the snake from moving back onto itself
                        snake_dx = -SNAKE_SIZE
                        snake_dy = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if snake_dx == 0:  # Prevent the snake from moving back onto itself
                        snake_dx = SNAKE_SIZE
                        snake_dy = 0

    # Move the snake
    if not paused:
        snake_x += snake_dx
        snake_y += snake_dy

        # Check for collisions with the food
        if snake_x == food_x and snake_y == food_y:
            score += 5
            food_x = random.randrange(SNAKE_SIZE, WINDOW_WIDTH - SNAKE_SIZE, SNAKE_SIZE)
            food_y = random.randrange(SNAKE_SIZE, WINDOW_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
        else:
            snake_segments.pop()  # Remove the last segment if not eating food

        # Insert the new position of the snake's head
        snake_segments.insert(0, (snake_x, snake_y))

        # Check for collisions with the snake's body or the window edges
        if (snake_x < 0 or snake_x >= WINDOW_WIDTH or
            snake_y < 0 or snake_y >= WINDOW_HEIGHT or
            (snake_x, snake_y) in snake_segments[1:]):
            running = False

    # Clear the window
    window.fill(BLACK)

    # Draw the snake
    for segment in snake_segments:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(window, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, GREEN)
    window.blit(score_text, (360, 10))

    # Draw instructions
    font = pygame.font.Font(None, 25)
    score_text = font.render(f"'w' or 'up', 's' or 'down', 'a' or 'left' & 'd' or 'right' to move around. Press 'P' to pause the game.", True, GREEN)
    window.blit(score_text, (20, 575))    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
