import pygame
import math

from Datos import *

class Led:
    def __init__(self,color,x,y,x1,x2,y1,y2,inicio,fin):
        self.color=color
        self.x = x
        self.y = y
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.nombre_start = inicio
        self.nombre_end = fin
    def led_apagada(self,screen,conectores):

        conector1 = None
        conector2 = None

        for c in conectores:
            if c.nombre == self.nombre_start:
                self.x1, self.y1 = c.x, c.y  # Cambiar coordenadas de inicio
            elif c.nombre == self.nombre_end:
                self.x2, self.y2 = c.x, c.y  # Cambiar coordenadas de fin

        for c in conectores:
            if c.x == self.x1 and c.y == self.y1:
                conector1 = c
            elif c.x == self.x2 and c.y == self.y2:
                conector2 = c

        self.x = (conector1.x + conector2.x) / 2
        self.y = (conector1.y + conector2.y) / 2

        corriente_conector1 = False
        if conector1.fase or conector1.neutro:
            corriente_conector1 = True
        # Verificar si conector2 tiene corriente
        corriente_conector2 = False
        if conector2.fase or conector2.neutro:
            corriente_conector2 = True

        if conector2.fase and conector1.fase:
            corriente_conector1 = True
            corriente_conector2 = False

        if conector2.neutro and conector1.neutro:
            corriente_conector1 = True
            corriente_conector2 = False

        # Cambiar color del LED según si ambos conectores tienen corriente
        if corriente_conector1 and corriente_conector2:
            self.color = (250, 0, 0)  # Color rojo para encendido
        else:
            self.color = (110, 0, 0)  # Color rojo oscuro para apagado

        pygame.draw.line(screen, (0, 0, 0, 0), (self.x1, self.y1), (self.x, self.y), 2)
        pygame.draw.line(screen, (0, 0, 0, 0), (self.x2, self.y2), (self.x, self.y), 2)
        for angle in range(0, 360, 3):
            circle_radius = 6
            start_x = self.x
            start_y = self.y
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen,self.color, (start_x, start_y), (end_x, end_y), 2)