import pygame

class Switch_16:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color_cuerpo = (127, 179, 213)  # Color del cuerpo del switch
        self.cApagado = (255, 255, 255)  # Color de los botones apagados
        self.cEncendido = (225, 178, 178)  # Color de los botones encendidos
        self.disL = 20  # Distancia horizontal entre botones
        self.disA = 40  # Distancia vertical entre botones
        self.largo = 150
        self.ancho = 36
        self.boton_colores = [self.cApagado] * 8  # Lista de colores de los botones
        self.boton_surfaces = []  # Lista para almacenar superficies de los botones

        # Crear superficies para los botones
        self.crear_botones()
    def crear_botones(self):
        for i in range(8):
            surface = pygame.Surface((7, 14))  # Tamaño del botón
            surface.fill(self.cApagado)  # Color inicial del botón
            self.boton_surfaces.append(surface)

    def dibujar(self, screen):
        # Dibujar el cuerpo del switch
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.disA), 2)
        for i in range(1, 8):
            pygame.draw.line(screen, (0, 0, 0), (self.x + self.disL * i, self.y), (self.x + self.disL * i, self.y + self.disA), 2)

        # Dibujar el relleno del cuerpo
        pygame.draw.line(screen, (0, 0, 0), (self.x - 5, self.y + 6), (self.x + self.largo, self.y + 6), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x - 5, self.y + self.ancho), (self.x + self.largo, self.y + self.ancho), 2)
        pygame.draw.line(screen,(0,0,0),(self.x - 5, self.y + 6),(self.x - 5, self.y + self.ancho),2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.largo, self.y + 6), (self.x + self.largo, self.y + self.ancho), 2)
        for i in range(self.y + 7, self.y + self.ancho):
            pygame.draw.line(screen, self.color_cuerpo, (self.x - 4, i), (self.x + self.largo, i))

        # Dibujar los botones en sus posiciones
        for i in range(8):
            x_pos = self.x + self.disL * i
            y_pos = self.y + 13
            screen.blit(self.boton_surfaces[i], (x_pos, y_pos))

    def detectar_click(self, pos):
        # Verificar si el clic está dentro de algún botón
        for i in range(8):
            boton_x = self.x + self.disL * i
            boton_y = self.y + 13
            if boton_x <= pos[0] <= boton_x + 7 and boton_y <= pos[1] <= boton_y + 14:
                # Cambiar el color del botón al ser presionado
                if self.boton_colores[i] == self.cApagado:
                    self.boton_colores[i] = self.cEncendido  # Cambiar a encendido
                else:
                    self.boton_colores[i] = self.cApagado  # Cambiar a apagado
                # Actualizar la superficie del botón
                self.boton_surfaces[i].fill(self.boton_colores[i])