import pygame
from constants import * 
from player import * 
from AsteroidField import *
from asteroid import *
from shot import *
import math

def check_circle_collision(obj1, obj2):
    """Check if two circular objects collide by comparing their distances and radii."""
    distance = math.sqrt((obj1.position.x - obj2.position.x) ** 2 + (obj1.position.y - obj2.position.y) ** 2)
    return distance < (obj1.radius + obj2.radius)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

     # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add the player to both groups
    updatable.add(player)
    drawable.add(player)

    AsteroidField.containers = updatable

    Asteroid.containers = (asteroids, updatable, drawable)

    Shot.containers = shots

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(0)

        dt = clock.tick(60) /1000

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                exit()

        for asteroid in asteroids:
            for shot in shots: 
                if check_circle_collision(asteroid, shot):
                    asteroid.split()
                    shot.kill()

        for shot in shots:  # Update and draw shots
            shot.update(dt)
            shot.draw(screen)

        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()

   
if __name__ == "__main__":
    main()