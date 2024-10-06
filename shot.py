import pygame
from circleshape import CircleShape
from constants import *
from AsteroidField import * 

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)  # Use SHOT_RADIUS for the radius
        self.velocity = velocity  # Velocity is passed from the Player class

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
        # Optionally, you might want to check if the shot goes off-screen and remove it.
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or 
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  # Remove the shot if it goes off-screen