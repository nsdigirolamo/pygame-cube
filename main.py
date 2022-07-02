import sys

import pygame as pygame

from point import Point
from cube import Cube, draw_cube
from camera import Camera

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 900
CENTER_X = SCREEN_WIDTH / 2
SCREEN_HEIGHT = 600
CENTER_Y = SCREEN_HEIGHT / 2
LARGE_FONT_SIZE = int(SCREEN_WIDTH * 0.03)
SMALL_FONT_SIZE = int(SCREEN_WIDTH * 0.015)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    camera = Camera(Point(0, 0, 0), 1000)  # camera is positioned at origin and viewport is a plane at (1000, 0, 0)
    cube = Cube(Point(3000, 0, 0), 1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        translate_speed = 10
        if pygame.key.get_pressed()[pygame.K_w]:
            cube.translate(translate_speed, 0, 0)
        if pygame.key.get_pressed()[pygame.K_s]:
            cube.translate(-translate_speed, 0, 0)

        draw_cube(cube, camera, screen)
        cube.rotate_z(0.001)

        pygame.display.update()
        screen.fill(BLACK)
