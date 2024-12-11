import pygame
from constants import *
import player

def main():
    # initialize pygame
    pygame.init()

    # create game window and set window title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    clock = pygame.time.Clock()
    dt = 0

    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # clear the screen (fill with black color)
        screen.fill((0, 0, 0))

        # update player
        player_instance.update(dt)

        # # draw player
        # player_instance.draw(screen)

        # # update asteroids
        # # ...

        # # draw asteroids
        # for asteroid in asteroids:
        #     asteroid.draw(screen)

        # # update the display
        # pygame.display.flip()
        # dt = clock.tick(60) / 1000

        # # draw asteroids
        player_instance.draw(screen)
        
        # update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()