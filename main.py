import pygame

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

    player = Player(
        x=SCREEN_WIDTH/2,
        y=SCREEN_HEIGHT/2,
        radius=PLAYER_RADIUS,
        containers=(updatable, drawable))

    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1_000


if __name__ == '__main__':
    main()
