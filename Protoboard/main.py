import pygame
import math
from pygame.locals import *

class Conector:
    def __init__(self, x, y, lista_conectores):  # agrege lista conectores
        self.x = x
        self.y = y
        self.largo = 5
        self.color = (84, 84, 84)
        lista_conectores.append((self.x + 2, self.y + 2))  # agrega las cc a la lista

    def dibujar(self, screen):
        for i in range(self.largo):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))
conectores = []
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
                conector = Conector(x_pos, y_pos,conectores)
                conector.dibujar(screen)

        for i in range(2):
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                conector = Conector(x_pos, y_pos+self.ancho-64,conectores)
                conector.dibujar(screen)

        for i in range(num_filas):
            y_pos = inicio_y + i * 20
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                conector = Conector(x_pos, y_pos+70,conectores)
                conector.dibujar(screen)

        for i in range(num_filas):
            y_pos = inicio_y + i * 20
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                conector = Conector(x_pos, y_pos+210,conectores)
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
<<<<<<< HEAD
=======
        conector_pila1 = Conector(pila_x+65, pila_y-20, conectores)  #positivo
        conector_pila2 = Conector(pila_x+35, pila_y-20, conectores) #negativo
>>>>>>> piherina

    def dibujarPila(self,screen):

        #Dibujo parte superior pila

        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y + 30), (self.pila_x, self.pila_y), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y + 30), (self.pila_x + 100, self.pila_y + 30), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x + 100, self.pila_y + 30), (self.pila_x + 100, self.pila_y), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y), (self.pila_x + 100, self.pila_y), 3)

        #Ciclo que permite rellenar la pila

        for i in range(100):
            pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y), (self.pila_x + i, self.pila_y + 30), 3)
            pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x + 100, self.pila_y + 30), (self.pila_x + 100 - i, self.pila_y), 3)

        #Dibujo parte inferior pila

        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 100, self.pila_y + 30), (self.pila_x + 100, self.pila_y + 120), 3)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 100, self.pila_y + 120), (self.pila_x, self.pila_y + 120), 3)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x, self.pila_y + 120), (self.pila_x, self.pila_y + 30), 3)

        #Ciclo que permite rellenar la parte interior de la pila

        for i in range(100):
            pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x, self.pila_y + 30), (self.pila_x + i, self.pila_y + 120))
            pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 100, self.pila_y + 120), (self.pila_x + 100 - i, self.pila_y + 30))

        #Dibujo de los componentes de la pila

        #Componente negativo (-)

        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 30, self.pila_y - 2), (self.pila_x + 30, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 30, self.pila_y - 16), (self.pila_x + 40, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 40, self.pila_y - 16), (self.pila_x + 40, self.pila_y - 2), 3)

        conector_pila1_mas = Conector(self.pila_x + 33, self.pila_y - 16, conectores)

        #Componente Positivo (+)

        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y  - 2), (self.pila_x + 60, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 16), (self.pila_x + 70, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 70, self.pila_y - 2), (self.pila_x + 70, self.pila_y - 16), 3)

        conector_pila2_menos = Conector(self.pila_x + 63, self.pila_y - 16, conectores)

        #Ciclo para rellenar componente 1 +
        for i in range(10):
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 16), (self.pila_x + 60 + i, self.pila_y - 2), 3)
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 70, self.pila_y - 2), (self.pila_x + 70 - i, self.pila_y - 16), 3)

        #Ciclo para rellenar componente 2 -
        for i in range(10):
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 30, self.pila_y - 16), (self.pila_x + 30 + i, self.pila_y - 2), 3)
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 40, self.pila_y - 2), (self.pila_x + 40 - i, self.pila_y - 16), 3)

        #Inclusión de positivo y negativo

        #Negativo

        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 40, self.pila_y + 15), (self.pila_x + 30, self.pila_y + 15), 2)

        #Positivo

        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 70, self.pila_y + 15), (self.pila_x + 60, self.pila_y + 15), 2)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 65, self.pila_y + 10), (self.pila_x + 65, self.pila_y + 20), 2)

