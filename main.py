import pygame
from constants import * 
from player import * 

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

    # Add the player to both groups
    updatable.add(player)
    drawable.add(player)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(0)

        dt = clock.tick(60) /1000

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

   
if __name__ == "__main__":
    main()