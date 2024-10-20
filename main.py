import pygame

from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player


def main() -> None:
    # Initialize PyGame
    pygame.init()

    # Time keeping
    clock, dt = pygame.time.Clock(), 0

    # Set the PyGame Screen constants
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    # Make PyGame Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set up containers for game objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Set up player sprite
    player = Player(
        x=SCREEN_WIDTH / 2,
        y=SCREEN_HEIGHT / 2,
        radius=PLAYER_RADIUS)

    # Set up asteroid field
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
