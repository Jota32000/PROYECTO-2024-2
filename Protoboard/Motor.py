import pygame
class Motor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 60
        self.largo = 100
        self.color = (31, 255, 0)
        self.c_cuerpo = (103, 103, 103)
        self.boton_color = self.color
        self.boton_x = self.x + 10
        self.boton_y = self.y + 10
        self.boton_largo = self.largo - 20
        self.boton_ancho = self.ancho - 20
        self.estado_boton = False

    def div_boton(self, screen):
        # Rellenar el área general
        for i in range(self.y, self.y + self.ancho):
            pygame.draw.line(screen, self.c_cuerpo, (self.x, i), (self.x + self.largo, i))

        # Dibujar borde del área general
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.largo, self.y), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo, self.y + self.ancho), (self.x, self.y + self.ancho), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.ancho), 3)

        for i in range(self.y + 10, (self.y + 10) + self.ancho - 20):
            pygame.draw.line(screen, self.boton_color, (self.x + 10, i), (self.x + self.largo - 10, i))

        pygame.draw.line(screen, (0, 0, 0), (self.x + 10, self.y + 10), (self.x + self.largo - 10, self.y + 10), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo - 10, self.y + 10), (self.x + self.largo - 10, self.y + self.ancho - 10), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo - 10, self.y + self.ancho - 10), (self.x + 10, self.y + self.ancho - 10), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x + 10, self.y + 10), (self.x + 10, self.y + self.ancho - 10), 3)

    def verificar_click(self, pos):
        # Verificar si se hizo clic dentro del área verde (botón)
        if self.boton_x <= pos[0] <= self.boton_x + self.boton_largo and self.boton_y <= pos[1] <= self.boton_y + self.boton_ancho:
            self.estado_boton = not self.estado_boton
            if self.estado_boton:
                self.boton_color = (69, 111, 63)
            else:
                self.boton_color = (31, 255, 0)
            return True
        return False

