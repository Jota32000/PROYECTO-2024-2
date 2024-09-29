import pygame
import math
from pygame.locals import *

global CONECTORES_SIZE
CONECTORES_SIZE = 1  # para no tener mas elementos de los necesarios
class Conector:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.fase = None
        self.neutro = None
        self.largo = 5
        self.color = (84, 84, 84)
        self.conexiones = []
        self.padre = self

    def dibujar(self, screen):
        for i in range(self.largo):
            # dibuja los puntos protoboard
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))


    """def __str__(self):
        return f"{self.nombre}\nx={self.x} y={self.y}"""


    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo) # conexion bidireccional A->B | B->A
        nodo.conexiones.append(self)
        cableado.actualizarbosque(self, nodo)
        """print("##########################################################")
        print("origen: ", self.nombre, "\ndestino: ", nodo.nombre)
        if self.conexiones:
            print("----------- Lista conexiones -----------")
            print("largo: ", len(self.conexiones))
            self.imprimir_conexiones()"""

    def eliminar_conexion(self,nodo, nodo_objetivo):
        if nodo_objetivo in self.conexiones: # ve que no se haya eliminado ya la conexion con ese nodo
            nodo.conexiones.remove(nodo_objetivo)
            nodo_objetivo.conexiones.remove(nodo)
            cableado.buscar_conexiones(nodo, nodo_objetivo)


    """def imprimir_conexiones(self):
        print(f">>> Conexiones de {self.nombre}:")
        for conector in self.conexiones:
            print(conector)"""

