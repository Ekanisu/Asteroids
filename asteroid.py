import pygame
import random
from circleshape import CircleShape
from constants import *
from AsteroidField import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):

        self.position += self.velocity * dt

    def split(self):

        self.kill()



        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle for splitting
        random_angle = random.uniform(20,50)


        # Create two new velocity vectors by rotating the current velocity
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids at the current position with the new radius
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity_1

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_velocity_2

        for container in Asteroid.containers:
            container.add(asteroid_1)
            container.add(asteroid_2)




    
   
