import pygame
import math

class Led:
    def __init__(self,color,conector1,conector2):
        self.color=color
        self.conector1 = conector1
        self.conector2 = conector2

    def led_apagada(self,screen):

        corriente_conector1 = False
        if self.conector1.fase or self.conector1.neutro:
            corriente_conector1 = True
        # Verificar si conector2 tiene corriente
        corriente_conector2 = False
        if self.conector2.fase or self.conector2.neutro:
            corriente_conector2 = True

        if self.conector2.fase and self.conector1.fase:
            corriente_conector1 = True
            corriente_conector2 = False

        if self.conector2.neutro and self.conector1.neutro:
            corriente_conector1 = True
            corriente_conector2 = False

        # Cambiar color del LED según si ambos conectores tienen corriente
        if corriente_conector1 and corriente_conector2:
            self.color = (250, 0, 0)  # Color rojo para encendido
        else:
            self.color = (110, 0, 0)  # Color rojo oscuro para apagado

        x =  (self.conector1.x+self.conector2.x)//2
        y = (self.conector1.y+self.conector2.y)//2

        pygame.draw.line(screen, (0, 0, 0, 0), (self.conector1.x, self.conector1.y), (x, y), 2)
        pygame.draw.line(screen, (0, 0, 0, 0), (self.conector2.x, self.conector2.y), (x, y), 2)
        for angle in range(0, 360, 3):
            circle_radius = 6
            start_x = x
            start_y = y
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen,self.color, (start_x, start_y), (end_x, end_y), 2)