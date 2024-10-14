import pygame
import math

from Datos import *

class Switch:
    def __init__(self, x, y, x1, x2, x3, x4, y1, y2, y3, y4):
        self.x = x
        self.y = y
        self.x1 = x1  # patita 1 izquierda / derecha
        self.x2 = x2  # patita 2  derecha / izquierda
        self.x3 = x3  # patita 3
        self.x4 = x4  # patita 4
        self.y1 = y1  # patita 1
        self.y2 = y2  # patita 1
        self.y3 = y3  # patita 1
        self.y4 = y4  # patita 1
        self.estado = False
        self.lado = 40  # Tamaño del switch (cuadrado)

    def switch_proto(self, screen):

        body_color = (150, 150, 150)
        circle_radius = 8  # Radio del "círculo" en el medio
        # Dibujar patitas
        pygame.draw.line(screen, (0, 0, 0), (self.x1, self.y1), (self.x + self.lado // 2, self.y + self.lado // 2), 2)  # patita 1
        pygame.draw.line(screen, (0, 0, 0), (self.x2, self.y2), (self.x + self.lado // 2, self.y + self.lado // 2), 2)  # patita 2
        pygame.draw.line(screen, (0, 0, 0), (self.x3, self.y3), (self.x + self.lado // 2, self.y + self.lado // 2), 2)  # patita 3
        pygame.draw.line(screen, (0, 0, 0), (self.x4, self.y4), (self.x + self.lado // 2, self.y + self.lado // 2), 2)  # patita 4
        # Dibujar cuerpo del switch (con líneas)
        for i in range(self.lado):
            pygame.draw.line(screen, body_color, (self.x, self.y + i), (self.x + self.lado, self.y + i))

        # Dibujar el "círculo" en el centro usando líneas
        for angle in range(0, 360, 10):
            start_x = self.x + self.lado // 2
            start_y = self.y + self.lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

        # Dibujar botón (usando líneas para crear un borde)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.lado, self.y), 2)  # Línea superior
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y), (self.x + self.lado, self.y + self.lado), 2)  # Línea derecha
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y + self.lado), (self.x, self.y + self.lado),
                         2)  # Línea inferior
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.lado), (self.x, self.y), 2)  # Línea izquierda