class Menu:
    def __init__(self, x, y):
        self.x = x
<<<<<<< HEAD
        self.y = y + 25
        self.ancho = 10
        self.alto = 15
        self.color_fondo_led = (66, 214, 2)
        self.color_fondo_switch = (255, 44, 44)     
        self.color_fondo_cable = (0, 90, 247)
        self.color_led = (50, 164, 0)
        self.color_switch = (205, 0, 0)     
        self.color_cable = (33, 0, 183)
=======
        self.y = y
        self.l1 = 200  # Ancho
        self.l2 = 550  # Alto
        self.color = (63, 129, 166)
        self.border_color = (0, 0, 0)
        self.border_thickness = 2
        self.border_radius = 10  # Ajusta este valor para redondear más o menos las esquinas
>>>>>>> piherina

        # Definir los rectángulos que representan los botones ocultos
        self.boton_led_rect = pygame.Rect(self.x + 50, self.y + 50, 100, 100)  # Posición y tamaño del botón oculto del LED
        self.boton_switch_rect = pygame.Rect(self.x + 50, self.y + 180, 100, 100)  # Posición y tamaño del botón oculto del switch

    def dibujar(self, screen):
        # Dibujar el fondo del rectángulo con esquinas redondeadas
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.l1, self.l2), border_radius=self.border_radius)

<<<<<<< HEAD
        #Ciclo para rellenar
        for i in range(50):
            pygame.draw.line(screen, (self.color_fondo_led), (self.x + 450, self.y - 100), (self.x + 450 + i, self.y - 50), 3)
            pygame.draw.line(screen, (self.color_fondo_led), (self.x + 500, self.y - 50), (self.x + 500 - i, self.y - 100), 3)

    def dibujar_menu_switch(self,menu):
        pygame.draw.line(screen, (self.color_fondo_switch), (self.x + 450, self.y - 25), (self.x + 500, self.y - 25), 3)
        pygame.draw.line(screen, (self.color_fondo_switch), (self.x + 500, self.y - 25), (self.x + 500, self.y + 25), 3)
        pygame.draw.line(screen, (self.color_fondo_switch), (self.x + 500, self.y + 25), (self.x + 450, self.y + 25), 3)
        pygame.draw.line(screen, (self.color_fondo_switch), (self.x + 450, self.y + 25), (self.x + 450, self.y - 25), 3)

        #Ciclo para rellenar
        for i in range(50):
            pygame.draw.line(screen, (self.color_fondo_switch), (self.x + 450, self.y + 25), (self.x + 500, self.y + 25 - i), 3)
            pygame.draw.line(screen, (self.color_fondo_switch), (self.x + 500, self.y - 25), (self.x + 450, self.y - 25 + i), 3)

    def dibujar_menu_cable(self,menu):
        pygame.draw.line(screen, (self.color_fondo_cable), (self.x + 450, self.y + 50), (self.x + 500, self.y + 50), 3)
        pygame.draw.line(screen, (self.color_fondo_cable), (self.x + 500, self.y + 50), (self.x + 500, self.y + 100), 3)
        pygame.draw.line(screen, (self.color_fondo_cable), (self.x + 500, self.y + 100), (self.x + 450, self.y + 100), 3)
        pygame.draw.line(screen, (self.color_fondo_cable), (self.x + 450, self.y + 100), (self.x + 450, self.y + 50), 3)

        #Ciclo para rellenar
        for i in range(50):
            pygame.draw.line(screen, (self.color_fondo_cable), (self.x + 450, self.y + 100), (self.x + 500, self.y + 100 - i), 3)
            pygame.draw.line(screen, (self.color_fondo_cable), (self.x + 500, self.y + 50), (self.x + 450, self.y + 50 + i), 3)      
