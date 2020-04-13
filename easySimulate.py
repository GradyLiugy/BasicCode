import math
import random
import pygame


'''定义一些常量'''
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
sun_radius = 120
earth_radius = 30
moon_radius = 10
earth_angle = 90
moon_angle = 0


'''获得一个星星'''
def getStars():
    return (random.randint(1, 799), random.randint(1, 799), 2, 2)


'''模拟运动'''
def simulate():
    global earth_angle, moon_angle
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Model of Sun-Earth-Moon")
    clock = pygame.time.Clock()
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(BLACK)
        # 星星(更像太空一点)
        for i in range(100):
            pygame.draw.rect(screen, WHITE, getStars())
        # 太阳
        pygame.draw.circle(screen, RED, (400, 400), sun_radius)
        # 地球
        earth_position = (400 + int(250 * math.cos(math.radians(earth_angle))),\
                          400 + int(250 * math.sin(math.radians(earth_angle))))
        pygame.draw.circle(screen, BLUE, earth_position, earth_radius)
        earth_angle = (earth_angle + 1) % 360
        # 月亮
        moon_position = (earth_position[0] + int(50*math.sin(math.radians(moon_angle))),\
                         earth_position[1] + int(50*math.cos(math.radians(moon_angle))))
        pygame.draw.circle(screen, YELLOW, moon_position, moon_radius)
        moon_angle = (moon_angle + 12) % 360
        pygame.display.flip()


if __name__ == '__main__':
    simulate()