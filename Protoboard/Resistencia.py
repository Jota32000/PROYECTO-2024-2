import pygame

class Resistencia:
    def __init__(self,conector1, conector2):
        self.conector_inicio = conector1
        self.conector_fin = conector2
        self.bandera = 0

    def dibujar_resistencia(self,screen):
            color = (251, 179, 92)
            pygame.draw.line(screen, "dark gray", (self.conector_inicio.x, self.conector_inicio.y),
                             (self.conector_fin.x, self.conector_fin.y), 3)
            x_medio = (self.conector_inicio.x + self.conector_fin.x) // 2
            y_medio = (self.conector_inicio.y + self.conector_fin.y) // 2

            if self.conector_inicio.x - self.conector_fin.x == 0:
                # Dibujo concreto de resistencia de forma vertical
                pygame.draw.line(screen, color, (x_medio + 10, y_medio + 15), (x_medio + 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio + 10), (x_medio + 5, y_medio + 5), 3)
                pygame.draw.line(screen, color, (x_medio + 5, y_medio + 5), (x_medio + 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio + 5, y_medio - 5), (x_medio + 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio - 10), (x_medio + 10, y_medio - 15), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio - 15), (x_medio - 10, y_medio - 15), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio - 15), (x_medio - 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio - 10), (x_medio - 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio - 5), (x_medio - 5, y_medio + 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio + 5), (x_medio - 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio + 10), (x_medio - 10, y_medio + 15), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio + 15), (x_medio + 10, y_medio + 15), 3)

                # Ciclos para rellenar interior
                for i in range(10):
                    pygame.draw.line(screen, color, (x_medio - 5 + i, y_medio - 15), (x_medio - 5 + i, y_medio + 15), 3)
                for i in range(5):
                    pygame.draw.line(screen, color, (x_medio - 10 + i, y_medio - 15 + i),
                                     (x_medio - 10 + i, y_medio - 15 + 2 * i), 3)
                    pygame.draw.line(screen, color, (x_medio - 10 + i, y_medio + 15 - i),
                                     (x_medio - 10 + i, y_medio + 15 - 2 * i), 3)
                    pygame.draw.line(screen, color, (x_medio + 10 - i, y_medio + 15 - i),
                                     (x_medio + 10 - i, y_medio + 15 - 2 * i), 3)
                    pygame.draw.line(screen, color, (x_medio + 10 - i, y_medio - 15 + i),
                                     (x_medio + 10 - i, y_medio - 15 + 2 * i), 3)

                # Lineas para determinar niveles de ohm
                pygame.draw.line(screen, "red", (x_medio - 5, y_medio - 3), (x_medio + 5, y_medio - 3), 3)
                pygame.draw.line(screen, "dark green", (x_medio - 5, y_medio + 4), (x_medio + 5, y_medio + 4), 3)
                pygame.draw.line(screen, "blue", (x_medio - 10, y_medio - 10), (x_medio + 10, y_medio - 10), 3)
                pygame.draw.line(screen, "yellow", (x_medio - 10, y_medio + 10), (x_medio + 10, y_medio + 10), 1)

            else:
                pygame.draw.line(screen, color, (x_medio + 5, y_medio + 5), (x_medio - 5, y_medio + 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio + 5), (x_medio - 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio + 10), (x_medio - 15, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio - 15, y_medio + 10), (x_medio - 15, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio - 15, y_medio - 10), (x_medio - 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio - 10), (x_medio - 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio - 5), (x_medio + 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio + 5, y_medio - 5), (x_medio + 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio - 10), (x_medio + 15, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio + 15, y_medio - 10), (x_medio + 15, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio + 15, y_medio + 10), (x_medio + 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio + 10), (x_medio + 5, y_medio + 5), 3)

                # Ciclos para rellenar interior
                for i in range(10):
                    pygame.draw.line(screen, color, (x_medio - 15, y_medio - 5 + i), (x_medio + 15, y_medio - 5 + i), 3)
                for i in range(5):
                    pygame.draw.line(screen, color, (x_medio - 15 + i, y_medio - 10 + i),
                                     (x_medio - 15 + 2 * i, y_medio - 10 + i), 3)
                    pygame.draw.line(screen, color, (x_medio + 15 - i, y_medio - 10 + i),
                                     (x_medio + 15 - 2 * i, y_medio - 10 + i), 3)
                    pygame.draw.line(screen, color, (x_medio + 15 - i, y_medio + 10 - i),
                                     (x_medio + 15 - 2 * i, y_medio + 10 - i), 3)
                    pygame.draw.line(screen, color, (x_medio - 15 + i, y_medio + 10 - i),
                                     (x_medio - 15 + 2 * i, y_medio + 10 - i), 3)

                # Lineas para determinar niveles de ohm
                pygame.draw.line(screen, "red", (x_medio + 4, y_medio - 5), (x_medio + 4, y_medio + 5), 3)
                pygame.draw.line(screen, "dark green", (x_medio - 3, y_medio - 5), (x_medio - 3, y_medio + 5), 3)
                pygame.draw.line(screen, "blue", (x_medio - 10, y_medio - 10), (x_medio - 10, y_medio + 10), 3)
                pygame.draw.line(screen, "yellow", (x_medio + 10, y_medio - 10), (x_medio + 10, y_medio + 10), 1)

    def validar_resistencia(self, resistencias):
        for resistencia in resistencias:
           if (resistencia.conector_inicio == self.conector_inicio and resistencia.conector_fin == self.conector_fin) or (resistencia.conector_inicio == self.conector_fin and resistencia.conector_fin == self.conector_inicio):
               return False  
        return True
    
    def dibujar_resistencia_actual(self, screen, conector1):
        if conector1 is not None:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, "dark gray", (conector1.x, conector1.y), current_pos, 3)

   