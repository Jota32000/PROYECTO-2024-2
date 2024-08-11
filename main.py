import pygame
from pygame.locals import *

# 04
def dibujar_letra(screen, letter, font_size, x, y, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(letter, True, color)
    screen.blit(text_surface, (x, y))

class Conector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largo = 5
        self.color = (84, 84, 84)

    def dibujar(self, screen):
        for i in range(self.largo):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))


class Protoboard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largo = 490
        self.ancho = 560
        self.color = (222, 222, 222)

    def crear(self, screen):
        # Línea superior
        pygame.draw.line(screen, ("black"), (self.x, self.y), (self.x + self.largo, self.y), 3)
        # Línea izquerda
        pygame.draw.line(screen, ("black"), (self.x, self.y), (self.x, self.y + self.ancho), 3)
        # Línea derecha
        pygame.draw.line(screen, ("black"), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho),
                         3)
        # Línea inferior
        pygame.draw.line(screen, ("black"), (self.x, self.y + self.ancho), (self.x + self.largo, self.y + self.ancho),
                         3)

        for i in range(self.ancho):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))

        alto = 10
        pygame.draw.line(screen, (222, 17, 17), ((self.x + 10), (self.y + alto)),
                         ((self.x + 10), (self.y - alto) + self.ancho), 1)
        pygame.draw.line(screen, (17, 17, 222), ((self.x + 53), (self.y + alto)),
                         ((self.x + 53), (self.y - alto) + self.ancho), 1)
        pygame.draw.line(screen, (17, 17, 222), ((self.x - 10) + self.largo, (self.y + alto)),
                         ((self.x - 10) + self.largo, (self.y - alto) + self.ancho), 1)
        pygame.draw.line(screen, (222, 17, 17), ((self.x - 53) + self.largo, (self.y + alto)),
                         ((self.x - 53) + self.largo, (self.y - alto) + self.ancho), 1)

        # crear CANAL Central
        mitad_largo = self.largo // 2
        pygame.draw.line(screen, (207, 207, 207), (self.x + mitad_largo, self.y),
                         (self.x + mitad_largo, self.y + self.ancho), 30)

        # Llamar al método para dibujar conectores
        self.dibujar_conectores(screen)

    def dibujar_conectores(self, screen):

        # Espaciado entre conectores
        separacion_y = 20
        # Coordenadas iniciales para conectores
        inicio_x = self.x + 20
        inicio_y = self.y + 20
        # Número de filas y columnas de conectores
        num_filas = 25
        num_columnas = 5

        dibujar_letra(screen, "+", 30, inicio_x - 2, inicio_y - 10, (222, 17, 17))
        dibujar_letra(screen, "-", 30, inicio_x + 20, inicio_y - 10, (17, 17, 222))
        dibujar_letra(screen, "+", 30, inicio_x + 425, inicio_y - 10, (222, 17, 17))
        dibujar_letra(screen, "-", 30, inicio_x + 445, inicio_y - 10, (17, 17, 222))
        dibujar_letra(screen, "a", 30, inicio_x + 55, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "b", 30, inicio_x + 85, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "c", 30, inicio_x + 115, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "d", 30, inicio_x + 145, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "e", 30, inicio_x + 175, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "f", 30, inicio_x + 260, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "g", 30, inicio_x + 290, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "h", 30, inicio_x + 320, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "i", 30, inicio_x + 350, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "j", 30, inicio_x + 380, inicio_y - 10, (84, 84, 84))

        for i in range(num_filas):
            for j in range(2): # conectores derecha col
                x_pos = (inicio_x + 20) + j * (self.largo - 63)
                y_pos = (inicio_y + 20) + i * separacion_y
                conector1 = Conector(x_pos, y_pos)
                conector1.dibujar(screen)
                conector2 = Conector((x_pos - 20), y_pos)
                conector2.dibujar(screen)

        # Dibujar conectores en la fila central izquierda
        for i in range(num_filas):
            x_pos = (inicio_x + 60)
            y_pos = (inicio_y + 20) + i * separacion_y
            for j in range(num_columnas):  # columnas de conectores en los bordes
                conector = Conector(x_pos, y_pos)
                conector.dibujar(screen)
                x_pos = x_pos + 30

        # Dibujar conectores en la fila central derecha
        for i in range(num_filas):
            x_pos = (inicio_x + 260)
            y_pos = (inicio_y + 20) + i * separacion_y
            for j in range(num_columnas):  # columnas de conectores en los bordes
                conector = Conector(x_pos, y_pos)
                conector.dibujar(screen)
                x_pos = x_pos + 30

