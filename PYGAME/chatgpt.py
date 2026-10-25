import pygame
import os

pygame.init()

# Screen settings
screen_width = 500
screen_height = 500

display_surface = pygame.display.set_mode(
    (screen_width, screen_height)
)
pygame.display.set_caption("Adding Images in Pygame")

# Find images relative to this Python script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

backdrop_path = os.path.join(BASE_DIR, "backdrop.png")
penguin_path = os.path.join(BASE_DIR, "penguin.png")

# Check whether image files exist
print("Script folder:", BASE_DIR)
print("Backdrop exists:", os.path.exists(backdrop_path))
print("Penguin exists:", os.path.exists(penguin_path))

# Load and scale background
backdropimg = pygame.transform.scale(
    pygame.image.load(backdrop_path).convert(),
    (screen_width, screen_height)
)

# Load and scale transparent penguin
penguinimg = pygame.transform.scale(
    pygame.image.load(penguin_path).convert_alpha(),
    (200, 200)
)

# Position penguin
penguin_rect = penguinimg.get_rect(
    center=(screen_width // 2, screen_height // 2 - 30)
)

# Create text
font = pygame.font.Font(None, 36)
txt = font.render(
    "hello world",
    True,
    pygame.Color("black")
)

txt_rect = txt.get_rect(
    center=(screen_width // 2, screen_height // 2 + 110)
)


def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw everything
        display_surface.blit(backdropimg, (0, 0))
        display_surface.blit(penguinimg, penguin_rect)
        display_surface.blit(txt, txt_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()