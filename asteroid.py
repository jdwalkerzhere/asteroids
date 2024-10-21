from circleshape import CircleShape
from constants import *
import pygame
import random


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

    def split(self):
        # Remove current asteroid from all sprite groups
        self.kill()

        # If the asteroid was already too small, just exit
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generating new trajectories and sizes
        new_angle = random.uniform(20, 50)
        new_vec_a = self.velocity.rotate(new_angle)
        new_vec_b = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Adding the two new asteroids
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)

        # Adding velocities and increasing speed
        asteroid_a.velocity = new_vec_a * 1.2
        asteroid_b.velocity = new_vec_b * 1.2

