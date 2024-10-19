import pygame

from constants import *
from player import Player


def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1_000


if __name__ == '__main__':
    main()
