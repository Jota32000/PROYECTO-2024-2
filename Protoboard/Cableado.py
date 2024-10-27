import pygame
from Conector import *

class Cableado:
    def __init__(self,conector1, conector2):
        self.conector_inicio = conector1
        self.conector_fin = conector2

    def dibujar_cables(self,screen):
        # verificar fase y neutro sino da problemas
        if self.conector_inicio.fase or self.conector_inicio.neutro or self.conector_fin.fase or self.conector_fin.neutro:
            if self.conector_inicio.fase and self.conector_fin.fase:
                color = (234, 79, 235) # morado
            elif self.conector_inicio.neutro and self.conector_fin.neutro:
                color = (61, 205, 234) # azul cielo dark
            else:
                color = "black"
        else:
            color = "black"
        pygame.draw.line(screen, color, (self.conector_inicio.x, self.conector_inicio.y), (self.conector_fin.x, self.conector_fin.y), 3)

    def validar_cable(self, cables):
        for cable in cables:
           if (cable.conector_inicio == self.conector_inicio and cable.conector_fin == self.conector_fin) or (cable.conector_inicio == self.conector_fin and cable.conector_fin == self.conector_inicio):
               return False
        return True

    def dibujar_cable_actual(self, screen, conector1):
        if conector1 is not None:
            current_pos = pygame.mouse.get_pos()
            if conector1.fase:
                color = (234, 79, 235)
            elif conector1.neutro:
                color = (61, 205, 234)
            else:
                color = "black"
            pygame.draw.line(screen, color, (conector1.x, conector1.y), current_pos, 3)