import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # initialize pygame
    pygame.init()

    # create game window and set window title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids!")

    clock = pygame.time.Clock()
    dt = 0

    # groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # create player and asteroids
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player_instance)
    drawable.add(player_instance)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    

    # Game loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update objects
        for obj in updatable:
            obj.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if player_instance.collide(asteroid):
                print("Game Over!")
                pygame.quit()
                quit()

        # draw objects
        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        
        # update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()