class Pila:
    def __init__(self,pila_x,pila_y):
        self.pila_x = pila_x
        self.pila_y = pila_y
        self.color_cabeza_pila = (240, 134, 21)
        self.color_cuerpo_pila = (0, 0, 0)
        self.color_componentes_pila = (170, 170, 170)
        self.largo = 750
        self.ancho = 550

    def dibujarPila(self,screen):
        #Dibujo parte superior pila

        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y), (self.pila_x + 30, self.pila_y), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y), (self.pila_x, self.pila_y + 100), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y + 100), (self.pila_x + 30, self.pila_y + 100), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x + 30, self.pila_y), (self.pila_x + 30, self.pila_y + 100), 3)

        #Ciclo que permite rellenar la pila
        for i in range(10):
            pygame.draw.rect(screen, self.color_cabeza_pila, (self.pila_x + i, self.pila_y, 20, 100))

        #Dibujo parte inferior pila
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 30, self.pila_y + 100), (self.pila_x + 120, self.pila_y + 100), 3)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 120, self.pila_y + 100), (self.pila_x + 120, self.pila_y), 3)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 120, self.pila_y), (self.pila_x + 30, self.pila_y), 3)

        #Ciclo que permite rellenar la parte interior de la pila

        for i in range(80):
            pygame.draw.rect(screen, self.color_cuerpo_pila, (self.pila_x + 30 + i, self.pila_y, 12, 100))

        #Dibujo de los componentes de la pila

        #Componente negativo (-)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x - 2, self.pila_y + 20), (self.pila_x - 15, self.pila_y + 20), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x - 15, self.pila_y + 20), (self.pila_x - 15, self.pila_y + 30), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x - 15, self.pila_y + 30), (self.pila_x - 2, self.pila_y + 30), 3)
        
        #Componente Positivo (+)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x - 2, self.pila_y + 60), (self.pila_x - 15, self.pila_y + 60), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x - 15, self.pila_y + 60), (self.pila_x - 15, self.pila_y + 70), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x - 2, self.pila_y + 70), (self.pila_x - 15, self.pila_y + 70), 3)
        
        #Ciclo para rellenar componente 1
        for i in range(10):
            pygame.draw.rect(screen, self.color_componentes_pila, (self.pila_x - 15 + i, self.pila_y + 20, 5, 10))

        #Ciclo para rellenar componente 2
        for i in range(10):
            pygame.draw.rect(screen, self.color_componentes_pila, (self.pila_x - 15 + i, self.pila_y + 60, 5, 10))
        
        #Inclusión de positivo y negativo

        #Negativo
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 10, self.pila_y + 30), (self.pila_x + 10, self.pila_y + 20), 2)

        #Positivo
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 10, self.pila_y + 70), (self.pila_x + 10, self.pila_y + 60), 2)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 15, self.pila_y + 65), (self.pila_x + 5, self.pila_y + 65), 2)


#Main
pygame.init()

#medidas de la protoboard
screen_width = 950
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]


fullscreen = False
running = True
while running:
    mainClock.tick(60)  # FPS de 60
    screen.fill("white") # directo el color sin variables extra

    x_proto = (screen.get_width() - 490) // 2
    y_proto = (screen.get_height() - 560) // 2

    # Crear y dibujar Protoboard

    protoboard = Protoboard(x_proto, y_proto)
    protoboard.crear(screen)

    # Crear y dibujar Pila

    x_pila = (screen.get_width() + 750) // 2
    y_pila = (screen.get_height() - 550) // 2

    pila = Pila(x_pila, y_pila)
    pila.dibujarPila(screen)

    # manejo de eventos
    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
        if event.type == VIDEORESIZE:

            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False
            if event.key == K_f:
                fullscreen = not fullscreen

                if fullscreen:
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

    pygame.display.flip()
    mainClock.tick(60)


pygame.quit()