import pygame
import math
from pygame.locals import *

class Conector:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.largo = 5
        self.color = (84, 84, 84)
        self.conexiones = []

    def dibujar(self, screen):
        for i in range(self.largo):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))

    def __str__(self):
        return f"Conector(nombre={self.nombre}, x={self.x}, y={self.y})"

    def agregar_conexion(self, conector_destino):
        if conector_destino not in self.conexiones:
            self.conexiones.append(conector_destino)
            print("origen: ", self.nombre, " dest: ", conector_destino)
            if self.conexiones:
                print("----- Lista conexiones ------")
                print("largo: ",len(self.conexiones),"\n")
                self.imprimir_conexiones()

    def imprimir_conexiones(self):
        print(f">>> Conexiones de {self.nombre}:")
        for conector in self.conexiones:
            print(conector)

conectores = []

boton_led = False #estado del boton de la led (activado=true o desactivado=false)
boton_switch=False #estado del boton del switch (activado=true o desactivado=false)

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

        # Llamar al metodo para dibujar conectores
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
                nombre_c1 = f"conector1_{i}_{j}"
                conector = Conector(nombre_c1, x_pos, y_pos)
                conectores.append(conector)
                conector.dibujar(screen)

        for i in range(2):
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                nombre_c2 = f"conector2_{i}_{j}"
                conector = Conector(nombre_c2, x_pos, y_pos + self.ancho - 64)
                conectores.append(conector)
                conector.dibujar(screen)

        for i in range(num_filas):
            y_pos = inicio_y + i * 20
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                nombre_c3 = f"conector3_{i}_{j}"
                conector = Conector(nombre_c3, x_pos, y_pos + 70)
                conectores.append(conector)
                conector.dibujar(screen)

        for i in range(num_filas):
            y_pos = inicio_y + i * 20
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                nombre_c4 = f"conector4_{i}_{j}"
                conector = Conector(nombre_c4, x_pos, y_pos + 210)
                conectores.append(conector)
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

        conector_pila1 = Conector("pila+", self.pila_x + 65, self.pila_y - 15) #positivo
        conectores.append(conector_pila1)

        conector_pila2 = Conector("pila-", self.pila_x + 35, self.pila_y - 15) #negativo
        conectores.append(conector_pila2)

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
        
        #Componente Positivo (+)
        
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y  - 2), (self.pila_x + 60, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 16), (self.pila_x + 60, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 70, self.pila_y - 2), (self.pila_x + 70, self.pila_y - 16), 3)
        
        #Ciclo para rellenar componente 1
        for i in range(10):
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 16), (self.pila_x + 60 + i, self.pila_y - 2), 3)
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 70, self.pila_y - 2), (self.pila_x + 70 - i, self.pila_y - 16), 3)
            
        #Ciclo para rellenar componente 2
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
        self.y = y
        self.l1 = 190  # Ancho
        self.l2 = 480  # Alto
        self.color = (63, 129, 166)
        self.border_color = (0, 0, 0)
        self.border_thickness = 2
        self.border_radius = 10

        # Definir las áreas de colisión para los botones
        self.boton_led_x = self.x + 50
        self.boton_led_y = self.y + 50
        self.boton_led_ancho = 100
        self.boton_led_alto = 100

        self.boton_switch_x = self.x + 50
        self.boton_switch_y = self.y + 180
        self.boton_switch_ancho = 100
        self.boton_switch_alto = 100

        self.boton_switch_x = self.x + 50
        self.boton_switch_y = self.y + 320
        self.boton_switch_ancho = 100
        self.boton_switch_alto = 100
    def dibujar(self, screen):
        x_borde = self.x + 5
        y_borde = self.y + 5
        l1=self.l1-5
        l2=self.l2-5

        # Dibujar las líneas rectas entre las esquinas
        pygame.draw.line(screen, self.color, (self.x , self.y), (self.x + self.l1, self.y),20)  # Línea superior
        pygame.draw.line(screen, self.color, (self.x + self.l1, self.y ), (self.x + self.l1, self.y + self.l2),20)  # Línea derecha
        pygame.draw.line(screen, self.color, (self.x + self.l1 , self.y + self.l2), (self.x, self.y + self.l2),20)  # Línea inferior
        pygame.draw.line(screen, self.color, (self.x, self.y + self.l2 ), (self.x, self.y ),20)  # Línea izquierda
        for i in range(self.l2):
            pygame.draw.line(screen, self.color, (self.x+4, self.y+4 + i), (self.x + self.l1-4, self.y + i))

        # Dibujar el borde del rectángulo con esquinas redondeadas
        pygame.draw.arc(screen, self.border_color, (x_borde, y_borde, 2 * self.border_radius, 2 * self.border_radius), 0.5 * math.pi, math.pi, self.border_thickness)  # Esquina superior izquierda
        pygame.draw.arc(screen, self.border_color, (x_borde + l1 - 2 * self.border_radius,y_borde, 2 * self.border_radius, 2 * self.border_radius), 0,0.5 * math.pi, self.border_thickness)  # Esquina superior derecha
        pygame.draw.arc(screen, self.border_color, (x_borde, y_borde + l2 - 2 * self.border_radius, 2 * self.border_radius, 2 * self.border_radius), math.pi,1.5 * math.pi, self.border_thickness)  # Esquina inferior izquierda
        pygame.draw.arc(screen, self.border_color, (x_borde + l1 - 2 * self.border_radius, y_borde + l2 - 2 * self.border_radius, 2 * self.border_radius,2 * self.border_radius), 1.5 * math.pi, 2 * math.pi, self.border_thickness)  # Esquina inferior derecha

        pygame.draw.line(screen, self.border_color, (x_borde + self.border_radius,y_borde), (x_borde + l1 - self.border_radius, y_borde),self.border_thickness)  # Línea superior
        pygame.draw.line(screen, self.border_color, (x_borde + l1, y_borde + self.border_radius), (x_borde + l1,y_borde + l2 - self.border_radius), self.border_thickness)  # Línea derecha
        pygame.draw.line(screen, self.border_color, (x_borde + l1 - self.border_radius, y_borde + l2), (x_borde + self.border_radius, y_borde + l2),self.border_thickness)  # Línea inferior
        pygame.draw.line(screen, self.border_color, (x_borde, y_borde + l2 - self.border_radius), (x_borde,y_borde + self.border_radius),self.border_thickness)  # Línea izquierda

        # Dibujar los iconos y componentes
        self.dibujar_icono(screen, self.x + 50, self.y + 50)
        self.dib_led(screen, self.x + 75, self.y + 65)
        self.dibujar_icono(screen, self.x + 50, self.y + 180)
        self.dib_switch(screen, self.x + 80, self.y + 210)
        self.dibujar_icono(screen, self.x + 50, self.y + 320)
        self.dib_basurero(screen,self.x+65,self.y+340)

        # Crear superficie para los botones semi-transparentes (para mostrar las áreas donde se puede hacer clic)
        boton_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # SRCALPHA para transparencia
        boton_led_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón LED
        boton_switch_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón Switch
        boton_basurero_surface = pygame.Surface((100,100),pygame.SRCALPHA) # Boton basurero

        # Dibujar los botones en sus respectivas superficies
        self.dibujar_icono(boton_surface, 0, 0)
        self.dib_led(boton_led_surface, 25, 15)
        self.dib_switch(boton_switch_surface, 25, 15)
        self.dib_basurero(boton_basurero_surface,25,15)

        # Blit de las superficies a la pantalla principal
        screen.blit(boton_led_surface, (self.x + 50, self.y + 50))  # Botón LED en la pantalla
    def dibujar_icono(self, screen, x, y):
        color = (39, 174, 96)
        lado = 100
        grosor_borde = 5

        # Dibujar cuadrado
        pygame.draw.line(screen, color, (x, y), (x + lado, y), grosor_borde)  # Línea superior
        pygame.draw.line(screen, color, (x, y), (x, y + lado), grosor_borde)  # Línea izquierda
        pygame.draw.line(screen, color, (x + lado, y), (x + lado, y + lado), grosor_borde)  # Línea derecha
        pygame.draw.line(screen, color, (x, y + lado), (x + lado, y + lado), grosor_borde)  # Línea inferior
        for i in range(lado):
            pygame.draw.line(screen, color, (x, y + i), (x + lado, y + i))

        # borde adicional
        pygame.draw.line(screen, self.border_color, (x, y), (x + lado, y), self.border_thickness)  # Borde superior
        pygame.draw.line(screen, self.border_color, (x, y), (x, y + lado), self.border_thickness)  # Borde izquierdo
        pygame.draw.line(screen, self.border_color, (x + lado, y), (x + lado, y + lado), self.border_thickness)  # Borde derecho
        pygame.draw.line(screen, self.border_color, (x, y + lado), (x + lado, y + lado),self.border_thickness)  # Borde inferior
    def dib_led(self, screen, x, y):
        width = 50  # Ancho del LED
        height = 35  # Alto del LED
        color = (199, 9, 9)
        terminal = 30  # Longitud de los terminales
        radius = 10  # Radio de las esquinas redondeadas
        pin_y=y+3

        # Dibujar las esquinas redondeadas
        pygame.draw.arc(screen, color, (x , y-radius-4 + height - 2 * radius, 2 * radius, 2 * radius),0.5 * math.pi, math.pi, 5)  # Esquina superior izquierda
        pygame.draw.arc(screen, color, (x + width - 2 * radius, y, 2 * radius, 2 * radius), 0, 0.5 * math.pi,5)  # Esquina superior derecha
        pygame.draw.arc(screen, color, (x+ width - 2 * radius, y + height - 2 * radius, 2 * radius, 2 * radius), 1.5 * math.pi, 2 * math.pi,5)  # Esquina inferior derecha
        pygame.draw.arc(screen, color, (x, y + height - 2 * radius, 2 * radius, 2 * radius), math.pi, 1.5 * math.pi,5)  # Esquina inferior izquierda

        # Dibujar las líneas rectas entre las esquinas
        pygame.draw.line(screen, color, (x + radius, y), (x + width - radius, y), 5)  # Línea superior
        pygame.draw.line(screen, color, (x + width, y + radius), (x + width, y + height - radius), 5)  # Línea derecha
        pygame.draw.line(screen, color, (x + width - radius, y + height), (x + radius, y + height), 5)  # Línea inferior
        pygame.draw.line(screen, color, (x, y + height - radius), (x, y + radius), 5)  # Línea izquierda
        for i in range(height-4):
            pygame.draw.line(screen, color, (x+3, pin_y + i), (x + width-3, pin_y + i))
        # Dibujar los terminales del LED (líneas)
        pygame.draw.line(screen, self.border_color, (x + width // 4, y + height), (x + width // 4, y + height + terminal), 2)
        pygame.draw.line(screen, self.border_color, (x + 3 * width // 4, y + height),(x + 3 * width // 4, y + height + terminal), 2)
    def dib_switch(self, screen, x, y):
        lado = 40  # Tamaño del switch (cuadrado)
        pin_length = 20  # Longitud de los pines
        body_color = (150, 150, 150)
        pin_color = (0, 0, 0)
        circle_radius = 10  # Radio del "círculo" en el medio
        pygame.draw.line(screen, body_color, (x,y),(x+lado,y),2)
        pygame.draw.line(screen, body_color, (x+lado, y), (x + lado, y + lado), 2)
        pygame.draw.line(screen, body_color, (x+lado, y+lado), (x, y + lado), 2)
        pygame.draw.line(screen, body_color, (x, y+lado), (x , y ), 2)
        for i in range(lado):
            pygame.draw.line(screen, body_color, (x, y + i), (x + lado, y + i))
        # Dibujar los pines del switch
        pygame.draw.line(screen, pin_color, (x, y + lado // 2), (x - pin_length, y + lado // 2), 3)
        pygame.draw.line(screen, pin_color, (x + lado, y + lado // 2), (x + lado + pin_length, y + lado // 2), 3)
        # Dibujar el "círculo" en el centro
        for angle in range(0, 360, 10):
            start_x = x + lado // 2
            start_y = y + lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)
    def dib_basurero(self,screen,x,y):
        largo=70
        sum=10
        base=50
        color=(190, 190, 190)
        pygame.draw.line(screen, color, (x, y), (x + largo, y), 10)
        pygame.draw.line(screen,color,(x+sum,y),(x+sum*2,y+largo),16)
        pygame.draw.line(screen,color,(x+sum*2,y+largo),(x+base,y+largo),5)
        pygame.draw.line(screen, color,(x + base, y + largo),(x+largo-sum,y),16)
        pygame.draw.line(screen,color,(x+sum*2,y-sum),(x+sum*5,y-sum),4)
        pygame.draw.line(screen, color, (x + sum * 2, y), (x + sum * 2, y - sum), 4)
        pygame.draw.line(screen, color, (x + sum * 5, y - sum), (x + sum * 5, y ), 4)

        for i in range(largo):
            pygame.draw.line(screen,color, (x+sum*2,y + i), (x + base, y + i))
        pygame.draw.line(screen, (161, 152, 152), (x+sum+15, y+sum+5), (x+sum+15, y+base+sum), 3)
        pygame.draw.line(screen, (161, 152, 152), (x + sum*3.5, y + sum + 5), (x + sum*3.5, y + base + sum), 3)
        pygame.draw.line(screen, (161, 152, 152), (x + sum*4.5, y + sum + 5), (x + sum*4.5, y + base + sum), 3)
    def manejar_eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pos

            # Coordenadas y dimensiones del área del botón LED
            boton_led_x = self.x + 50
            boton_led_y = self.y + 50
            boton_led_ancho = 100
            boton_led_alto = 100

            # Verificar si el clic está dentro del área del botón LED
            if boton_led_x <= mouse_x <= boton_led_x + boton_led_ancho and boton_led_y <= mouse_y <= boton_led_y + boton_led_alto:
                self.accion_boton_led()

            # Coordenadas y dimensiones del área del botón Switch
            boton_switch_x = self.x + 80
            boton_switch_y = self.y + 210
            boton_switch_ancho = 100
            boton_switch_alto = 100

            # Verificar si el clic está dentro del área del botón Switch
            if boton_switch_x <= mouse_x <= boton_switch_x + boton_switch_ancho and boton_switch_y <= mouse_y <= boton_switch_y + boton_switch_alto:
                self.accion_boton_switch()

            # Coordenadas y dimensiones del área del botón Basurero
            boton_basurero_x = self.x + 64
            boton_basurero_y = self.y + 340
            boton_basurero_ancho = 100
            boton_basurero_alto = 100

            # Verificar si el clic está dentro del área del botón basurero
            if boton_basurero_x <= mouse_x <= boton_basurero_x + boton_basurero_ancho and boton_basurero_y <= mouse_y <= boton_basurero_y + boton_basurero_alto:
                self.accion_boton_basurero()
    def accion_boton_led(self):
        #print("Botón LED presionado")
        global boton_led
        if boton_led == False:
            boton_led = True
        else:
            boton_led = False
        print("led_b",boton_led)
    def accion_boton_switch(self):
        #print("Botón Switch presionado")
        global boton_switch
        if boton_switch == False:
            boton_switch = True
        else:
            boton_switch = False
        print(boton_switch)
    def accion_boton_basurero(self):
        #print("Botón Basurero presionado")
        pass

    def dibujar_flecha(self,interruptor,x,y):

        line_color =  (39, 174, 96) if interruptor else "red"
        pygame.draw.line(screen, line_color, (x, y), (x + 100, y), 6)
        pygame.draw.line(screen, line_color, (x + 25, y + 25), (x, y), 6)
        pygame.draw.line(screen, line_color, (x + 25, y - 25), (x, y), 6)
class Cableado:
    def __init__(self):
        self.dibujando_cable = False
        self.inicio_cable = None
        self.cables = []

    def dibujar_cables(self):
        for cable in self.cables:
            pygame.draw.line(screen, "black", (cable[0].x, cable[0].y), (cable[1].x, cable[1].y), 3)

    def comienzo_cable(self, conector_origen):
        self.inicio_cable = conector_origen
        self.dibujando_cable = True


    def finalizar_cable(self, conector_siguiente):
        if not self.quitar_cable(self.inicio_cable, conector_siguiente):
            self.cables.append((self.inicio_cable, conector_siguiente))
            self.inicio_cable.agregar_conexion(conector_siguiente)
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
            pygame.draw.line(screen, "black", (self.inicio_cable.x, self.inicio_cable.y), current_pos, 3)

    def obtener_indices_conector(self,nombre):

        if nombre in ["pila-", "pila+"]:
            return -1, -1

        partes = nombre.split("_")
        if len(partes) == 3:
            i = int(partes[1])
            j = int(partes[2])
            return i, j
        else:
            return None

    def validar_corriente(self, conectores, conector_inicio, conector_final):
        actual = conector_inicio
        visitados = set()
        polo_positivo = False
        polo_negativo = False


        #buscar conectores positivos y negativos
        name_positivos = {f"conector1_1_{i}" for i in range(30)} | {f"conector2_1_{i}" for i in range(30)}
        name_negativos = {f"conector1_0_{i}" for i in range(30)} | {f"conector2_0_{i}" for i in range(30)}

        while actual:
            # verificar si el conector actual es positivo o negativo
            if actual.nombre in name_positivos:
                polo_positivo = True
            if actual.nombre in name_negativos:
                polo_negativo = True

            if conector_final in actual.conexiones:
                if polo_positivo and polo_negativo:
                    return True
                return False

            visitados.add(actual)

            #encuentra el siguiente conector no visitado
            siguiente_conector = None
            for conexion in actual.conexiones:
                if conexion not in visitados:
                    siguiente_conector = conexion
                    break

            if siguiente_conector:
                actual = siguiente_conector
            else:
                break #no hay mas conectores

        return False
class Led:
    def __init__(self,color,x,y,x1,x2,y1,y2):
        self.color=color
        self.x=x
        self.y=y
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def led_apagada(self,screen):
        pygame.draw.line(screen, (0, 0, 0, 0), (self.x1, self.y1), (self.x, self.y), 2)
        pygame.draw.line(screen, (0, 0, 0, 0), (self.x2, self.y2), (self.x, self.y), 2)
        for angle in range(0, 360, 3):
            circle_radius = 6
            start_x = self.x
            start_y = self.y
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen,self.color, (start_x, start_y), (end_x, end_y), 2)
class Switch:
    def __init__(self,x,y,x1,x2,y1,y2):
        self.x=x
        self.y=y
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def switch_proto(self,screen):
        lado = 20  # Tamaño del switch (cuadrado)
        body_color = (150, 150, 150)
        circle_radius = 5  # Radio del "círculo" en el medio
        pygame.draw.line(screen, (0, 0, 0, 0), (self.x1, self.y1), (self.x+lado//2, self.y+lado//2), 2)#patita 1
        pygame.draw.line(screen, (0, 0, 0, 0), (self.x2, self.y2), (self.x+lado//2, self.y+lado//2), 2)#patita 2
        for i in range(lado):
            pygame.draw.line(screen, body_color, (self.x, self.y + i), (self.x + lado,self.y + i))
        # Dibujar el "círculo" en el centro
        for angle in range(0, 360, 10):
            start_x = self.x + lado // 2
            start_y = self.y + lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)
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
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.85)

# Crear la ventana con el tamaño ajustado
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

#Crear el cableado
cableado = Cableado()
fullscreen = False
running = True
x1 = 0
x2 = 0
y1 = 0
y2 = 0
guardar_led=[]
guardar_switch=[]
ultimo_conector= None

# Variables para controlar la animación
global interruptor
interruptor = False

global interruptor2
interruptor2 = False

global interruptor3
interruptor3 = False

while running:
    screen.fill("white") # directo el color sin variables extra

    x_proto = (screen.get_width() - 840) // 2
    y_proto = (screen.get_height() - 400) // 2

    # Crear y dibujar Protoboard

    protoboard = Protoboard(x_proto, y_proto)
    protoboard.crear(screen)

    # Crear y dibujar Pila

    x_pila = (screen.get_width() - 1100) // 2
    y_pila = (screen.get_height() - 150) // 2

    pila = Pila(x_pila, y_pila)
    pila.dibujarPila(screen)

    # Crear y dibujar Menu
    x_menu = x_proto + 700
    y_menu = y_proto - 20

    menu = Menu(x_menu,y_menu)
    menu.dibujar(screen)
    clock = pygame.time.Clock()

    def buscar_conector_por_nombre(nombre, lista_conectores):
        for conector in lista_conectores:
            if conector.nombre == nombre:
                return conector
        return None

    def distancia(punto1, punto2):
        return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)
    def punto_mas_cercano(pos_mouse, lista_conectores, distancia_maxima):
        punto_cercano = None
        distancia_minima = 10000

        for conector in lista_conectores:
            conector_pos = (conector.x, conector.y)  # Extrae las coordenadas del conector
            dist = distancia(pos_mouse, conector_pos)
            if dist < distancia_minima and dist <= distancia_maxima:
                distancia_minima = dist
                punto_cercano = conector
        return punto_cercano

    distancia_maxima = 10

    cableado.dibujar_cables()
    for i in guardar_led:
        i.led_apagada(screen)

    for i in guardar_switch:
        i.switch_proto(screen)
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
            x, y = event.pos

            if boton_led ==True:
                if not conector_cercano:
                    print( )
                elif x1 ==0:
                    x1=conector_cercano.x
                    y1=conector_cercano.y
                else:
                    x2 =conector_cercano.x
                    y2=conector_cercano.y
                    if (((x1+40)>=x2) or ((x1-40)<=x2) or (x1==x2) )and (((y1+40)<=y2) or ((y1-40)>=y2) or (y1==y2)):
                        x_mitad, y_mitad = ((x1 + x2) / 2, (y1 + y2) / 2)
                        led_a = Led((160, 0, 0), x_mitad, y_mitad, x1, x2, y1, y2)
                        led_a.led_apagada(screen)
                        x1, x2, y1, y2 = 0, 0, 0, 0
                        boton_led = False
                        guardar_led.append(led_a)

            elif boton_switch==True:
                if not conector_cercano:
                    print( )
                elif x1==0:
                    x1 = conector_cercano.x
                    y1 = conector_cercano.y
                else:
                    x2 = conector_cercano.x
                    y2 = conector_cercano.y
                    if (((x1+40)>=x2) or ((x1-40)<=x2) or (x1==x2) )and (((y1+40)<=y2) or ((y1-40)>=y2) or (y1==y2)):
                        x_mitad, y_mitad = (((x1 + x2) / 2)-10, ((y1 + y2) / 2)-10)
                        switch_a = Switch(x_mitad, y_mitad, x1, x2, y1, y2)
                        switch_a.switch_proto(screen)
                        x1, x2, y1, y2 = 0, 0, 0, 0
                        boton_switch = False
                        guardar_switch.append(switch_a)


            elif conector_cercano and boton_led == False and boton_switch == False:

                for conector in conectores:

                    if conector_cercano == conector:

                        if not cableado.dibujando_cable:

                            cableado.comienzo_cable(conector)
                        else:
                            cableado.finalizar_cable(conector)
                            ultimo_conector = conector_cercano
        
        if event.type == pygame.QUIT:
            running = False
        menu.manejar_eventos(event)

        # Buscar pila+ y pila- en la lista conectores
        conector_pila1 = buscar_conector_por_nombre("pila+", conectores)
        conector_pila2 = buscar_conector_por_nombre("pila-", conectores)
        rrr = cableado.validar_corriente(conectores, conector_pila1, conector_pila2)
        if rrr:
            print("||| HAY CORRIENTE |||")

    cableado.dibujar_cable_actual()

        #esto define el dibujo de las flechas acorde a la resolucion (interruptor x,y)
    if boton_led: 
        menu.dibujar_flecha(interruptor, x_menu + 220, y_menu + 90) #valor referencial para las flechas
        
    elif boton_switch: 
        menu.dibujar_flecha(interruptor2, x_menu + 220, y_menu + 240)

    elif interruptor3:
        menu.dibujar_flecha(interruptor3, 1500, 660)

    elif interruptor  and interruptor2:
        interruptor2 = False
        interruptor = False
    
    elif interruptor and interruptor3:
        interruptor3 = False
        interruptor = False
        
    elif interruptor2 and interruptor3:
        interruptor2 = False
        interruptor3 = False

    elif interruptor and interruptor2  and interruptor3:
        interruptor = False
        interruptor2 = False
        interruptor3 = False

    pygame.display.flip()
    mainClock.tick(30)

pygame.quit()