=======
        # Dibujar el borde del rectángulo con esquinas redondeadas
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.l1, self.l2), self.border_thickness, border_radius=self.border_radius)

        # Dibujar los iconos y componentes
        self.dibujar_icono(screen, self.x + 50, self.y + 50)
        self.dib_led(screen, self.x + 75, self.y + 65)
        self.dibujar_icono(screen, self.x + 50, self.y + 180)
        self.dib_switch(screen, self.x + 80, self.y + 210)
        self.dibujar_icono(screen, self.x + 50, self.y + 320)

        # Crear superficie para los botones semi-transparentes (para mostrar las áreas donde se puede hacer clic)
        boton_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # SRCALPHA para transparencia
        boton_led_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón LED
        boton_switch_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón Switch

        # Dibujar los botones en sus respectivas superficies
        self.dibujar_icono(boton_surface, 0, 0)
        self.dib_led(boton_led_surface, 25, 15)  # Ajusta la posición dentro del botón
        self.dib_switch(boton_switch_surface, 25, 15)  # Ajusta la posición dentro del botón
>>>>>>> piherina

        # Blit de las superficies a la pantalla principal
        screen.blit(boton_led_surface, (self.x + 50, self.y + 50))  # Botón LED en la pantalla

<<<<<<< HEAD
    def dibujar_switch(self,menu):
        pygame.draw.line(screen, (self.color_switch), (self.x + 490, self.y + 20), (self.x + 460, self.y + 20), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 460, self.y + 20), (self.x + 460, self.y + 15), 3) 
        pygame.draw.line(screen, (self.color_switch), (self.x + 460, self.y + 15), (self.x + 455, self.y + 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 455, self.y + 15), (self.x + 455, self.y - 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 455, self.y - 15), (self.x + 460, self.y - 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 460, self.y - 15), (self.x + 460, self.y - 20), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 460, self.y - 20), (self.x + 490, self.y - 20), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 490, self.y - 20), (self.x + 490, self.y - 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 490, self.y - 15), (self.x + 495, self.y - 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 495, self.y - 15), (self.x + 495, self.y + 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 495, self.y + 15), (self.x + 490, self.y + 15), 3)
        pygame.draw.line(screen, (self.color_switch), (self.x + 490, self.y + 15), (self.x + 490, self.y + 20), 3)


    def dibujar_cable(self,menu):
        pygame.draw.line(screen, (self.color_cable), (self.x + 490, self.y + 75), (self.x + 460, self.y + 75), 6)

    def animacion(self,menu):

        posicion_mouse = pygame.mouse.get_pos()
        area_x_rect_1, area_y_rect_1 = self.x + 450, self.y - 100 
        area_x_rect_2, area_y_rect_2 = self.x + 450, self.y - 25
        area_x_rect_3, area_y_rect_3 = self.x + 450, self.y + 50                                            
        ancho,alto = 50, 50
        
        if (area_x_rect_1 <= posicion_mouse[0] <= area_x_rect_1 + ancho and
        area_y_rect_1 <= posicion_mouse[1] <= area_y_rect_1 + alto):
            pygame.draw.line(screen, self.color_led, (self.x + 580 , self.y - 85), (self.x + 550 , self.y - 75), 3)
            pygame.draw.line(screen, self.color_led, (self.x + 550 , self.y - 75), (self.x + 600 , self.y - 75), 3)
            pygame.draw.line(screen, self.color_led, (self.x + 580 , self.y - 65), (self.x + 550 , self.y - 75), 3)

        if (area_x_rect_2 <= posicion_mouse[0] <= area_x_rect_2 + ancho and
        area_y_rect_2 <= posicion_mouse[1] <= area_y_rect_2 + alto):
            pygame.draw.line(screen, self.color_switch, (self.x + 580 , self.y - 10), (self.x + 550 , self.y ), 3)
            pygame.draw.line(screen, self.color_switch, (self.x + 550 , self.y), (self.x + 600 , self.y), 3)
            pygame.draw.line(screen, self.color_switch, (self.x + 580 , self.y + 10), (self.x + 550 , self.y), 3)

        if (area_x_rect_3 <= posicion_mouse[0] <= area_x_rect_3 + ancho and
        area_y_rect_3 <= posicion_mouse[1] <= area_y_rect_3 + alto):
            pygame.draw.line(screen, self.color_cable, (self.x + 580, self.y + 85), (self.x + 550, self.y + 75), 3)
            pygame.draw.line(screen, self.color_cable, (self.x + 550, self.y + 75), (self.x + 600, self.y + 75), 3)
            pygame.draw.line(screen, self.color_cable, (self.x + 580, self.y + 65), (self.x + 550, self.y + 75), 3)

