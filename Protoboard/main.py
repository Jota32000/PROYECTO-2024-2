import pygame
import sys

def dibujar_letra(screen, letter, font_size, x, y,color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(letter, True,color)
    screen.blit(text_surface, (x, y))
class Conector:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def dibujar (self,screen):
        self.largo=5
        self.color=(84, 84, 84 )
        """"
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + self.largo, self.y))
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y + self.largo))  # Línea izquierda
        pygame.draw.line(screen, self.color, (self.x + self.largo, self.y),(self.x + self.largo, self.y + self.largo))  # Línea derecha
        pygame.draw.line(screen, self.color, (self.x, self.y + self.largo),(self.x + self.largo, self.y + self.largo))  # Línea inferior
        """
        for i in range(self.largo):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))
class Protoboard:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def crear(self,screen):
        self.largo = 490
        self.ancho=560
        self.color = (222, 222, 222)

        # Línea superior
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x + self.largo, self.y),3)
        # Línea izquierda
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y + self.ancho),3)
        # Línea derecha
        pygame.draw.line(screen, (0,0,0), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho),3)
        # Línea inferior
        pygame.draw.line(screen, (0,0,0), (self.x, self.y + self.ancho), (self.x + self.largo, self.y + self.ancho),3)

        for i in range(self.ancho):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))
        alto=10
        pygame.draw.line(screen, (222, 17, 17 ), ((self.x+10), (self.y+alto)), ((self.x+10), (self.y -alto)+ self.ancho), 1)
        pygame.draw.line(screen, (17, 17, 222), ((self.x + 53), (self.y + alto)),((self.x + 53), (self.y - alto) + self.ancho), 1)
        pygame.draw.line(screen, (17,17,222), ((self.x-10) + self.largo, (self.y+alto)), ((self.x-10) + self.largo, (self.y-alto) + self.ancho),1)
        pygame.draw.line(screen, (222, 17, 17), ((self.x - 53) + self.largo, (self.y + alto)),((self.x - 53) + self.largo, (self.y - alto) + self.ancho), 1)

        #crear CANAL Central
        mitad_largo= self.largo//2
        pygame.draw.line(screen, (207, 207, 207), (self.x + mitad_largo, self.y),(self.x + mitad_largo, self.y + self.ancho), 30)

        # Llamar al método para dibujar conectores
        self.dibujar_conectores(screen)

    def dibujar_conectores(self, screen):
        # Espaciado entre conectores
        separacion_x = 20
        separacion_y = 20

        # Coordenadas iniciales para conectores
        inicio_x = self.x + 20
        inicio_y = self.y + 20

        # Número de filas y columnas de conectores
        num_filas = 25
        num_columnas = 5
        dibujar_letra(screen,"+",30,inicio_x-2,inicio_y-10,(222,17,17))
        dibujar_letra(screen, "-", 30, inicio_x+20, inicio_y - 10, (17,17,222))
        dibujar_letra(screen, "+", 30, inicio_x+425, inicio_y - 10, (222, 17, 17))
        dibujar_letra(screen, "-", 30, inicio_x +445, inicio_y - 10, (17, 17, 222))
        dibujar_letra(screen, "a", 30, inicio_x +55, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "b", 30, inicio_x + 85, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "c", 30, inicio_x + 115, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "d", 30, inicio_x + 145, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "e", 30, inicio_x + 175, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "f", 30, inicio_x + 260, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "g", 30, inicio_x + 290, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "h", 30, inicio_x + 320, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "i", 30, inicio_x + 350, inicio_y - 10, (84, 84, 84))
        dibujar_letra(screen, "j", 30, inicio_x + 380, inicio_y - 10, (84, 84, 84))

        # Dibujar conectores en las filas laterales
        for i in range(num_filas):
            for j in range(4):  # columnas de conectores en los bordes
                x_pos = (inicio_x+20) + j * (self.largo-63)
                y_pos = (inicio_y+20)+ i * separacion_y
                conector1 = Conector(x_pos, y_pos)
                conector1.dibujar(screen)
                conector2 = Conector((x_pos-20),y_pos)
                conector2.dibujar(screen)


        # Dibujar conectores en la fila central izquierda
        for i in range(num_filas):
            x_pos = (inicio_x + 60)
            y_pos = (inicio_y+20) + i * separacion_y
            for j in range(num_columnas):  # columnas de conectores en los bordes
                conector=Conector(x_pos,y_pos)
                conector.dibujar(screen)
                x_pos = x_pos + 30

        # Dibujar conectores en la fila central derecha
        for i in range(num_filas):
            x_pos = (inicio_x + 260)
            y_pos = (inicio_y+20) + i * separacion_y
            for j in range(num_columnas):  # columnas de conectores en los bordes
                conector=Conector(x_pos,y_pos)
                conector.dibujar(screen)
                x_pos = x_pos + 30


pygame.init()


screen_width = 950
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Proto")

white = (255, 255, 255)
screen.fill(white)

ancho_p= 490 #medidad de la protoboard
largo_p= 560

# Calcular las coordenadas para centrar Protoboard
x_proto = (screen_width - ancho_p) // 2
y_proto = (screen_height - largo_p) // 2

running = True
while running:

    # Crear y dibujar Protoboard
    protoboard = Protoboard(x_proto, y_proto)
    protoboard.crear(screen)

    pygame.display.flip()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()