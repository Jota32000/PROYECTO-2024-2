import pygame
import math


class Switch:
    def __init__(self, conector):
        self.x = conector.x
        self.y = conector.y
        self.color_cuerpo = (165, 198, 193)
        self.color_encendido = (192, 100, 198)
        self.color_circulo = (91, 91, 91 )  # Color inicial del círculo
        self.estado = False
        self.lado = 60  # Tamaño del switch (cuadrado)
        self.pin1 = conector
        self.pin2 = None
        self.pin3 = None
        self.pin4 = None
        self.bandera = 1

    def switch_proto(self, screen):

        # Dibujar el cuerpo del switch usando líneas
        for i in range(self.lado):
            pygame.draw.line(screen, self.color_cuerpo, (self.x, self.y + i), (self.x + self.lado, self.y + i))
        # Dibujar el "círculo" en el centro usando líneas
        circle_radius = 10  # Radio del círculo
        circulos_pin=5# circulos en las 4 esquinas
        # Dibujar las líneas del cuerpo del switch
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + self.lado, self.y), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y), (self.x + self.lado, self.y + self.lado), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y + self.lado), (self.x, self.y + self.lado), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.lado), (self.x, self.y), 2)

        for angle in range(0, 360, 10):
            start_x = self.x + self.lado // 2
            start_y = self.y + self.lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, self.color_circulo, (start_x, start_y), (end_x, end_y), 2)

        # Dibujar 4 círculos pequeños (pines) en las esquinas usando líneas
        pin_radius = 5  # Radio de los "pines" (círculos pequeños)
        esquinas = [
            (self.x+10, self.y+10),  # Esquina superior izquierda
            (self.x + self.lado-10, self.y+10),  # Esquina superior derecha
            (self.x+10, self.y + self.lado-10),  # Esquina inferior izquierda
            (self.x + self.lado-10, self.y + self.lado-10)  # Esquina inferior derecha
        ]

        for esquina in esquinas:
            for angle in range(0, 360, 10):
                start_x = esquina[0]
                start_y = esquina[1]
                end_x = start_x + int(pin_radius * math.cos(math.radians(angle)))
                end_y = start_y + int(pin_radius * math.sin(math.radians(angle)))
                pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

    def detectar_click(self, mouse_pos):
        # Verificar si el clic está dentro del área del switch
        if self.x <= mouse_pos[0] <= self.x + self.lado and self.y <= mouse_pos[1] <= self.y + self.lado:
            self.estado = not self.estado  # Cambiar el estado del switch
            # Cambiar el color del círculo cuando el estado cambia
            if self.estado:
                self.color_circulo = self.color_encendido  # Cambiar al color encendido
                a, b = self.pines2(0)  # Llama a pines2 con el índice 0
                if a is not None and b is not None:
                    if a.fase or a.neutro:
                        self.bandera = 2
                    a.agregar_conexion(b)
            else:
                self.color_circulo = (91, 91, 91)  # Volver al color apagado
                a, b = self.pines2(0)  # Llama a pines2 para desconectar
                if a is not None and b is not None:
                    if self.bandera == 2:
                        b.eliminar_conexion(b, a)
                    else:
                        a.eliminar_conexion(a, b)

    def pines2(self,i):
        if i==0:
            return self.pin1,self.pin2
        if i==1:
            return self.pin3, self.pin4
        return None, None