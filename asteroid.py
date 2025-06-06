import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
         super().__init__(x, y, radius)
    def draw(self, screen):
         pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.position)), self.radius, 2)
    def update(self, dt):
         self.position += (self.velocity * dt)
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_direction = random.uniform(20, 50)
        velocity_copy1 = self.velocity.copy() * 1.2
        velocity_copy2 = self.velocity.copy() * 1.2
        velocity_copy1 = velocity_copy1.rotate(new_direction)
        velocity_copy2 = velocity_copy2.rotate(-new_direction)
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = velocity_copy1
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = velocity_copy2
        self.kill()
