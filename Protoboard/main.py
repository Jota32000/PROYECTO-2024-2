import pygame
import math
from pygame.locals import *

####################################
global CONECTORES_SIZE
CONECTORES_SIZE = 1  # para no tener mas elementos de los necesarios
####################################


class Conector:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.largo = 5
        self.color = (84, 84, 84)
        self.conexiones = []
        self.fase = None
        self.neutro = None
        self.padre = self

    def dibujar(self, screen):
        for i in range(self.largo):
            # dibuja los puntos protoboard
            partes = self.nombre.split("_")
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))

    def eliminar_padre(self):
        self.padre = self

    def __str__(self):
        return f"{self.nombre}\nx={self.x} y={self.y})\n"

    def agregar_conexion(self, conector_destino):
        if conector_destino not in self.conexiones:
            self.conexiones.append(conector_destino)
            """print("##########################################################")
            print("origen: ", self.nombre, "\ndestino: ", conector_destino)
            if self.conexiones:
                print("----------- Lista conexiones -----------")
                print("largo: ", len(self.conexiones))
                self.imprimir_conexiones()"""

    def clean_conexion(self, otro_conector):
        if otro_conector in self.conexiones:
            self.conexiones.remove(otro_conector)

    """def imprimir_conexiones(self):
        print(f">>> Conexiones de {self.nombre}:")
        for conector in self.conexiones:
            print(conector)"""
 
conectores = [] 
 
boton_led = False #Estado del boton de la led (activado = true o desactivado = false) 
boton_switch = False #Estado del boton del switch (activado = true o desactivado = false) 
boton_basurero = False #Estado del boton del basurero (activado=true o desactivado = false)

