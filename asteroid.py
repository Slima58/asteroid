import random
import pygame
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return "This was a small asteroid"
        else: 
            random_angle = random.uniform(20, 50)
            velocity = self.velocity * 1.2
            nrad = self.radius - ASTEROID_MIN_RADIUS
            self.kill()
            for i in range(-1,2,2):
                asteroid = Asteroid(self.position.x, self.position.y, nrad )
                asteroid.velocity = velocity.rotate(random_angle * i)
  
