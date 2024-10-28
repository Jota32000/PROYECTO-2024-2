import pygame

class Chip:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ancho=27
        self.largo=190
        self.color_cuerpo=(53, 46, 46 )
        self.dis=10
        self.lado=30

    def dibujar(self, screen):
        # Patas superiores
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.dis), 2)  # pin 1 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y), (self.x + self.lado, self.y + self.dis),
                         2)  # pin 2 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 2), self.y),
                         (self.x + (self.lado * 2), self.y + self.dis), 2)  # pin 3 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 3), self.y),
                         (self.x + (self.lado * 3), self.y + self.dis), 2)  # pin 4 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 4), self.y),
                         (self.x + (self.lado * 4), self.y + self.dis), 2)  # pin 5 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 5), self.y),
                         (self.x + (self.lado * 5), self.y + self.dis), 2)  # pin 6 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 6), self.y),
                         (self.x + (self.lado * 6), self.y + self.dis), 2)  # pin 7 arriba

        # Patas inferiores
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x, self.y + 20), 2)  # pin 1 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y + 30), (self.x + self.lado, self.y + 20),
                         2)  # pin 2 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 2), self.y + 30),
                         (self.x + (self.lado * 2), self.y + 20), 2)  # pin 3 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 3), self.y + 30),
                         (self.x + (self.lado * 3), self.y + 20), 2)  # pin 4 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 4), self.y + 30),
                         (self.x + (self.lado * 4), self.y + 20), 2)  # pin 5 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 5), self.y + 30),
                         (self.x + (self.lado * 5), self.y + 20), 2)  # pin 6 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 6), self.y + 30),
                         (self.x + (self.lado * 6), self.y + 20), 2)  # pin 7 abajo

        # Dibujo del cuerpo del objeto con líneas
        for i in range(self.y + 5, self.y + self.ancho):
            pygame.draw.line(screen, self.color_cuerpo, (self.x - 5, i), (self.x + self.largo, i))