def dibujar_a(screen, x, y,ancho,alto,color):
    pygame.draw.line(screen, color, (x, y + alto), (x + ancho // 2, y), 2)  # Línea diagonal izquierda
    pygame.draw.line(screen, color, (x + ancho // 2, y), (x + ancho, y + alto), 2)  # Línea diagonal derecha
    pygame.draw.line(screen, color, (x + ancho // 4, y + alto // 2), (x + ancho - ancho // 4, y + alto // 2),2)  # Barra horizontal
def dibujar_b(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen,color,(x,y),((x+10),y),2)
    pygame.draw.line(screen,color,((x+10),y),((x+10),(y+4)),2)
    pygame.draw.line(screen, color, (x, (y+4)), ((x + 10), (y+4)), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + 10), (y + alto)), 2)
    pygame.draw.line(screen, color, ((x + 10), (y+alto)), ((x + 10), (y+6)), 2)
def dibujar_c(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x,( y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x+ancho), y), 2)
    pygame.draw.line(screen, color, ((x+ancho), y), ((x +ancho), (y+3)), 2)
    pygame.draw.line(screen, color, (x, (y+alto)), ((x+ancho), (y+alto)), 2)
    pygame.draw.line(screen, color, ((x+ancho), (y+alto)), ((x +ancho), (y+alto-3)), 2)
def dibujar_d(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), (x+2,y), 2)
    pygame.draw.line(screen, color, (x+2 , y), (x + ancho, y + alto), 2)
    pygame.draw.line(screen, color, (x,(y+alto)), (x + ancho, y + alto), 2)
def dibujar_e(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x,(y+5)), ((x + ancho), (y + 5)), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
=======

    def dibujar_icono(self, screen, x, y):
        color = (39, 174, 96)
        lado = 100
        pygame.draw.rect(screen, color, (x, y, lado, lado), border_radius=10)
        pygame.draw.rect(screen, self.border_color, (x, y, lado, lado), self.border_thickness, border_radius=10)
>>>>>>> piherina

    def dib_led(self, screen, x, y):
        width = 50  # Ancho del LED
        height = 35  # Alto del LED
        color = (199, 9, 9)
        terminal = 30  # Longitud de los terminales
        # Dibujar el cuerpo del LED como un rectángulo con esquinas redondeadas
        pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
        # Dibujar los terminales del LED (líneas)
        pygame.draw.line(screen, (0, 0, 0), (x + width // 4, y + height), (x + width // 4, y + height + terminal), 2)
        pygame.draw.line(screen, (0, 0, 0), (x + 3 * width // 4, y + height), (x + 3 * width // 4, y + height + terminal), 2)

    def dib_switch(self, screen, x, y):
        size = 40  # Tamaño del switch (cuadrado)
        pin_length = 20  # Longitud de los pines
        body_color = (150, 150, 150)
        pin_color = (0, 0, 0)
        circle_radius = 10  # Radio del "círculo" en el medio
        pygame.draw.rect(screen, body_color, (x, y, size, size))
        # Dibujar los pines del switch (líneas)
        pygame.draw.line(screen, pin_color, (x, y + size // 2), (x - pin_length, y + size // 2), 3)
        pygame.draw.line(screen, pin_color, (x + size, y + size // 2), (x + size + pin_length, y + size // 2), 3)
        # Dibujar el "círculo" en el centro
        for angle in range(0, 360, 10):
            start_x = x + size // 2
            start_y = y + size // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

    def manejar_eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.boton_led_rect.collidepoint(pos):
                self.accion_boton_led()
            elif self.boton_switch_rect.collidepoint(pos):
                self.accion_boton_switch()

    def accion_boton_led(self):
        print("Botón LED presionado")

    def accion_boton_switch(self):
        print("Botón Switch presionado")
class Cableado:
    def __init__(self):
        self.dibujando_cable = False
        self.inicio_cable = None
        self.cables = []

    def dibujar_cables(self):
        for cable in self.cables:
            pygame.draw.line(screen,"black", cable[0], cable[1], 3)

    def comienzo_cable(self, anclaje):
        self.inicio_cable = anclaje
        self.dibujando_cable = True

    def finalizar_cable(self, anclaje):
        if not self.quitar_cable(self.inicio_cable, anclaje):
            self.cables.append((self.inicio_cable, anclaje))
        self.dibujando_cable = False
        self.inicio_cable = None

    def quitar_cable(self, start, end):
        for cable in self.cables:
            if (cable[0] == start and cable[1] == end) or (cable[0] == end and cable[1] == start):
                self.cables.remove(cable)
                return True
        return False

    def dibujar_cable_actual(self):
        if self.dibujando_cable and self.inicio_cable:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, "black", self.inicio_cable, current_pos, 3)

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

#Main
pygame.init()

# Obtener el tamaño de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Configurar la pantalla en un tamaño
window_width = int(screen_width * 0.98)
window_height = int(screen_height * 0.94)

# Crear la ventana con el tamaño ajustado
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

cableado = Cableado()
fullscreen = False
running = True

while running:
    screen.fill("white") # directo el color sin variables extra

    x_proto = (screen.get_width() - 650) // 2
    y_proto = (screen.get_height() - 400) // 2

    # Crear y dibujar Protoboard

    conectores.clear()
    protoboard = Protoboard(x_proto, y_proto)
    protoboard.crear(screen)

    # Crear y dibujar Pila

    x_pila = (screen.get_width() - 950) // 2
    y_pila = (screen.get_height() - 150) // 2

    pila = Pila(x_pila, y_pila)
    pila.dibujarPila(screen)

    # Crear y dibujar Menu
<<<<<<< HEAD

    x_menu = (screen.get_width() - 200) // 2
    y_menu = (screen.get_height() - 40) // 2

    menu = Menu(x_menu, y_menu)
    menu.dibujar_menu_led(screen)
    menu.dibujar_menu_switch(screen)
    menu.dibujar_menu_cable(screen)
    menu.dibujar_cable(screen)
    menu.dibujar_led(screen)
    menu.dibujar_switch(screen)
    menu.animacion(screen)
=======
    menu = Menu(980, 80)
    menu.dibujar(screen)
    clock = pygame.time.Clock()

>>>>>>> piherina

    def distancia(punto1, punto2):
        return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)


    def punto_mas_cercano(pos_mouse, lista_conectores, distancia_maxima):
        punto_cercano = None
        distancia_minima = 10000

        for conector in lista_conectores:
            dist = distancia(pos_mouse, conector)
            if dist < distancia_minima and dist <= distancia_maxima:
                distancia_minima = dist
                punto_cercano = conector
        return punto_cercano

    distancia_maxima = 10

    cableado.dibujar_cables()

    # Manejo de eventos


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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            conector_cercano = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)

            if conector_cercano:
                x1, y1 = conector_cercano

                if not cableado.dibujando_cable:
                    cableado.comienzo_cable((x1, y1))
                else:
                    cableado.finalizar_cable((x1, y1))

        if event.type == pygame.QUIT:
            running = False
        menu.manejar_eventos(event)


    cableado.dibujar_cable_actual()
    pygame.display.flip()
    mainClock.tick(60)

pygame.quit()
