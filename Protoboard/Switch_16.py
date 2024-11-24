import pygame

class Switch_16:
    def __init__(self,conector):
        self.x = conector.x
        self.y = conector.y
        self.color_cuerpo = (127, 179, 213)  # Color del cuerpo del switch
        self.cApagado = (255, 255, 255)  # Color de los botones apagados
        self.cEncendido = (225, 178, 178)  # Color de los botones encendidos
        self.disL = 30  # Distancia horizontal
        self.disA = 60
        self.largo = 220
        self.ancho = 53
        self.boton_colores = [self.cApagado] * 8  # Lista de colores de los botones
        self.boton_surfaces = []  # Lista para almacenar superficies de los botones
        # Crear superficies para los botones
        self.crear_botones()
        self.pin1=conector
        self.pin2 = None
        self.pin3 = None
        self.pin4 = None
        self.pin5 = None
        self.pin6 = None
        self.pin7 = None
        self.pin8 = None
        self.pin9 = None
        self.pin10 = None
        self.pin11 = None
        self.pin12 = None
        self.pin13 = None
        self.pin14 = None
        self.pin15 = None
        self.pin16 = None
        self.bandera = [1] * 8 # hace eso: [1, 1, 1, 1, 1, 1, 1, 1] sino da out of range

    def crear_botones(self):
        for i in range(8):
            surface = pygame.Surface((8, 25))  # Tamaño del botón
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
            screen.blit(self.boton_surfaces[i], (x_pos, y_pos+5))
    def detectar_click(self, pos):
        # Verificar si el clic está dentro de algún botón
        for i in range(8):
            boton_x = self.x + self.disL * i
            boton_y = self.y + 18
            if boton_x <= pos[0] <= boton_x + 8 and boton_y <= pos[1] <= boton_y + 25:
                # Cambiar el color del botón al ser presionado
                if self.boton_colores[i] == self.cApagado:
                    self.boton_colores[i] = self.cEncendido  # Cambiar a encendido
                    a,b=self.pines2(i)
                    if a!=None and b!=None:
                        if a.fase or a.neutro:
                            self.bandera[i] = 2 # ahora verifica por cada pareja no solo 1 vez
                        else:
                            self.bandera[i] = 1
                        a.agregar_conexion(b)
                else:
                    self.boton_colores[i] = self.cApagado  # Cambiar a apagado
                    a, b = self.pines2(i)
                    if a != None and b != None:
                        if self.bandera[i] == 2:
                            b.eliminar_conexion(b,a)
                        else:
                            a.eliminar_conexion(a, b)

                # Actualizar la superficie del botón
                self.boton_surfaces[i].fill(self.boton_colores[i])
    def pines2(self,i):
        if i==0:
            return self.pin1,self.pin9
        if i==1:
            return self.pin2, self.pin10
        if i==2:
            return self.pin3, self.pin11
        if i==3:
            return self.pin4, self.pin12
        if i==4:
            return self.pin5, self.pin13
        if i==5:
            return self.pin6, self.pin14
        if i==6:
            return self.pin7, self.pin15
        if i==7:
            return self.pin8, self.pin16
        return None,None