cables = []

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

        #fors
        for i in range(2): 
            for j in range(num_columnas): 
                x_pos = inicio_x + j * separacion_x 
                y_pos = inicio_y + i * 20 
                nombre_c1 = f"conector1_{i}_{j}" 
                conector = Conector(nombre_c1, x_pos, y_pos)
                if CONECTORES_SIZE:
                    conectores.append(conector)
                conector.dibujar(screen)
 
        for i in range(2): 
            for j in range(num_columnas): 
                x_pos = inicio_x + j * separacion_x 
                y_pos = inicio_y + i * 20 
                nombre_c2 = f"conector2_{i}_{j}" 
                conector = Conector(nombre_c2, x_pos, y_pos + self.ancho - 64)
                if CONECTORES_SIZE:
                    conectores.append(conector)
                conector.dibujar(screen) 
 
        for i in range(num_filas): 
            y_pos = inicio_y + i * 20 
            for j in range(num_columnas): 
                x_pos = inicio_x + j * separacion_x 
                nombre_c3 = f"conector3_{i}_{j}" 
                conector = Conector(nombre_c3, x_pos, y_pos + 70)
                if CONECTORES_SIZE:
                    conectores.append(conector)
                conector.dibujar(screen) 
 
        for i in range(num_filas): 
            y_pos = inicio_y + i * 20 
            for j in range(num_columnas): 
                x_pos = inicio_x + j * separacion_x 
                nombre_c4 = f"conector4_{i}_{j}" 
                conector = Conector(nombre_c4, x_pos, y_pos + 210)
                if CONECTORES_SIZE:
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

        if CONECTORES_SIZE:
            conector_pila1 = Conector("pila+", self.pila_x + 65, self.pila_y - 15) #positivo
            conectores.append(conector_pila1)

            conector_pila2 = Conector("pila-", self.pila_x + 35, self.pila_y - 15) #negativo
            conectores.append(conector_pila2)
            conector_pila1.fase = True
            conector_pila2.neutro = True
 
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
            boton_switch_y = self.y + 180 
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
        print("Botón LED presionado") 
        global boton_led 
        if boton_led == False: 
            boton_led = not boton_led  
        else:
            boton_led = not boton_led  # Desactivar el LED  
        #print("led_b",boton_led) 
    def accion_boton_switch(self): 
        print("Botón Switch presionado") 
        global boton_switch 
        if boton_switch == False: 
            boton_switch = not boton_switch
        else:
            boton_switch = not boton_switch  # Desactivar el switch
        #print(boton_switch) 
    def accion_boton_basurero(self):
        #print("Botón Basurero presionado") 
        global boton_basurero
        if boton_basurero == False: 
            boton_basurero = not boton_basurero
        else:
            boton_basurero = not boton_basurero  # Desactivar el basurero
 
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
            if cable[0].fase or cable[1].neutro:  # listo creo
                pygame.draw.line(screen, "violet", (cable[0].x, cable[0].y), (cable[1].x, cable[1].y), 3)
            else:
                pygame.draw.line(screen, "black", (cable[0].x, cable[0].y), (cable[1].x, cable[1].y), 3)

    def encontrar(self, conector):
        actual = conector

        while actual != actual.padre:
            actual = actual.padre

        nodo_actual = conector  # actual es el padre
        while nodo_actual != nodo_actual.padre:
            siguiente = nodo_actual.padre  # swap de toda la vida pero con nodos
            nodo_actual.padre = actual
            nodo_actual = siguiente

        return actual

    def union(self, conector1, conector2):
        nodo1 = self.encontrar(conector1)
        nodo2 = self.encontrar(conector2)

        if nodo1 != nodo2:
            if len(nodo1.conexiones) >= len(nodo2.conexiones):
                nodo2.padre = nodo1
            else:
                nodo1.padre = nodo2
        ####################################################

        # dudo de la legalidad de esto... consultar mas tarde
        # print(nodo1.nombre, nodo1.padre.nombre, nodo2.nombre,nodo2.padre.nombre)

    def nuevo_padre(self, conector):
        print("///////// nuevo padre ///////////////////")

        conector.eliminar_padre()
        for conectado in conector.conexiones:
            self.union(conector, conectado)

    def comienzo_cable(self, conector_origen):
        self.inicio_cable = conector_origen
        self.dibujando_cable = True

    def energy_fila(self, conector):

        nombre = conector.nombre
        partes = nombre.split("_")

        if len(partes) == 3:
            name = partes[0]
            i = int(partes[1])
            j = 0

        for cable in conectores:
            if cable.nombre == f"{name}_{i}_{j}":

                if conector.fase:
                    cable.fase = True
                elif conector.neutro:
                    cable.neutro = True
                cable.padre = conector.padre
                # print("siu2", cable.nombre, cable.padre.nombre)
                j += 1

    ############################

    def energy_col(self, conector):
        nombre = conector.nombre
        partes = nombre.split("_")

        if len(partes) == 3:
            name = partes[0]
            i = 0
            j = int(partes[2])

        for cable in conectores:
            if cable.nombre == f"{name}_{i}_{j}":
                if conector.fase:
                    cable.fase = True
                elif conector.neutro:
                    cable.neutro = True
                cable.padre = conector.padre
                print("========= cc ===========")
                print("colum", cable.nombre, cable.padre.nombre)
                print("========= cc =========== fin")
                i += 1

    def verificar_y_quitar_corriente(self, conector):
        print("conector: ", conector.nombre)
        self.conexiones = []
        nombre = conector.nombre

        partes = nombre.split("_")
        name = partes[0]
        if "conector1" in conector.nombre or "conector2" in conector.nombre:

            i = int(partes[1])
            j = 0
            bandera = True
            fase = False

            for cable in conectores:
                if cable.nombre == f"{name}_{i}_{j}":
                    if cable.conexiones:
                        for conexion in cable.conexiones:
                            print(f">> {conexion.nombre}")
                            if conexion.nombre == "pila+":
                                bandera = False
                                fase = True
                                print("toca")
                            elif conexion.nombre == "pila-":
                                bandera = False
                                break
                    j += 1

            j = 0
            # si no hay pila
            if not bandera:
                for cable in conectores:
                    if cable.nombre == f"{name}_{i}_{j}":

                        if fase:
                            cable.fase = True
                            print(f">>{cable.nombre} padre {cable.padre.nombre}:")
                            cable.padre = conector.padre
                        else:
                            cable.neutro = True
                            cable.padre = conector.padre
                        j += 1

            else:
                for cable in conectores:
                    if cable.nombre == f"{name}_{i}_{j}":
                        cable.fase = False
                        cable.neutro = False
                        j += 1


        else:

            # la misma wea pero cols
            i = 0
            j = int(partes[2])

        bandera = True
        fase = False
        for cable in conectores:
            if cable.nombre == f"{name}_{i}_{j}":
                if cable.conexiones:
                    print(f"Conexiones de {cable.nombre}:")
                    for conexion in cable.conexiones:
                        print(f">> {conexion.nombre}")
                        if conexion.nombre == "pila+":
                            bandera = False
                            fase = True
                        elif conexion.nombre == "pila-":
                            bandera = False
                            break
                i += 1
        i = 0
        # si no hay pila
        if not bandera:
            for cable in conectores:
                if cable.nombre == f"{name}_{i}_{j}":

                    if fase:
                        cable.fase = True
                        print(f">>{cable.nombre} padre {cable.padre.nombre}:")
                        cable.padre = conector.padre
                    else:
                        cable.neutro = True
                        cable.padre = conector.padre
                    i += 1

        else:
            for cable in conectores:
                if cable.nombre == f"{name}_{i}_{j}":
                    cable.fase = False
                    cable.neutro = False
                    i += 1

    def finalizar_cable(self, conector_siguiente):
        if self.inicio_cable.nombre == conector_siguiente.nombre:
            print("----------------------------")
            print("selecciono un punto")
            print("eso no es valido")
            print("----------------------------")
            self.dibujando_cable = False
            self.inicio_cable = None
            return
        if ((self.inicio_cable.fase and conector_siguiente.neutro) or (
                self.inicio_cable.neutro and conector_siguiente.fase)):
            print("----------------------------------")
            print("corto de pixar")
            print("no puede conectar neutro y fase")
            print("----------------------------------")
            self.dibujando_cable = False
            self.inicio_cable = None
            return

        if not self.quitar_cable(self.inicio_cable, conector_siguiente):
            self.cables.append((self.inicio_cable, conector_siguiente))

            self.inicio_cable.agregar_conexion(conector_siguiente)
            conector_siguiente.agregar_conexion(self.inicio_cable)
            self.union(self.inicio_cable, conector_siguiente)
            print("||| ", self.inicio_cable.nombre, self.inicio_cable.padre.nombre, conector_siguiente.nombre,
                  conector_siguiente.padre.nombre)

            if self.inicio_cable.fase:
                conector_siguiente.fase = True
                if (
                        "conector1" in conector_siguiente.nombre or "conector2" in conector_siguiente.nombre) and conector_siguiente.nombre != "pila+" and conector_siguiente.nombre != "pila-":
                    self.energy_fila(conector_siguiente)

                else:
                    if (conector_siguiente.nombre != "pila+") and (conector_siguiente.nombre != "pila-"):
                        self.energy_col(conector_siguiente)

            if conector_siguiente.fase:

                self.inicio_cable.fase = True
                if (
                        "conector1" in self.inicio_cable.nombre or "conector2" in self.inicio_cable.nombre) and self.inicio_cable.nombre != "pila+" and self.inicio_cable.nombre != "pila-":
                    self.energy_fila(self.inicio_cable)

                else:
                    if self.inicio_cable.nombre != "pila+" and self.inicio_cable.nombre != "pila-":
                        self.energy_col(self.inicio_cable)

            if self.inicio_cable.neutro:
                conector_siguiente.neutro = True

                if (
                        "conector1" in conector_siguiente.nombre or "conector2" in conector_siguiente.nombre) and conector_siguiente.nombre != "pila+" and conector_siguiente.nombre != "pila-":
                    self.energy_fila(conector_siguiente)

                else:
                    if conector_siguiente.nombre != "pila+" and conector_siguiente.nombre != "pila-":
                        self.energy_col(conector_siguiente)

            if conector_siguiente.neutro:

                self.inicio_cable.neutro = True
                if ("conector1" in self.inicio_cable.nombre or "conector2" in self.inicio_cable.nombre) and self.inicio_cable.nombre != "pila+" and self.inicio_cable.nombre != "pila-":
                    self.energy_fila(self.inicio_cable)

                else:
                    if self.inicio_cable.nombre != "pila+" and self.inicio_cable.nombre != "pila-":
                        self.energy_col(self.inicio_cable)

        self.dibujando_cable = False
        self.inicio_cable = None

    def quitar_cable(self, start, end):

        for cable in self.cables:

            if (cable[0] == start and cable[1] == end) or (cable[0] == end and cable[1] == start):

                # quita la fase y neutro de los nodos

                # mata las conexiones entre los conectores
                self.nuevo_padre(start)
                self.nuevo_padre(end)
                start.clean_conexion(end)
                end.clean_conexion(start)

                ########################################

                if (start.nombre != "pila+" and start.nombre != "pila-") and (
                        end.nombre != "pila+" and end.nombre != "pila-"):

                    print("conexiones de ", start.nombre, start.conexiones, " y ", end.nombre, end.conexiones)
                    print(end.nombre)
                    self.verificar_y_quitar_corriente(end)
                    self.verificar_y_quitar_corriente(start)
                    print(start.fase, start.neutro, end.fase, end.neutro)
                else:

                    for c in conectores:
                        if "pila" not in c.nombre:
                            c.fase = False
                            c.neutro = False

                self.cables.remove(cable)

                return True

            if cable[0] == start or cable[1] == start or cable[0] == end or cable[1] == end:
                return True

        return False

    def dibujar_cable_actual(self):
        if self.dibujando_cable and self.inicio_cable:
            current_pos = pygame.mouse.get_pos()

            if self.inicio_cable.fase or self.inicio_cable.neutro:  # listo
                pygame.draw.line(screen, "violet", (self.inicio_cable.x, self.inicio_cable.y), current_pos, 3)
            else:
                pygame.draw.line(screen, "black", (self.inicio_cable.x, self.inicio_cable.y), current_pos, 3)



