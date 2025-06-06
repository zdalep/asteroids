import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.position)), self.radius, 0)
    def update(self, dt):
        self.position += (self.velocity * dt)
