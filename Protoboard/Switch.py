import pygame
import math

from Datos import *

class Switch:
    def __init__(self, x, y, x1, x2, y1, y2):
        self.x = x
        self.y = y
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.estado=False

    def switch_proto(self, screen):
        lado = 20  # Tamaño del switch (cuadrado)
        body_color = (150, 150, 150)
        circle_radius = 5  # Radio del "círculo" en el medio



        self.x, self.y = (((self.x1 + self.x2) / 2) - 10, ((self.y1 + self.y2) / 2) - 10)

        # Dibujar patitas
        pygame.draw.line(screen, (0, 0, 0), (self.x1, self.y1), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 1
        pygame.draw.line(screen, (0, 0, 0), (self.x2, self.y2), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 2

        # Dibujar cuerpo del switch (con líneas)
        for i in range(lado):
            pygame.draw.line(screen, body_color, (self.x, self.y + i), (self.x + lado, self.y + i))

        # Dibujar el "círculo" en el centro usando líneas
        for angle in range(0, 360, 10):
            start_x = self.x + lado // 2
            start_y = self.y + lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

        # Dibujar botón (usando líneas para crear un borde)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + lado, self.y), 2)  # Línea superior
        pygame.draw.line(screen, (0, 0, 0), (self.x + lado, self.y), (self.x + lado, self.y + lado), 2)  # Línea derecha
        pygame.draw.line(screen, (0, 0, 0), (self.x + lado, self.y + lado), (self.x, self.y + lado),
                         2)  # Línea inferior
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + lado), (self.x, self.y), 2)  # Línea izquierda