class Led:
    def __init__(self,color,x,y,x1,x2,y1,y2): 
        self.color=color 
        self.x = x 
        self.y = y 
        self.x1 = x1 
        self.x2 = x2 
        self.y1 = y1 
        self.y2 = y2

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

class Basurero:
    def __init__(self):
        #No presenta atributos
        pass
    def eliminar_led(self,x,y):
        rango_click = 10
        #Buscador de led en la lista de los leds
        for led in guardar_led:
            #si se clickea en el rango correspondiente, se borra de la lista led
            if led.x - rango_click <= x <= led.x + rango_click and led.y - rango_click <= y <= led.y + rango_click:
                guardar_led.remove(led)
    def eliminar_switch(self,x,y):
        rango_click = 10
        #Buscador de led en la lista de los switchs
        for switch in guardar_switch:
            #si se clickea en el rango correspondiente, se borra de la lista switch
            if switch.x - rango_click <= x <= switch.x + rango_click and switch.y - rango_click <= y <= switch.y + rango_click:
                guardar_switch.remove(switch)

    def eliminar_cable(self,x,y):
        rango_click = 10
        #Buscador de cable en la lista de los cables
        for cable in cables:
            #si se clickea en el rango correspondiente, se borra de la lista cable
            if cable[0].x - rango_click <= x <= cable[0].x + rango_click and cable[0].y - rango_click <= y <= cable[0].y + rango_click:
                cables.remove(cable)

            elif cable[1].x - rango_click <= x <= cable[1].x + rango_click and cable[1].y - rango_click <= y <= cable[1].y + rango_click:
                cables.remove(cable)

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
 
    # Crear y dibujar Menú
    x_menu = x_proto + 700 
    y_menu = y_proto - 20 
 
    menu = Menu(x_menu,y_menu) 
    menu.dibujar(screen) 
    
    # Crear funcionalidad de basurero
    
    basurero = Basurero()
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

    # Manejo de eventos de la pantalla
    
    for event in pygame.event.get(): 
 
        if event.type == QUIT or event.type == K_ESCAPE or event.type == pygame.QUIT: 
            running = False 
        if event.type == VIDEORESIZE: 
            if not fullscreen: 
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE) 
 
        if event.type == KEYDOWN: 
            if event.key == K_f: 
                fullscreen = not fullscreen 
                if fullscreen: 
                    screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN) 
                else: 
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE) 

        #manejo de eventos especial para que cuando se quiera eliminar un item, se elimine bien y no se quiera agregar un cable

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and boton_basurero:
                cableado = Cableado()
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                basurero.eliminar_led(mouse_x, mouse_y)
                basurero.eliminar_switch(mouse_x, mouse_y)
                basurero.eliminar_cable(mouse_x, mouse_y)
                boton_basurero = not boton_basurero
                        
        #manejo de eventos normal para cables, led y switch

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and boton_basurero == False:  
            mouse_pos = event.pos 
            conector_cercano = punto_mas_cercano(mouse_pos, conectores, distancia_maxima) 
            x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                conector_cercano = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                x, y = event.pos

                if boton_led == True:
                    if not conector_cercano:
                        print()
                    elif x1 == 0:
                        x1 = conector_cercano.x
                        y1 = conector_cercano.y
                    else:
                        x2 = conector_cercano.x
                        y2 = conector_cercano.y
                        if (((x1 + 40) >= x2) or ((x1 - 40) <= x2) or ((x1 + 20) <= x2) or ((x1 - 20) <= x2)) and (((y1 + 40) <= y2) or ((y1 - 40) >= y2) or ((y1 + 20) <= y2) or ((y1 - 20) <= y2)) and ( x1 - x2) <= 40 and (x2 - x1) <= 40 and (y2 - y1) <= 40 and (y1 - y2) <= 40:
                            x_mitad, y_mitad = ((x1 + x2) / 2, (y1 + y2) / 2)
                            led_a = Led((160, 0, 0), x_mitad, y_mitad, x1, x2, y1, y2)
                            led_a.led_apagada(screen)
                            x1, x2, y1, y2 = 0, 0, 0, 0
                            boton_led = False
                            guardar_led.append(led_a)

                elif boton_switch == True:
                    if not conector_cercano:
                        print()
                    elif x1 == 0:
                        x1 = conector_cercano.x
                        y1 = conector_cercano.y
                    else:
                        x2 = conector_cercano.x
                        y2 = conector_cercano.y
                        if (((x1 + 40) >= x2) or ((x1 - 40) <= x2) or ((x1 + 20) <= x2) or ((x1 - 20) <= x2)) and (((y1 + 40) <= y2) or ((y1 - 40) >= y2) or ((y1 + 20) <= y2) or ((y1 - 20) <= y2)) and (x1 - x2) <= 40 and (x2 - x1) <= 40 and (y2 - y1) <= 40 and (y1 - y2) <= 40:
                            x_mitad, y_mitad = (((x1 + x2) / 2) - 10, ((y1 + y2) / 2) - 10)
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


        
        #Manejo de evento del menú
        
        menu.manejar_eventos(event) 
 
        #Buscar pila+ y pila- en la lista conectores 
        #conector_pila1 = buscar_conector_por_nombre("pila+ ", conectores) 
        #conector_pila2 = buscar_conector_por_nombre("pila- ", conectores) 
        #rrr = cableado.validar_corriente(conectores, conector_pila1, conector_pila2) 
        #if rrr: 
        #    print("||| HAY CORRIENTE |||") 
                 
    cableado.dibujar_cable_actual()

    #Esto define el dibujo de las flechas acorde a la resolucion (interruptor x,y) 
    if boton_led:  
        menu.dibujar_flecha(boton_led, x_menu + 220, y_menu + 100) #valor referencial para las flechas 
         
    elif boton_switch:  
        menu.dibujar_flecha(boton_switch, x_menu + 220, y_menu + 240) #valor referencial para las flechas
 
    elif boton_basurero:  
        menu.dibujar_flecha(boton_basurero, x_menu + 220, y_menu + 380) #valor referencial para las flechas
 
    elif boton_led  and boton_switch: 
        boton_led = False 
        boton_switch = False 
     
    elif boton_led and boton_basurero: 
        boton_led = False 
        boton_basurero = False 
         
    elif boton_switch and boton_basurero: 
        boton_switch = False 
        boton_basurero = False 
 
    elif boton_led and boton_switch and boton_basurero: 
        boton_led = False 
        boton_switch = False 
        boton_basurero = False


        ##################### Muestra donde hay o no energy ######################
    def dibujar_conectores(screen, conectores):
        for conector in conectores:
            if conector.fase:
                pygame.draw.line(screen, "red", (conector.x, conector.y), (conector.x + conector.largo, conector.y),
                                 6)
            elif conector.neutro:
                pygame.draw.line(screen, "blue", (conector.x, conector.y),
                                 (conector.x + conector.largo, conector.y), 6)

        ############################################################################


    dibujar_conectores(screen, conectores)

    pygame.display.flip()
    CONECTORES_SIZE = 0  # evita exceso conectores
    mainClock.tick(60)

pygame.quit()