conectores = []
boton_cable = False #Estado del boton del cable (activado = true o desactivado = false)
boton_led = False #Estado del boton de la led (activado = true o desactivado = false)
boton_switch = False #Estado del boton del switch (activado = true o desactivado = false)
boton_edicion = False #Estado del boton de edición (activado = true o desactivado = false)
boton_basurero = False #Estado del boton del basurero (activado=true o desactivado = false)
cables = []
conectores_cables = []
edicion_coordenadas = []
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

        for j in range(num_columnas):
            primer_conector_columna = None  # guarda el primer nodo de cada columna

            for i in range(num_filas):
                y_pos = inicio_y + i * 20
                x_pos = inicio_x + j * separacion_x
                nombre_c3 = f"conector3_{i}_{j}"
                conector = Conector(nombre_c3, x_pos, y_pos + 70)
                if CONECTORES_SIZE:
                    conectores.append(conector)
                conector.dibujar(screen)

                # conectar con el primer nodo de la columna
                if i == 0:
                    primer_conector_columna = conector  # guardar el primer nodo de la columna
                else:
                    primer_conector_columna.agregar_conexion(conector)
        # solo repito el proceso
        for j in range(num_columnas):
            primer_conector_columna = None

            for i in range(num_filas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                nombre_c4 = f"conector4_{i}_{j}"
                conector = Conector(nombre_c4, x_pos, y_pos + 210)

                if CONECTORES_SIZE:
                    conectores.append(conector)
                conector.dibujar(screen)
                if i == 0:
                    primer_conector_columna = conector
                else:
                    primer_conector_columna.agregar_conexion(conector)


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
        self.l1 = 640  # Ancho
        self.l2 = 130  # Alto
        self.color = (63, 129, 166)
        self.border_color = (0, 0, 0)
        self.border_thickness = 2
        self.border_radius = 10

        # Definir las áreas de colisión para los botones
        self.boton_led_x = self.x + 50
        self.boton_led_y = self.y + 50
        self.boton_led_ancho = 100
        self.boton_led_alto = 100

        self.boton_switch_x =  self.x + 50
        self.boton_switch_y =  self.y + 180
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
        self.dibujar_icono(screen,100,self.x + 20, self.y + 10)
        self.dib_cable(screen,self.x + 95, self.y - 15)
        self.dibujar_icono(screen,100,self.x + 145, self.y + 10)
        self.dib_led(screen, self.x + 170, self.y + 35)
        self.dibujar_icono(screen,100,self.x + 270, self.y + 10)
        self.dib_switch(screen, self.x + 300, self.y + 40)
        self.dibujar_icono(screen,100,self.x + 395, self.y + 10)
        self.dib_editor(screen,self.x + 420, self.y + 25)
        self.dibujar_icono(screen,100,self.x +520, self.y + 10)
        self.dib_basurero(screen,self.x + 535,self.y + 30)
        
        # Crear superficie para los botones semi-transparentes (para mostrar las áreas donde se puede hacer clic)
        boton_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # SRCALPHA para transparencia
        boton_led_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón LED
        boton_switch_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón Switch
        boton_basurero_surface = pygame.Surface((100,100),pygame.SRCALPHA) # Boton basurero
        boton_edicion_surface = pygame.Surface((100, 100), pygame.SRCALPHA) # Botón edición
        boton_cable_surface = pygame.Surface((100, 100), pygame.SRCALPHA) #Botón cable

        # Dibujar los botones en sus respectivas superficies
        self.dibujar_icono(boton_surface,0,0, 0)
        self.dib_led(boton_led_surface, 25, 15)
        self.dib_switch(boton_switch_surface, 25, 15)
        self.dib_basurero(boton_basurero_surface,25,15)
        self.dib_cable(boton_cable_surface, 25, 15)
        self.dib_editor(boton_edicion_surface, 25, 15)

        # Blit de las superficies a la pantalla principal
        screen.blit(boton_led_surface, (self.x + 145, self.y + 20))  # Botón LED en la pantalla   
    def dibujar_icono(self,screen,lado,x, y):
        y = y + 5
        color = (39, 174, 96)
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
    def dib_editor(self,screen,x,y):
        color = (229, 184, 0)
        cabeza = (255, 96, 96)
        #dibujo lapiz
        pygame.draw.line(screen,color,(x+25,y) , (x+25, y+70), 15)
        pygame.draw.line(screen,"white",(x+20,y+71), (x+25,y+80), 5)
        pygame.draw.line(screen,"white",(x+30,y+71), (x+25,y+80), 5)
        #cabeza lapiz
        pygame.draw.line(screen,cabeza,(x+18,y) , (x+32, y), 5)
        #ciclo para relleno
        for i in range(6):
            pygame.draw.line(screen,"white",(x+20,y+70), (x+20+i,y+70+1*i), 5)
            pygame.draw.line(screen,"white",(x+30,y+70), (x+20+i,y+70+1*i), 5)
        pygame.draw.line(screen,"black",(x+23,y+80), (x+27,y+80), 4)
    def dib_cable(self,screen,x,y):
        cobre = (255, 166, 60)
        pygame.draw.line(screen,"black",(x+10 ,y+80), (x-60 ,y+80), 7)
        pygame.draw.line(screen,cobre,(x+11 ,y+80), (x+15 ,y+80), 4)
        pygame.draw.line(screen,cobre,(x-61 ,y+80), (x-65 ,y+80), 4)
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
    def dibujar_recuadro_escogido(self,screen,lado,x,y):
        color = "red"
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
    def manejar_eventos(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pos

            # Coordenadas y dimensiones del área del boton cable
            boton_cable_x = self.x + 20
            boton_cable_y = self.y + 10
            boton_cable_ancho = 100
            boton_cable_alto = 100

            if boton_cable_x <= mouse_x <= boton_cable_x + boton_cable_ancho and boton_cable_y <= mouse_y <= boton_cable_y + boton_cable_alto:
                self.accion_boton_cable()

            # Coordenadas y dimensiones del área del botón LED
            boton_led_x = self.x + 145
            boton_led_y = self.y + 10
            boton_led_ancho = 100
            boton_led_alto = 100

            # Verificar si el clic está dentro del área del botón LED
            if boton_led_x <= mouse_x <= boton_led_x + boton_led_ancho and boton_led_y <= mouse_y <= boton_led_y + boton_led_alto:
                self.accion_boton_led()

            # Coordenadas y dimensiones del área del botón Switch
            boton_switch_x = self.x + 270
            boton_switch_y = self.y + 10            
            boton_switch_ancho = 100
            boton_switch_alto = 100

            # Verificar si el clic está dentro del área del botón Switch
            if boton_switch_x <= mouse_x <= boton_switch_x + boton_switch_ancho and boton_switch_y <= mouse_y <= boton_switch_y + boton_switch_alto:
                self.accion_boton_switch()

            # Coordenadas y dimensiones del área del botón Edición
            boton_edicion_x = self.x + 395                      
            boton_edicion_y = self.y + 10
            boton_edicion_ancho = 100
            boton_edicion_alto = 100

            # Verificar si el clic está dentro del área del botón Edición
            if boton_edicion_x <= mouse_x <= boton_edicion_x + boton_edicion_ancho and boton_edicion_y <= mouse_y <= boton_edicion_y + boton_edicion_alto:
                self.accion_boton_edicion()

            # Coordenadas y dimensiones del área del botón Basurero
            boton_basurero_x = self.x + 520
            boton_basurero_y = self.y + 10
            boton_basurero_ancho = 100
            boton_basurero_alto = 100

            # Verificar si el clic está dentro del área del botón basurero
            if boton_basurero_x <= mouse_x <= boton_basurero_x + boton_basurero_ancho and boton_basurero_y <= mouse_y <= boton_basurero_y + boton_basurero_alto:
                self.accion_boton_basurero()
    def accion_boton_cable(self):
        print("Botón Cable presionado")
        global boton_cable
        global boton_led
        boton_led = False
        global boton_switch
        boton_switch = False
        global boton_edicion
        boton_edicion = False
        global boton_basurero
        boton_basurero = False
        if boton_cable == False:
            boton_cable = not boton_cable
        else:
            boton_cable = not boton_cable  # Desactivar el cable
    def accion_boton_led(self):
        print("Botón LED presionado")
        global boton_cable
        boton_cable = False
        global boton_led
        global boton_switch
        boton_switch = False
        global boton_edicion
        boton_edicion = False
        global boton_basurero
        boton_basurero = False
        if boton_led == False:
            boton_led = not boton_led
        else:
            boton_led = not boton_led  # Desactivar el LED
        #print("led_b",boton_led)
    def accion_boton_switch(self):
        print("Botón Switch presionado")
        global boton_cable
        boton_cable = False
        global boton_led
        boton_led = False
        global boton_switch
        global boton_edicion
        boton_edicion = False
        global boton_basurero
        boton_basurero = False
        if boton_switch == False:
            boton_switch = not boton_switch
        else:
            boton_switch = not boton_switch  # Desactivar el switch
        #print(boton_switch)
    def accion_boton_edicion(self):
        print("Botón Edición presionado")
        global boton_cable
        boton_cable = False
        global boton_led       
        boton_led = False
        global boton_switch
        boton_switch = False
        global boton_edicion
        global boton_basurero
        boton_basurero = False
        if boton_edicion == True:
            boton_edicion = not boton_edicion    
        else:
            boton_edicion = not boton_edicion # Desactivar la edición
    def accion_boton_basurero(self):
        print("Botón Basurero presionado")
        global boton_cable
        boton_cable = False
        global boton_led
        boton_led = False
        global boton_switch
        boton_switch = False
        global boton_edicion
        boton_edicion = False
        global boton_basurero
        if boton_basurero == False:
            boton_basurero = not boton_basurero
        else:
            boton_basurero = not boton_basurero  # Desactivar el basurero
class Cableado:

    def __init__(self):
        self.dibujando_cable = False
        self.inicio_cable = None
    def dibujar_cables(self):
        for cable in cables:
            # verificar fase y neutro sino da problemas
            conector_inicio, conector_fin = cable[0], cable[1]

            if conector_inicio.fase or conector_inicio.neutro or conector_fin.fase or conector_fin.neutro:
                if conector_inicio.fase and conector_fin.fase:
                    color = (234, 79, 235) # morado
                elif conector_inicio.neutro and conector_fin.neutro:
                    color = (61, 205, 234) # azul cielo dark
                else:
                    color = "black"
            else:
                color = "black"
            pygame.draw.line(screen, color, (cable[0].x, cable[0].y), (cable[1].x, cable[1].y), 3)

    def comienzo_cable(self, conector_origen):
        self.inicio_cable = conector_origen
        self.dibujando_cable = True

    def energy_protoboard(self, pila_turno):
        for nodo in conectores: # ve los padres de p+ y p- segun eso da energy o no
            if pila_turno.nombre == "pila+":
                if nodo.padre.nombre == pila_turno.padre.nombre:
                    nodo.fase = True
                    nodo.neutro = False
                else:
                    nodo.fase = False
            elif pila_turno.nombre == "pila-":
                if nodo.padre.nombre == pila_turno.padre.nombre:
                    nodo.fase = False
                    nodo.neutro = True
                else:
                    nodo.neutro = False

    def finalizar_cable(self, conector_siguiente):

        if self.inicio_cable.nombre == conector_siguiente.nombre:
            print("----------------------------")
            print("Selecciono un punto")
            print("Eso no es valido")
            print("----------------------------")
            self.dibujando_cable = False
            self.inicio_cable = None
            return

        if ((self.inicio_cable.fase and conector_siguiente.neutro) or (
                self.inicio_cable.neutro and conector_siguiente.fase)):
            print("----------------------------------")
            print("Corto de pixar")
            print("No puede conectar neutro y fase")
            print("----------------------------------")
            self.activar_explosion()
            self.dibujando_cable = False
            self.inicio_cable = None
            return

        if "pila" in self.inicio_cable.nombre and conector_siguiente.nombre.startswith(("conector3_", "conector4_")):
            print("-------------------------------------------")
            print("Los cables de la pila solo van en los buses")
            print("-------------------------------------------")
            self.dibujando_cable = False
            self.inicio_cable = None
            return

        if not self.quitar_cable(self.inicio_cable, conector_siguiente):
            for cable in cables:
                if self.inicio_cable in cable or conector_siguiente in cable:
                    print("-------------------------------------------")
                    print("Ya hay un cable en este nodo")
                    print("-------------------------------------------")
                    self.dibujando_cable = False
                    self.inicio_cable = None
                    return
            # ------------------ Fin Validaciones de cables -------------------

            cables.append((self.inicio_cable, conector_siguiente))

            # si coloco de c3/c4 a c1 o c2 se pase la energia de fila a columna
            if (self.inicio_cable.nombre.startswith(("conector3_", "conector4_")) and
                    conector_siguiente.nombre.startswith(("conector1_", "conector2_"))):

                for nodo in conectores:
                    if nodo.y == conector_siguiente.y:
                        self.inicio_cable.agregar_conexion(nodo)

            # ---------------- Fin validacion fila columna -------------------

            elif self.inicio_cable.nombre in ["pila+", "pila-"] :
                for nodo in conectores:
                    if nodo.y == conector_siguiente.y:  # misma fila (solo c1 y c2)
                        self.inicio_cable.agregar_conexion(nodo)

            elif self.inicio_cable.nombre.startswith(("conector1_", "conector2_")) and conector_siguiente.nombre.startswith(("pila")):
                for nodo in conectores:
                    if nodo.y == self.inicio_cable.y:  # misma fila (solo c1 y c2)
                        conector_siguiente.agregar_conexion(nodo)

            else:
                for nodo in conectores:
                    if nodo.x == conector_siguiente.x:  # ver si estan en la misma columna | se limita el alcance
                        if conector_siguiente.nombre.startswith("conector3_"):
                            if nodo.nombre.startswith("conector3_") and nodo.nombre != self.inicio_cable.nombre:
                                self.inicio_cable.agregar_conexion(nodo)
                        elif conector_siguiente.nombre.startswith("conector4_"): # limita el rango de add solo a c4_
                            if nodo.nombre.startswith("conector4_") and nodo.nombre != self.inicio_cable.nombre:
                                self.inicio_cable.agregar_conexion(nodo)
        if self.inicio_cable.padre.nombre.startswith("pila"):
            print(self.inicio_cable.padre.nombre)
        self.dibujando_cable = False
        self.inicio_cable = None

    def quitar_cable(self, start, end):
        for cable in cables:

            if (cable[0] == start and cable[1] == end) or (cable[0] == end and cable[1] == start):
                cables.remove(cable)

                if start and end:

                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

                    if self.inicio_cable.nombre.startswith("pila"):
                        print("holalllllll")
                        end.padre = end
                        self.inicio_cable.padre = self.inicio_cable

                    # elimina conexiones en filas y columnas
                    if start.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in conectores:
                            if nodo.y == start.y:
                                nodo.eliminar_conexion(nodo, end)
                                end.eliminar_conexion(end, nodo)

                    elif start.nombre.startswith(("conector3_", "conector4_")):
                        for nodo in conectores:
                            if nodo.x == start.x:
                                nodo.eliminar_conexion(nodo, end)
                                end.eliminar_conexion(end, nodo)

                    # lo mismo para end
                    if end.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in conectores:
                            if nodo.y == end.y:
                                nodo.eliminar_conexion(nodo, start)
                                start.eliminar_conexion(start, nodo)

                    elif end.nombre.startswith(("conector3_", "conector4_")):
                        for nodo in conectores:
                            if nodo.x == end.x:
                                nodo.eliminar_conexion(nodo, start)
                                start.eliminar_conexion(start, nodo)


                return True
        return False
    def dibujar_cable_actual(self):
        if self.dibujando_cable and self.inicio_cable:
            current_pos = pygame.mouse.get_pos()
            if self.inicio_cable.fase:
                color = (234, 79, 235)
            elif self.inicio_cable.neutro:
                color = (61, 205, 234)
            else:
                color = "black"

            pygame.draw.line(screen, color, (self.inicio_cable.x, self.inicio_cable.y), current_pos, 3)


    def actualizarbosque(self, origen, destino):
        if origen.padre != destino.padre:
            coincidencia_origen = 0
            for nodo in conectores:
                if nodo.padre == origen.padre:
                    coincidencia_origen += 1

            coincidencia_destino = 0
            for nodo in conectores:
                if nodo.padre == destino.padre:
                    coincidencia_destino += 1

            if coincidencia_origen >= coincidencia_destino:
                nuevo_padre = origen.padre
                viejo_padre = destino.padre
            else:
                nuevo_padre = destino.padre
                viejo_padre = origen.padre

            self.actualizar_padre_subarbol(viejo_padre, nuevo_padre)

    def actualizar_padre_subarbol(self, viejo_padre, nuevo_padre):
        for nodo in conectores:
            if nodo.padre == viejo_padre:
                nodo.padre = nuevo_padre

    def buscar_conexiones(self,nodo, nodo_objetivo):
        visitados = []
        conneciones = []
        conneciones.append(nodo)
        existe_conexion_alternativa = False
        while (len(conneciones) > 0):
            actual = conneciones.pop(0)
            for i in actual.conexiones:
                if i not in visitados:
                    conneciones.append(i)
            visitados.append(actual)
            if nodo_objetivo in nodo.conexiones:
                existe_conexion_alternativa = True

        if existe_conexion_alternativa:
            for i in visitados:
                i.padre = nodo_objetivo
        else:
            nodo.padre = nodo
            for i in visitados:
                i.padre = nodo

    def activar_explosion(self):
        print("ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ")
        print("                   NUKE")
        print("∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨")

        screen.fill((243, 190, 49))
        pygame.display.flip()
        pygame.time.delay(100)

        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.delay(100)
        #----- QUITAR OBJETOS -----
        for nodo in conectores:
            if not nodo.nombre.startswith("pila"):
                nodo.fase = False
                nodo.neutro = False
            nodo.padre = nodo

        cables.clear()
        guardar_led.clear()
        guardar_switch.clear()
        #--------- FIN ---------
        return




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
        patita1 = punto_mas_cercano((self.x1, self.y1), conectores, distancia_maxima)
        patita2 = punto_mas_cercano((self.x2, self.y2), conectores, distancia_maxima)
        conector1 = None
        conector2 = None
        for i in conectores:
            if i.x == patita1.x and i.y == patita1.y:
                conector1 = i
            elif i.x == patita2.x and i.y == patita2.y:
                conector2 = i
        if conector1 == None or conector2== None:
            print("existe problemas en los conectores")
        corriente_conector1 = False
        if conector1.fase or conector1.neutro:
            corriente_conector1 = True
        # Verificar si conector2 tiene corriente
        corriente_conector2 = False
        if conector2.fase or conector2.neutro:
            corriente_conector2 = True

        if conector2.fase and conector1.fase:
            corriente_conector1 = True
            corriente_conector2 = False

        if conector2.neutro and conector1.neutro:
            corriente_conector1 = True
            corriente_conector2 = False

        # Cambiar color del LED según si ambos conectores tienen corriente
        if corriente_conector1 and corriente_conector2:
            self.color = (250, 0, 0)  # Color rojo para encendido
        else:
            self.color = (110, 0, 0)  # Color rojo oscuro para apagado

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
    def __init__(self, x, y, x1, x2, y1, y2):
        self.x = x
        self.y = y
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.estado=False
    def switch_proto(self, screen):
        lado = 20  # Tamaño del switch (cuadrado)
        body_color = (150, 150, 150)
        circle_radius = 5  # Radio del "círculo" en el medio
        # Dibujar patitas
        pygame.draw.line(screen, (0, 0, 0), (self.x1, self.y1), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 1
        pygame.draw.line(screen, (0, 0, 0), (self.x2, self.y2), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 2

        # Dibujar cuerpo del switch (con líneas)
        for i in range(lado):
            pygame.draw.line(screen, body_color, (self.x, self.y + i), (self.x + lado, self.y + i))

        # Dibujar el "círculo" en el centro usando líneas
        for angle in range(0, 360, 10):
            start_x = self.x + lado // 2
            start_y = self.y + lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

        # Dibujar botón (usando líneas para crear un borde)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + lado, self.y), 2)  # Línea superior
        pygame.draw.line(screen, (0, 0, 0), (self.x + lado, self.y), (self.x + lado, self.y + lado), 2)  # Línea derecha
        pygame.draw.line(screen, (0, 0, 0), (self.x + lado, self.y + lado), (self.x, self.y + lado),
                         2)  # Línea inferior
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + lado), (self.x, self.y), 2)  # Línea izquierda
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
        rango_click = 20
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
def switch_presionado(switch, mouse_pos):
    lado = 20  # Tamaño del switch (cuadrado)
    x, y = mouse_pos
    if switch.x <= x <= switch.x + lado and switch.y <= y <= switch.y + lado:
        return True
    return False
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
led_coordenadas = []
guardar_switch=[]
switch_coordenadas = []
ultimo_conector= None

while running:
    screen.fill("white") # directo el color sin variables extra

    x_proto = (screen.get_width() - 650) // 2 
    y_proto = (screen.get_height() - 300) // 2

    # Crear y dibujar Protoboard
    protoboard = Protoboard(x_proto, y_proto)
    protoboard.crear(screen)
    
    # Crear y dibujar Pila
    x_pila = (screen.get_width() - 950) // 2
    y_pila = (screen.get_height() - 50) // 2

    pila = Pila(x_pila, y_pila)
    pila.dibujarPila(screen)
    
    # Crear y dibujar Menú
    x_menu = x_proto 
    y_menu = y_proto - 200

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
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                basurero.eliminar_led(mouse_x, mouse_y)
                basurero.eliminar_switch(mouse_x, mouse_y)
                basurero.eliminar_cable(mouse_x, mouse_y)
                boton_basurero = False
        #manejo de eventos normal para cables, led y switch

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and boton_basurero == False:
            mouse_pos = pygame.mouse.get_pos()  # Obtén la posición del mouse
            for switch in guardar_switch:
                if switch_presionado(switch, mouse_pos):  # Verifica si un switch fue presionado
                    print(f"Switch presionado en coordenadas: ({switch.x}, {switch.y})")
                    patita1 = punto_mas_cercano((switch.x1,switch.y1), conectores, distancia_maxima)
                    patita2 = punto_mas_cercano((switch.x2,switch.y2), conectores, distancia_maxima)
                    conector_p1=None
                    conector_p2 = None
                    for i in conectores:
                        if i.x == patita1.x and i.y == patita1.y:
                            conector_p1 = i
                        elif i.x == patita2.x and i.y == patita2.y:
                            conector_p2 = i
                    if conector_p1==None or conector_p2== None:
                        print("existe problemas en los conectores")
                    if switch.estado== True:
                        conector_p1.eliminar_conexion(conector_p1,conector_p2)
                        switch.estado= False
                        print("Switch apagado")
                    if switch.estado==False:
                        conector_p1.agregar_conexion(conector_p2)
                        switch.estado= True
                        print("Switch encendido")

            mouse_pos = event.pos
            conector_cercano = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
            x, y = event.pos

            if boton_led:
                if not conector_cercano:
                    pass
                    #print(" ")
                elif x1 == 0:
                    x1 = conector_cercano.x
                    y1 = conector_cercano.y
                    conector1 = conector_cercano  # Guarda el primer conector
                else:
                    x2 = conector_cercano.x
                    y2 = conector_cercano.y
                    conector2 = conector_cercano  # Guarda el segundo conector
                    # Verifica si los conectores están dentro del rango adecuado
                    if (((x1 + 40) >= x2) or ((x1 - 40) <= x2) or ((x1 + 20) <= x2) or ((x1 - 20) <= x2)) and \
                            (((y1 + 40) <= y2) or ((y1 - 40) >= y2) or ((y1 + 20) <= y2) or ((y1 - 20) <= y2)) and \
                            (x1 - x2) <= 40 and (x2 - x1) <= 40 and (y2 - y1) <= 40 and (y1 - y2) <= 40:

                        tupla1 = (x1,y1)
                        tupla2 = (x2, y2)
                        led_coordenadas.append(tupla1)
                        led_coordenadas.append(tupla2)
                        x_mitad, y_mitad = ((x1 + x2) / 2, (y1 + y2) / 2)
                        c_apagada = (110, 0, 0)  # Color rojo oscuro para apagado
                        led_a = Led(c_apagada, x_mitad, y_mitad, x1, x2, y1, y2)
                        # Dibujar el LED
                        led_a.led_apagada(screen)

                        # Restablecer variables
                        x1, x2, y1, y2 = 0, 0, 0, 0
                        boton_led = False
                        guardar_led.append(led_a)
                    
            elif boton_switch:
                if not conector_cercano:
                    pass
                elif x1 == 0:
                    x1 = conector_cercano.x
                    y1 = conector_cercano.y
                else:
                    x2 = conector_cercano.x
                    y2 = conector_cercano.y

                    tupla1 = (x1,y1)
                    tupla2 = (x2, y2)
                    switch_coordenadas.append(tupla1)
                    switch_coordenadas.append(tupla2)
                    if (((x1 + 40) >= x2) or ((x1 - 40) <= x2) or ((x1 + 20) <= x2) or ((x1 - 20) <= x2)) and (((y1 + 40) <= y2) or ((y1 - 40) >= y2) or ((y1 + 20) <= y2) or ((y1 - 20) <= y2)) and (x1 - x2) <= 40 and (x2 - x1) <= 40 and (y2 - y1) <= 40 and (y1 - y2) <= 40:
                        x_mitad, y_mitad = (((x1 + x2) / 2) - 10, ((y1 + y2) / 2) - 10)
                        switch_a = Switch(x_mitad, y_mitad, x1, x2, y1, y2)
                        switch_a.switch_proto(screen)
                        x1, x2, y1, y2 = 0, 0, 0, 0
                        boton_switch = False
                        guardar_switch.append(switch_a)

            elif conector_cercano and boton_led == False and boton_switch == False and boton_cable and boton_edicion == False and boton_basurero == False:
                for conector in conectores:
                    if conector_cercano == conector:
                        if not cableado.dibujando_cable:
                            cableado.comienzo_cable(conector)
                        else:
                            cableado.finalizar_cable(conector)
                            ultimo_conector = conector_cercano
                 
            elif boton_edicion:
                i = 0
                validador = False
                rango_click = 10
                mouse_pos = pygame.mouse.get_pos()
                conector_cercano = punto_mas_cercano(mouse_pos, conectores, distancia_maxima) #obtencion de punto cercano
                if conector_cercano == None:
                    pass
                else:
                    edicion_coordenadas.append(conector_cercano)
                    #print("Origen: ",cables[0][0].x,cables[0][0].y)
                    #print("Destino: ",cables[0][1].x,cables[0][1].y)
                    #print("Edición: ",edicion_coordenadas[len(edicion_coordenadas) - 1].x,edicion_coordenadas[len(edicion_coordenadas) - 1].y)

                for cable in cables:
                    if cable[0].x - rango_click <= x <= cable[0].x + rango_click and cable[0].y - rango_click <= y <= cable[0].y + rango_click:
                        print("entró en el origen del cable")
                        start = cable[1]
                        end = cable[0]
                        for i in range(len(cables)):
                            if cable[0] == cables[i][0]:
                                cables.pop(i)                           #Elimina el cable simulando edición
                                indice = len(edicion_coordenadas) - 2   #Indicar indice de la lista "edicion_coordenadas"
                                nuevo = (edicion_coordenadas[indice])   #Obtener coordenadas de tipo conector
                                cables.insert(i,(nuevo,cable[1]))       #Inserta directamente un nuevo cable simulando edición

                        if start and end:
                            end.eliminar_conexion(start, end)
                            if end.nombre.startswith(("conector1_", "conector2_")):
                                 for nodo in conectores:
                                    if nodo.y == end.y:
                                        nodo.eliminar_conexion(nodo, start)
                            # -------------------- elimina columnas ------------------------
                            else:
                                #print("--------------------------------")
                                cont=0
                                for nodo in conectores:
                                    if nodo.x == end.x:
                                        if end.nombre.startswith("conector3_"):
                                            #print(nodo.nombre,"\t",cont)
                                            cont+=1
                                            nodo.eliminar_conexion(nodo, start)
                                        elif end.nombre.startswith("conector4_"):
                                            nodo.eliminar_conexion(nodo, start) 
                            # ------------------------ Agregar corriente en destino ------------------------
                            if start.nombre in ["pila+", "pila-"]:          # Coordenadas de inicio / coordenadas de destino ( tipo conector)
                                for nodo in conectores:
                                    if nodo.y == nuevo.y:  # ver si estan en la misma fila
                                        start.agregar_conexion(nodo)
                            else:
                                for nodo in conectores:
                                    if nodo.x == nuevo.x:  # ver si estan en la misma columna | se limita el alcance
                                        if nuevo.nombre.startswith("conector3_"):
                                            if nodo.nombre.startswith("conector3_") and nodo.nombre!=start.nombre:
                                                start.agregar_conexion(nodo)

                                        elif nuevo.nombre.startswith("conector4_"):
                                            if nodo.nombre.startswith("conector4_"):
                                                if nodo.nombre.startswith("conector4_") and nodo.nombre != start.nombre:
                                                    start.agregar_conexion(nodo)                                               
                        edicion_coordenadas.clear() #limpieza de lista
                        validador = True
                        boton_edicion = False
                       
                    elif cable[1].x - rango_click <= x <= cable[1].x + rango_click and cable[1].y - rango_click <= y <= cable[1].y + rango_click: 
                        print("Entró en el destino del cable")
                        start = cable[1]
                        end = cable[0]
                        for i in range(len(cables)):
                            if cable[1] == cables[i][1]:
                                cables.pop(i)                           #Elimina el cable simulando edición
                                indice = len(edicion_coordenadas) - 2   #Indicar indice de la lista "edicion_coordenadas"
                                nuevo = (edicion_coordenadas[indice])   #Obtener coordenadas de tipo conector
                                cables.insert(i,(cable[0],nuevo))       #Inserta directamente un nuevo cable simulando edición
                                break


                        if start and end:
                            start.eliminar_conexion(start, end)
                            if start.nombre.startswith(("conector1_", "conector2_")):
                                for nodo in conectores:
                                    if nodo.y == start.y:
                                        nodo.eliminar_conexion(nodo, end)
                            # -------------------- elimina columnas ------------------------
                            else:
                                #print("--------------------------------")
                                cont=0
                                for nodo in conectores:
                                    if nodo.x == start.x:
                                        if start.nombre.startswith("conector3_"):
                                            #print(nodo.nombre,"\t",cont)
                                            cont+=1
                                            nodo.eliminar_conexion(nodo, end)

                                        elif start.nombre.startswith("conector4_"):
                                            nodo.eliminar_conexion(nodo, end)
                            
                            # ------------------------ Agregar corriente en destino ------------------------
                            if end.nombre in ["pila+", "pila-"]:          # Coordenadas de inicio / coordenadas de destino ( tipo conector)
                                for nodo in conectores:
                                    if nodo.y == nuevo.y:  # ver si estan en la misma fila
                                        end.agregar_conexion(nodo)
                            else:
                                for nodo in conectores:
                                    if nodo.x == nuevo.x:  # ver si estan en la misma columna | se limita el alcance
                                        if nuevo.nombre.startswith("conector3_"):
                                            if nodo.nombre.startswith("conector3_") and nodo.nombre!=end.nombre:
                                                end.agregar_conexion(nodo)

                                        elif nuevo.nombre.startswith("conector4_"):
                                            if nodo.nombre.startswith("conector4_"):
                                                if nodo.nombre.startswith("conector4_") and nodo.nombre != end.nombre:
                                                    end.agregar_conexion(nodo)                                                     
                        edicion_coordenadas.clear() #limpieza de lista
                        validador = True
                        boton_edicion = False
                    
                while i < len(led_coordenadas) and validador == False:
                    if led_coordenadas[i][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and led_coordenadas[i][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y: 
                        print("entró en el origen del LED")
                        x = edicion_coordenadas[len(edicion_coordenadas) - 2].x #coordenada x que el usuario escogio para cambiar
                        y = edicion_coordenadas[len(edicion_coordenadas) - 2].y #coordenada y que el usuario escogio para cambiar
                        x_origen = led_coordenadas[i][0]
                        y_origen = led_coordenadas[i][1]
                        x_destino = led_coordenadas[i+1][0]
                        y_destino = led_coordenadas[i+1][1]

                        if i % 2 == 0:
                            pos = i // 2
                        else:
                            pos = (i - 1) // 2

                        if (((x + 40) >= x_destino) or ((x - 40) <= x_destino) or ((x + 20) <= x_destino) or ((x - 20) <= x_destino)) and \
                            (((y + 40) <= y_destino) or ((y - 40) >= y_destino) or ((y + 20) <= y_destino) or ((y - 20) <= y_destino)) and \
                            (x - x_destino) <= 40 and (x_destino - x) <= 40 and (y_destino - y) <= 40 and (y - y_destino) <= 40:
                            guardar_led.remove(guardar_led[pos]) # Eliminar la led para posteriormente actualizar su posicion
                            x_mitad, y_mitad = ((x + x_destino) / 2, (y_destino + y) / 2)
                            c_encendida = (250, 0, 0)  # Color rojo para encendido
                            c_apagada = (110, 0, 0)  # Color rojo oscuro para apagado
                               
                            # Verificar si conector1 tiene corriente
                            corriente_conector1 = False
                            if conector1.fase or conector1.neutro:
                                corriente_conector1 = True

                            # Verificar si conector2 tiene corriente
                            corriente_conector2 = False
                            if conector2.fase or conector2.neutro:
                                corriente_conector2 = True

                            if conector2.fase and conector1.fase:
                                corriente_conector1 = True
                                corriente_conector2 = False

                            if conector2.neutro and conector1.neutro:
                                corriente_conector1 = True
                                corriente_conector2 = False

                            # Cambiar color del LED según si ambos conectores tienen corriente
                            if corriente_conector1 and corriente_conector2:
                                led_a = Led(c_encendida, x_mitad, y_mitad, x, x_destino, y, y_destino)
                            else:
                                led_a = Led(c_apagada, x_mitad, y_mitad, x, x_destino, y, y_destino)
                            led_a.led_apagada(screen) # Dibujar el LED
                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0 # Restablecer variables
                            edicion_coordenadas.clear() # Limpieza de lista edicion coordenadas
                            guardar_led.insert(i, led_a) # Insertar directamente el LED en la posición original
                            led_coordenadas[i] = x,y
                            boton_edicion = False 
                            validador = True
                            break

                    elif led_coordenadas[i+1][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and led_coordenadas[i+1][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y: 
                        print("Entró en el destino del LED")
                        x = edicion_coordenadas[len(edicion_coordenadas) - 2].x #coordenada x que el usuario escogio para cambiar
                        y = edicion_coordenadas[len(edicion_coordenadas) - 2].y #coordenada y que el usuario escogio para cambiar
                        x_origen = led_coordenadas[i][0]    #Obtengo coordenada x de origen
                        y_origen = led_coordenadas[i][1]    #Obtengo coordenada y de origen
                        x_destino = led_coordenadas[i+1][0] #Obtengo coordenada x de destino
                        y_destino = led_coordenadas[i+1][1] #Obtengo coordenada y de destino

                        if i % 2 == 0:
                            pos = i // 2
                        else:
                            pos = (i - 1) // 2
                        if (((x_origen + 40) >= x) or ((x_origen - 40) <= x) or ((x_origen + 20) <= x) or ((x_origen - 20) <= x)) and \
                            (((y_origen + 40) <= y) or ((y_origen - 40) >= y) or ((y_origen + 20) <= y) or ((y_origen - 20) <= y)) and \
                            (x_origen - x) <= 40 and (x_destino - x) <= 40 and (y - y_origen) <= 40 and (y_origen - y) <= 40:
                            guardar_led.remove(guardar_led[pos]) # Eliminar la led para posteriormente actualizar su posicion
                            x_mitad, y_mitad = ((x_origen + x) / 2, (y_origen + y) / 2)
                            c_encendida = (250, 0, 0)  # Color rojo para encendido
                            c_apagada = (110, 0, 0)  # Color rojo oscuro para apagado
                                
                            # Verificar si conector1 tiene corriente
                            corriente_conector1 = False
                            if conector1.fase or conector1.neutro:
                                corriente_conector1 = True

                            # Verificar si conector2 tiene corriente
                            corriente_conector2 = False
                            if conector2.fase or conector2.neutro:
                                corriente_conector2 = True

                            if conector2.fase and conector1.fase:
                                corriente_conector1 = True
                                corriente_conector2 = False

                            if conector2.neutro and conector1.neutro:
                                corriente_conector1 = True
                                corriente_conector2 = False

                            # Cambiar color del LED según si ambos conectores tienen corriente
                            if corriente_conector1 and corriente_conector2:
                                led_a = Led(c_encendida, x_mitad, y_mitad, x_origen, x, y_origen, y)
                            else:
                                led_a = Led(c_apagada, x_mitad, y_mitad, x_origen, x, y_origen, y)

                            # Dibujar el LED
                            led_a.led_apagada(screen)
                            # Restablecer variables
                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0
                            edicion_coordenadas.clear()
                            guardar_led.insert(i, led_a) # Inserta directamente en la posicion correspondiente las nuevas coordenadas
                            led_coordenadas[i+1] = x,y # Actualiza las coordenadas en la lista de las posiciones de cada led
                            boton_edicion = False
                            validador = True
                            break
                    i+=2
                i = 0
                while i < len(switch_coordenadas) and validador == False:
                    if switch_coordenadas[i][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and switch_coordenadas[i][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y:
                        print("Entró en el origen del switch")
                        x = edicion_coordenadas[len(edicion_coordenadas) - 2].x #coordenada x que el usuario escogio para cambiar
                        y = edicion_coordenadas[len(edicion_coordenadas) - 2].y #coordenada y que el usuario escogio para cambiar
                        x_origen = switch_coordenadas[i][0] #Obtengo coordenada x de origen
                        y_origen = switch_coordenadas[i][1] #Obtengo coordenada y de origen
                        x_destino = switch_coordenadas[i+1][0]  #Obtengo coordenada x de destino
                        y_destino = switch_coordenadas[i+1][1]  #Obtengo coordenada y de destino

                        if i % 2 == 0:
                            pos = i // 2
                        else:
                            pos = (i - 1) // 2

                        if (((x + 40) >= x_destino) or ((x - 40) <= x_destino) or ((x + 20) <= x_destino) or ((x - 20) <= x_destino)) and \
                            (((y + 40) <= y_destino) or ((y - 40) >= y_destino) or ((y + 20) <= y_destino) or ((y - 20) <= y_destino)) and \
                            (x - x_destino) <= 40 and (x_destino - x) <= 40 and (y_destino - y) <= 40 and (y - y_destino) <= 40:

                            guardar_switch.remove(guardar_switch[pos]) # Eliminar el swich para posteriormente actualizar su posicion
                            x_mitad, y_mitad = (((x + x_destino) / 2) - 10, ((y + y_destino) / 2) - 10)
                            switch_a = Switch(x_mitad, y_mitad, x, x_destino, y, y_destino) # Dibujar el switch
                            switch_a.switch_proto(screen)

                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0
                            edicion_coordenadas.clear() # Limpieza de lista edicion coordenadas
                            guardar_switch.insert(i, switch_a) # Insertar directamente el switch en la posición original
                            switch_coordenadas[i] = (x,y) # Actualiza las coordenadas en la lista de las posiciones de cada switch
                            boton_edicion = False 
                            validador = True
                            break

                    elif switch_coordenadas[i+1][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and switch_coordenadas[i+1][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y:   
                        print("Entró en el destino del switch")
                        x = edicion_coordenadas[len(edicion_coordenadas) - 2].x #coordenada x que el usuario escogio para cambiar
                        y = edicion_coordenadas[len(edicion_coordenadas) - 2].y #coordenada y que el usuario escogio para cambiar
                        x_origen = switch_coordenadas[i][0]
                        y_origen = switch_coordenadas[i][1]
                        x_destino = switch_coordenadas[i+1][0]
                        y_destino = switch_coordenadas[i+1][1]
                            
                        if i % 2 == 0:
                            pos = i // 2
                        else:
                            pos = (i - 1) // 2
                        if (((x_origen + 40) >= x) or ((x_origen - 40) <= x) or ((x_origen + 20) <= x) or ((x_origen - 20) <= x)) and \
                            (((y_origen + 40) <= y) or ((y_origen - 40) >= y) or ((y_origen + 20) <= y) or ((y_origen - 20) <= y)) and \
                            (x_origen - x) <= 40 and (x_destino - x) <= 40 and (y - y_origen) <= 40 and (y_origen - y) <= 40:
                                
                            guardar_switch.remove(guardar_switch[pos]) # Eliminar la led para posteriormente actualizar su posicion
                            x_mitad, y_mitad = (((x_origen + x) / 2) - 10, ((y_origen + y) / 2) - 10)
                            switch_a = Switch(x_mitad, y_mitad, x_origen, x, y_origen, y) # Dibujar el switch
                            switch_a.switch_proto(screen)

                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0
                            edicion_coordenadas.clear() # Limpieza de lista edicion coordenadas
                            guardar_switch.insert(i, switch_a) # Insertar directamente el switch en la posición original
                            switch_coordenadas[i+1] = (x,y) # Actualiza las coordenadas en la lista de las posiciones de cada switch
                            boton_edicion = False 
                            validador = True
                            break
                    i+=2

        #Manejo de evento del menú
        menu.manejar_eventos(event)
    cableado.dibujar_cable_actual()

    # Opcion de menú escogida según usuario
    if boton_cable:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 20,y_menu + 15)
        menu.dib_cable(screen, x_menu + 95, y_menu - 15)    
    
    elif boton_led:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 145,y_menu + 15)
        menu.dib_led(screen, x_menu + 170, y_menu + 35)
                
    elif boton_switch:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 270,y_menu + 15)
        menu.dib_switch(screen, x_menu + 300, y_menu + 40)     
        
    elif boton_edicion:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 395,y_menu + 15)         
        menu.dib_editor(screen, x_menu + 420, y_menu + 25)

    elif boton_basurero:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 520,y_menu + 15)     
        menu.dib_basurero(screen, x_menu + 535, y_menu + 30)



    for c in conectores: # busca las pilas y las envia a cambiar o no estado fase / neutro
        if c.nombre == "pila+":
            if not c.conexiones:
                c.padre =c
            cableado.energy_protoboard(c)
            #print("+",c.padre.nombre)
        if c.nombre == "pila-":
            if not c.conexiones:
                c.padre =c
            cableado.energy_protoboard(c)
            #print("-",c.padre.nombre)

    def dibujar_conectores(screen, conectores): # le da color a los puntos segun el tipo de energy
        for conector in conectores:
            if not conector.nombre.startswith("pila"):
                if conector.fase:
                    pygame.draw.line(screen, "red", (conector.x, conector.y), (conector.x + conector.largo, conector.y),
                                     6)
                elif conector.neutro:
                    pygame.draw.line(screen, "blue", (conector.x, conector.y), (conector.x + conector.largo, conector.y),
                                     6)

    dibujar_conectores(screen, conectores)
    pygame.display.flip()
    CONECTORES_SIZE = 0  # evita exceso conectores
    mainClock.tick(30)

pygame.quit()
"""print("\n|------------- INFO -------------|\n")
aux=0
for c in conectores:
    if c.nombre != c.padre.nombre:
        print(f"{aux}) N {c.nombre} P {c.padre.nombre}")
        aux+=1

print("\n|------------- TEND -------------|\n")"""

"""#print("Conexiones restantes:")
for nodo in conectores:
    conexiones = [n.nombre for n in nodo.conexiones]
    if conexiones:
        print(f"Nodo {nodo.nombre} está conectado con: {conexiones}")"""

"""for nodo in conectores:
    if nodo.padre != nodo:
        print ("Nodo",nodo.nombre," padre",nodo.padre.nombre)"""