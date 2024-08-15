import pygame
from pygame.locals import *

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
        self.largo = 650
        self.ancho = 400
        self.color = (222, 222, 222)

    def crear(self, screen):
        # Línea superior
        pygame.draw.line(screen, ("black"), (self.x, self.y), (self.x + self.largo, self.y), 3)
        # Línea izquerda
        pygame.draw.line(screen, ("black"), (self.x, self.y), (self.x, self.y + self.ancho), 3)
        # Línea derecha
        pygame.draw.line(screen, ("black"), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho),3)
        # Línea inferior
        pygame.draw.line(screen, ("black"), (self.x, self.y + self.ancho), (self.x + self.largo, self.y + self.ancho),3)

        for i in range(self.ancho):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))

        alto = 10
        pygame.draw.line(screen, (17, 17, 222), (self.x + alto, self.y + alto), (self.x + self.largo - 10, self.y + alto),1)
        pygame.draw.line(screen, (222, 17, 17), (self.x + alto, self.y + 53), (self.x + self.largo - 10, self.y + 53),1)
        pygame.draw.line(screen, (222, 17, 17), (self.x + alto, self.y + self.ancho-10), (self.x + self.largo - 10, self.y + self.ancho-10),1)
        pygame.draw.line(screen, (17, 17, 222), (self.x + alto, self.y + self.ancho - 53),(self.x + self.largo - 10, self.y + self.ancho - 53), 1)

        # crear CANAL Central
        mitad_largo = self.ancho // 2
        pygame.draw.line(screen, (207, 207, 207), (self.x, self.y + mitad_largo),(self.x + self.largo, self.y + mitad_largo), 30)

        # Llamar al método para dibujar conectores
        self.dibujar_conectores(screen)

    def dibujar_conectores(self, screen):
        # Espaciado entre conectores
        separacion_x = 20
        # Coordenadas iniciales para conectores
        inicio_x = self.x +35
        inicio_y = self.y + 20
        # Número de filas y columnas de conectores
        num_filas = 5
        num_columnas = 30

        dibujar_1(screen,inicio_x-3,inicio_y+45,10,(84,84,84))
        dibujar_5(screen,inicio_x+77,inicio_y+45,10,(84,84,84))
        dibujar_1(screen, inicio_x+175, inicio_y + 55, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x+175, inicio_y + 40, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x+275, inicio_y + 55, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x+275, inicio_y + 40, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x+375, inicio_y + 55, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x+375, inicio_y + 40, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x+475, inicio_y + 55, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x+475, inicio_y + 40, 10, (84, 84, 84))
        dibujar_3(screen, inicio_x+575, inicio_y + 55, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x+575, inicio_y + 40, 10, (84, 84, 84))

        dibujar_1(screen, inicio_x - 3, inicio_y + self.ancho-95, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 77, inicio_y + self.ancho-95, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x + 175, inicio_y + self.ancho-85, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 175, inicio_y + self.ancho-100, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x + 275, inicio_y + self.ancho-85, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 275, inicio_y + self.ancho-100, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x + 375, inicio_y + self.ancho-85, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 375, inicio_y + self.ancho-100, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x + 475, inicio_y + self.ancho-85, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 475, inicio_y + self.ancho-100, 10, (84, 84, 84))
        dibujar_3(screen, inicio_x + 575, inicio_y + self.ancho-85, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 575, inicio_y + self.ancho-100, 10, (84, 84, 84))

        dibujar_mas(screen,inicio_x-20,inicio_y+357,10,(222,17,17))
        dibujar_menos(screen,inicio_x-20,inicio_y+337,(17,17,222))
        dibujar_a(screen,inicio_x-20,inicio_y+285,10,10,(84 , 84, 84))
        dibujar_b(screen, inicio_x-20, inicio_y+265, 10,  (84, 84, 84))
        dibujar_c(screen, inicio_x-20 , inicio_y+245, 10, 10, (84, 84, 84))
        dibujar_d(screen, inicio_x-20 , inicio_y+225, 10, 10, (84, 84, 84))
        dibujar_e(screen, inicio_x-20 , inicio_y+205, 10, 10, (84, 84, 84))
        dibujar_f(screen, inicio_x-20 , inicio_y+145, 10, 10, (84, 84, 84))
        dibujar_g(screen, inicio_x-20 , inicio_y+125, 10, 10, (84, 84, 84))
        dibujar_h(screen, inicio_x-20 , inicio_y+105, 10, 10, (84, 84, 84))
        dibujar_i(screen, inicio_x-20 , inicio_y+85, 10, 10, (84, 84, 84))
        dibujar_j(screen, inicio_x-20, inicio_y+65, 10, 10, (84, 84, 84))
        dibujar_mas(screen, inicio_x - 20, inicio_y+20, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x - 20, inicio_y+2 , (17, 17, 222))

        dibujar_mas(screen, inicio_x +self.largo-55, inicio_y + 357, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x +self.largo-55, inicio_y + 337, (17, 17, 222))
        dibujar_a(screen, inicio_x+self.largo-55, inicio_y + 285, 10, 10, (84, 84, 84))
        dibujar_b(screen, inicio_x+self.largo-55, inicio_y + 265, 10, (84, 84, 84))
        dibujar_c(screen, inicio_x +self.largo-55, inicio_y + 245, 10, 10, (84, 84, 84))
        dibujar_d(screen, inicio_x +self.largo-55, inicio_y + 225, 10, 10, (84, 84, 84))
        dibujar_e(screen, inicio_x +self.largo-55, inicio_y + 205, 10, 10, (84, 84, 84))
        dibujar_f(screen, inicio_x +self.largo-55, inicio_y + 145, 10, 10, (84, 84, 84))
        dibujar_g(screen, inicio_x +self.largo-55, inicio_y + 125, 10, 10, (84, 84, 84))
        dibujar_h(screen, inicio_x +self.largo-55, inicio_y + 105, 10, 10, (84, 84, 84))
        dibujar_i(screen, inicio_x +self.largo-55, inicio_y + 85, 10, 10, (84, 84, 84))
        dibujar_j(screen, inicio_x +self.largo-55, inicio_y + 65, 10, 10, (84, 84, 84))
        dibujar_mas(screen, inicio_x + self.largo - 55, inicio_y + 20, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x + self.largo - 55, inicio_y + 2, (17, 17, 222))

        for i in range(2):
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                conector = Conector(x_pos, y_pos)
                conector.dibujar(screen)

        for i in range(2):
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                conector = Conector(x_pos, y_pos+self.ancho-64)
                conector.dibujar(screen)

        for i in range(num_filas):
            y_pos = inicio_y + i * 20
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                conector = Conector(x_pos, y_pos+70)
                conector.dibujar(screen)

        for i in range(num_filas):
            y_pos = inicio_y + i * 20
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                conector = Conector(x_pos, y_pos+210)
                conector.dibujar(screen)

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

