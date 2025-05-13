import pygame
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from asteroid import*

pygame.init()
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

PLAYER = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroidfield = AsteroidField()

dt = 0
black = (0, 0, 0)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    for item in drawable:
        item.draw(screen)
    updatable.update(dt)

    for asteroid in asteroids:
        if PLAYER.collision(asteroid):
            print("Game over!")
            pygame.QUIT()

    for asteroid in asteroids:
        for shot in shots:
            if asteroid.collision(shot):
                asteroid.split()
                shot.kill()    
    
    pygame.display.flip()
    dt = CLOCK.tick(60) / 1000


