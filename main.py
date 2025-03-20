import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    clock = pygame.time.Clock()
    dt = 0.016
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2,PLAYER_RADIUS)
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,color)
        pygame.display.flip()
        clock.tick(60)
        player.draw(screen)
        

if __name__ == '__main__':
    main()
