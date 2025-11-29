import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    

    running = True
    while running:
        log_state()

        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        player.update(dt)

        player.draw(screen)

        pygame.display.flip()

        
        
        


if __name__ == "__main__":
    main()

