import pygame
from constants import *

def main():
    # initialize pygame
    pygame.init()

    # create game window and set window title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    # Game loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # clear the screen (fill with black color)
        screen.fill((0, 0, 0))

        # # draw asteroids
        # pygame.draw.circle(screen, (255, 255, 255), (640, 360), 100)

        # update the display
        pygame.display.flip()

    # quit pygame
    pygame.quit()

    print("Asteroids game has ended.")
    print("Goodbye!")

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()