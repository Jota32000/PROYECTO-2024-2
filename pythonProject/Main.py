import pygame, sys
from pygame.locals import *

def draw_filled_figure(surface, color, rect):
    x, y, width, height = rect
    line_spacing = 1  # Espacio entre lineas

    # Dibuja lineas horizontales
    for i in range(y, y + height, line_spacing):
        pygame.draw.line(surface, color, (x, i), (x + width, i))

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

fullscreen = False

while True:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

    black_color = (200, 200, 200)
    light_color = (222, 222, 222)
    red_color = (255, 0, 0)
    blue_color = (0, 0, 255)

    # fondo protoboard y canal central
    draw_filled_figure(screen, light_color, (50, 110, 760, 440)) # x, y, width, height
    draw_filled_figure(screen, black_color, (50, 320, 760, 20)) # x, y, width, height

    #lineas divisoras de buses / pistas
    pygame.draw.line(screen, black_color, (50,170), (810,170)) #170
    pygame.draw.line(screen, black_color, (50, 490), (810, 490))

    # polos +- arriba
    pygame.draw.line(screen, red_color, (80, 160), (780, 160))
    # faltan los hoyos de y=530 (puntos por poner) le di 10 de separacion
    pygame.draw.line(screen, blue_color, (80, 118), (780, 118))

    #polos +- abajo
    pygame.draw.line(screen, red_color, (80, 540), (780, 540))
    #faltan los hoyos de y=530 (puntos por poner) le di 10 de separacion
    pygame.draw.line(screen, blue_color, (80, 500), (780, 500))


    pygame.display.update()
    mainClock.tick(60)