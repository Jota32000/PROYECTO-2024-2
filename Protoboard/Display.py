import pygame
import math

class Display:
    def __init__(self, conector):
        self.x = conector.x
        self.y = conector.y
        self.ancho = 150
        self.largo = 125
        self.c_cuerpo = (45, 55, 44)
        self.lado = 30
        self.pin1 = conector
        self.pin2 = None
        self.pin3 = None
        self.pin4 = None
        self.pin5 = None
        self.pin6 = None
        self.pin7 = None
        self.pin8 = None
        self.pin9 = None
        self.pin10 = None

    def dibujar(self, screen):
        x = self.x + 15
        y = self.y + 15
        horiz = 66
        vert = 61
        x_cir = x + 90
        y_cir = y + horiz + 50
        radio_circulo = 12

        for i in range(self.y, self.y + self.ancho):
            pygame.draw.line(screen, self.c_cuerpo, (self.x, i), (self.x + self.largo, i))

        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.largo, self.y), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo, self.y + self.ancho), (self.x, self.y + self.ancho), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.ancho), 3)

        color_a = (202, 0, 0) if self.pin4.fase else (214, 203, 203)
        color_b=(202, 0, 0) if self.pin5.fase else (214, 203, 203)
        color_c = (202, 0, 0) if self.pin9.fase else (214, 203, 203)
        color_d = (202, 0, 0) if self.pin7.fase else (214, 203, 203)
        color_e = (202, 0, 0) if self.pin6.fase else (214, 203, 203)
        color_f = (202, 0, 0) if self.pin2.fase else (214, 203, 203)
        color_g = (202, 0, 0) if self.pin1.fase else (214, 203, 203)
        color_p = (202, 0, 0) if self.pin10.fase else (214, 203, 203)

        pygame.draw.line(screen, color_a, (x, y), (x + vert, y), 5)  # a
        pygame.draw.line(screen, color_g, (x, y + 63), (x + vert, y + 63), 5)  # g
        pygame.draw.line(screen, color_d, (x, y + 126), (x + vert, y + 126), 5)  # d
        pygame.draw.line(screen, color_f, (x - 5, y), (x - 5, y + vert), 5)  # f
        pygame.draw.line(screen, color_b, (x + horiz, y), (x + horiz, y + vert), 5)  # b
        pygame.draw.line(screen, color_e, (x - 5, y + horiz), (x - 5, y + horiz + vert), 5)  # e
        pygame.draw.line(screen, color_c, (x + horiz, y + horiz), (x + horiz, y + horiz + vert), 5)  # c

        # Dibujar un círculo simulado usando líneas radiales
        for angle in range(0, 360, 2):  # Cambia el paso para ajustar la densidad de líneas
            end_x = x_cir + int(radio_circulo * math.cos(math.radians(angle)))
            end_y = y_cir + int(radio_circulo * math.sin(math.radians(angle)))
            pygame.draw.line(screen, color_p, (x_cir, y_cir), (end_x, end_y), 2)
