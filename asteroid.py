from circleshape import CircleShape
from constants import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color='white',
            center=self.position,
            radius=self.radius,
            width=2)

    def update(self, dt):
        assert self.velocity, "Velocity not set before call to 'update'"
        self.position += self.velocity * dt
