import pygame

from constants import *


def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        pygame.display.flip()
        dt = clock.tick(60) / 1_000


if __name__ == '__main__':
    main()
