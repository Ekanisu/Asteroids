from shot import Shot
import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_timer = 0

    def shoot(self):
        if self.shoot_timer == 0:# Create a vector pointing in the direction the player is facing
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED  # Set the velocity of the shot

        # Create a new shot at the player's position
            shot = Shot(self.position.x, self.position.y, velocity)

        # Add the shot to the shots group
            Shot.containers.add(shot)
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white = (255, 255, 255)  # Define the white color
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()

        # Decrease the shoot timer by dt, ensuring it doesn't go below 0
        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