def dibujar_a(screen, x, y,ancho,alto,color):

    pygame.draw.line(screen, color, (x, y + alto), (x + ancho // 2, y), 2)  # Línea diagonal izquierda
    pygame.draw.line(screen, color, (x + ancho // 2, y), (x + ancho, y + alto), 2)  # Línea diagonal derecha
    pygame.draw.line(screen, color, (x + ancho // 4, y + alto // 2), (x + ancho - ancho // 4, y + alto // 2),2)  # Barra horizontal
def dibujar_b(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), ((x + alto // 2), y), 2)
    pygame.draw.line(screen, color, ((x + alto // 2), y), ((x + alto // 2), (y + ((alto // 2)-3))), 2)
    pygame.draw.line(screen, color, (x+alto//2, (y + ((alto // 2)-3))), ((x), (y + ((alto // 2)-3))), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + alto//2), (y + alto)), 2)
    pygame.draw.line(screen, color, ((x + alto//2), (y+alto)), ((x + alto//2), (y+(alto//2))), 2)
    pygame.draw.line(screen,color,((x + alto//2), (y+(alto//2))),(x,y+alto//2),2)
def dibujar_c(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x,( y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x+ancho), y), 2)
    pygame.draw.line(screen, color, ((x+ancho), y), ((x +ancho), (y+(alto//3))), 2)
    pygame.draw.line(screen, color, (x, (y+alto)), ((x+ancho), (y+alto)), 2)
    pygame.draw.line(screen, color, ((x+ancho), (y+alto)), ((x +ancho), (y+alto-(alto//3))), 2)
def dibujar_d(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), (x+alto//5,y), 2)
    pygame.draw.line(screen, color, (x+alto//5 , y), (x + ancho, y + alto), 2)
    pygame.draw.line(screen, color, (x,(y+alto)), (x + ancho, y + alto), 2)
def dibujar_e(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x,(y+(alto//2))), ((x + ancho), (y + alto//2)), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
def dibujar_f(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x,(y+alto//2)), ((x + ancho), (y + alto//2)), 2)
def dibujar_g(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x,( y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x+ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y+alto)), ((x+ancho), (y+alto)), 2)
    pygame.draw.line(screen, color, ((x+ancho), (y+alto)), ((x +ancho), (y+alto-alto//3)), 2)
    pygame.draw.line(screen,color,((x+ancho),(y+alto//2)),(x+alto//3,(y+alto//2)),2)
def dibujar_h(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x,(y+alto//2)), ((x + ancho), (y + alto//2)), 2)
    pygame.draw.line(screen, color, (x+ancho, y), (x+ancho, (y + alto)), 2)
def dibujar_i(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, ((x+(ancho//2)), y), ((x+(ancho//2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
def dibujar_j(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, ((x+(ancho//2)), y), ((x+(ancho//2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho//2), (y + alto)), 2)
def dibujar_l(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y+alto),(x+alto//2,y+alto),2)
def dibujar_m(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y),(x+alto//2,y+alto//2),2)
    pygame.draw.line(screen,color,(x+alto//2,y+alto//2),(x+alto,y),2)
    pygame.draw.line(screen,color,(x+alto,y),(x+alto,y+alto),2)
def dibujar_n(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), (x + alto//2, y + alto), 2)
    pygame.draw.line(screen, color, (x + alto//2, y + alto), (x + alto//2, y), 2)
def dibujar_o(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+alto//2,y),2)
    pygame.draw.line(screen,color,(x+alto//2,y),(x+alto//2,y+alto),2)
    pygame.draw.line(screen,color,(x+alto//2,y+alto),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y+alto),(x,y),2)
def dibujar_p(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen,color,(x,y),((x+alto//2),y),2)
    pygame.draw.line(screen,color,((x+alto//2),y),((x+alto//2),(y+(alto//2))),2)
    pygame.draw.line(screen, color, (x, (y+(alto//2))), ((x + alto//2), (y+(alto//2))), 2)
def dibujar_q(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+alto//2,y),2)
    pygame.draw.line(screen,color,(x+alto//2,y),(x+alto//2,y+alto),2)
    pygame.draw.line(screen,color,(x+alto//2,y+alto),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y+alto),(x,y),2)
    pygame.draw.line(screen,color,(x+alto//4,y+alto//2),(x+alto-4,y+alto),3)
def dibujar_r(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen,color,(x,y),((x+alto//2),y),2)
    pygame.draw.line(screen,color,((x+alto//2),y),((x+alto//2),(y+(alto//2))),2)
    pygame.draw.line(screen, color, (x, (y+(alto//2))), ((x + alto//2), (y+(alto//2))), 2)
    pygame.draw.line(screen,color,(x, (y+(alto//2))),(x+alto//2,y+alto),3)
def dibujar_s(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+alto//2,y),2)
    pygame.draw.line(screen,color,(x+alto//2,y),(x+alto//2,y+alto//4),2)
    pygame.draw.line(screen,color,(x,y),(x,y+alto//2),2)
    pygame.draw.line(screen,color,(x,y+alto//2),(x+alto//2,y+alto//2),2)
    pygame.draw.line(screen,color,(x+alto//2,y+alto//2),(x+alto//2,y+alto),2)
    pygame.draw.line(screen,color,(x+alto//2,y+alto),(x,y+alto),2)
def dibujar_t(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, ((x+(ancho//2)), y), ((x+(ancho//2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
def dibujar_u(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x+alto//2,y),(x+alto//2,y+alto),2)
    pygame.draw.line(screen,color,(x+alto//2,y+alto),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y+alto),(x,y),2)
def dibujar_v(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+alto/4,y+alto),2)
    pygame.draw.line(screen,color,(x+alto//4,y+alto),(x+alto//2,y),2)
def dibujar_x(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x + alto //2, y + alto), 2)
    pygame.draw.line(screen,color,(x+alto//2,y),(x,y+alto),2)
def dibujar_y(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x + alto //4, y + alto//2), 2)
    pygame.draw.line(screen,color,(x+alto//2,y),(x,y+alto),2)
def dibujar_mas(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+alto,y),2)
    pygame.draw.line(screen,color,(x+5,y-5),(x+5,y+5),2)
def dibujar_menos(screen,x,y,color):
    pygame.draw.line(screen, color, (x + 5, y - 5), (x + 5, y + 5), 2)
def dibujar_1(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+5,y+10),2)
    pygame.draw.line(screen,color,(x,y),(x+alto,y),2)
def dibujar_2(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y),(x+5,y),2)
    pygame.draw.line(screen, color, (x+5, y), (x + 5, y+alto), 2)
    pygame.draw.line(screen, color, (x+5, y+alto), (x +alto, y+alto), 2)
    pygame.draw.line(screen, color, (x+alto, y+alto), (x+alto,y), 2)
def dibujar_3(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x +alto, y), 2)
    pygame.draw.line(screen, color, (x, y), (x,y+alto), 2)
    pygame.draw.line(screen, color, (x+5, y), (x + 5, y+alto), 2)
    pygame.draw.line(screen, color, (x+alto, y+alto), (x+alto, y), 2)
def dibujar_4(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), (x + 5, y+alto), 2)

def dibujar_5(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y+alto), (x+5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x +alto, y ), 2)
    pygame.draw.line(screen, color, (x + alto, y + alto), (x + alto, y), 2)
def dibujar_0(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y + alto), (x + alto, y + alto), 2)
    pygame.draw.line(screen, color, (x + alto, y+alto), (x + alto, y ), 2)
    pygame.draw.line(screen, color, (x, y), (x+alto, y), 2)

def escribir(screen,color,largo):
    dibujar_l(screen,74,30,largo,color)
    dibujar_o(screen,84,30,largo,color)
    dibujar_s(screen, 95, 30, largo, color)

    dibujar_c(screen, 125, 30, largo,largo, color)
    dibujar_o(screen, 145, 30, largo, color)
    dibujar_m(screen, 155, 30, largo, color)
    dibujar_p(screen, 175, 30, largo, color)
    dibujar_o(screen, 185, 30, largo, color)
    dibujar_n(screen, 195, 30, largo, color)
    dibujar_e(screen, 205, 30, largo,largo, color)
    dibujar_n(screen, 225, 30, largo, color)
    dibujar_t(screen, 235, 30, largo,largo, color)
    dibujar_e(screen, 253, 30, largo,largo, color)
    dibujar_s(screen, 270, 30, largo, color)

    dibujar_s(screen, 300, 30, largo, color)
    dibujar_e(screen, 310, 30, largo,largo, color)

    dibujar_c(screen, 340, 30, largo,largo, color)
    dibujar_o(screen, 360, 30, largo, color)
    dibujar_n(screen, 372, 30, largo, color)
    dibujar_e(screen, 383, 30, largo,largo, color)
    dibujar_c(screen, 400, 30, largo,largo, color)
    dibujar_t(screen, 420, 30, largo,largo, color)
    dibujar_a(screen, 435, 30, largo,largo, color)
    dibujar_n(screen, 452, 30, largo, color)

    dibujar_p(screen, 480, 30, largo, color)
    dibujar_r(screen, 493, 30, largo, color)
    dibujar_i(screen, 505, 30, largo,largo, color)
    dibujar_m(screen, 523, 30, largo, color)
    dibujar_e(screen, 543, 30, largo,largo, color)
    dibujar_r(screen, 563, 30, largo, color)
    dibujar_o(screen, 573, 30, largo, color)

    dibujar_p(screen, 603, 30, largo, color)
    dibujar_o(screen, 616, 30, largo, color)
    dibujar_r(screen, 630, 30, largo, color)

    dibujar_e(screen, 660, 30, largo,largo, color)
    dibujar_l(screen, 678, 30, largo, color)

    dibujar_l(screen, 710, 30, largo, color)
    dibujar_a(screen, 720, 30, largo,largo, color)
    dibujar_d(screen, 740, 30, largo,largo, color)
    dibujar_o(screen, 757, 30, largo, color)

    dibujar_n(screen, 787, 30, largo, color)
    dibujar_e(screen, 800, 30, largo,largo, color)
    dibujar_g(screen, 818, 30, largo,largo, color)
    dibujar_a(screen, 838, 30, largo,largo, color)
    dibujar_t(screen, 853, 30, largo,largo, color)
    dibujar_i(screen, 873, 30, largo, largo,color)
    dibujar_v(screen, 893, 30, largo, color)
    dibujar_o(screen, 905, 30, largo, color)

    dibujar_y(screen, 30, 60, largo, color)

    dibujar_l(screen, 60, 60, largo, color)
    dibujar_u(screen, 73, 60, largo, color)
    dibujar_e(screen, 86, 60, largo,largo, color)
    dibujar_g(screen, 105, 60, largo,largo, color)
    dibujar_o(screen, 125, 60, largo, color)

    dibujar_p(screen, 155, 60, largo, color)
    dibujar_o(screen, 167, 60, largo, color)
    dibujar_r(screen, 180, 60, largo, color)

    dibujar_e(screen, 210, 60, largo, largo, color)
    dibujar_l(screen, 228, 60, largo, color)

    dibujar_p(screen, 258, 60, largo, color)
    dibujar_o(screen, 269, 60, largo, color)
    dibujar_s(screen, 283, 60, largo, color)
    dibujar_i(screen, 296, 60, largo,largo, color)
    dibujar_t(screen, 315, 60, largo,largo, color)
    dibujar_i(screen, 333, 60, largo,largo, color)
    dibujar_v(screen, 350, 60, largo, color)
    dibujar_o(screen, 365, 60, largo, color)

    dibujar_c(screen, 395, 60, largo,largo, color)
    dibujar_o(screen, 414, 60, largo, color)
    dibujar_n(screen, 426, 60, largo, color)

    dibujar_l(screen, 452, 60, largo, color)
    dibujar_a(screen, 462, 60, largo,largo, color)

    dibujar_e(screen, 492, 60, largo,largo, color)
    dibujar_x(screen, 512, 60, largo, color)
    dibujar_c(screen, 525, 60, largo,largo, color)
    dibujar_e(screen, 545, 60, largo,largo, color)
    dibujar_p(screen, 563, 60, largo, color)
    dibujar_c(screen, 575, 60, largo,largo, color)
    dibujar_i(screen, 595, 60, largo,largo, color)
    dibujar_o(screen, 615, 60, largo, color)
    dibujar_n(screen, 625, 60, largo, color)

    dibujar_d(screen, 655, 60, largo, largo, color)
    dibujar_e(screen, 672, 60, largo, largo, color)

    dibujar_l(screen, 707, 60, largo, color)
    dibujar_o(screen, 720, 60, largo, color)
    dibujar_s(screen, 730, 60, largo, color)

    dibujar_c(screen, 760, 60, largo,largo, color)
    dibujar_a(screen, 778, 60, largo,largo, color)
    dibujar_b(screen, 797, 60, largo, color)
    dibujar_l(screen, 810, 60, largo, color)
    dibujar_e(screen, 820, 60, largo,largo, color)
    dibujar_s(screen, 837, 60, largo, color)




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
    screen.fill("white") # directo el color sin variables extra

    x_proto = (screen.get_width() - 650) // 2
    y_proto = (screen.get_height() - 400) // 2

    # Crear y dibujar Protoboard

    protoboard = Protoboard(x_proto, y_proto)
    protoboard.crear(screen)

    # Crear y dibujar Pila

    x_pila = 10# (screen.get_width() + 750) // 2
    y_pila = 400# (screen.get_height() - 550) // 2

    pila = Pila(x_pila, y_pila)
    pila.dibujarPila(screen)

    # texto de instrucciones
    escribir(screen,(0,0,0),15)

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
