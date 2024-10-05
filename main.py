import pygame
from constants import * 
def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    while pygame.get_init == True:
        fill()
        display.flip()

   
if __name__ == "__main__":
    main()