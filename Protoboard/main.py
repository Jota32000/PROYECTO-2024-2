import pygame
from pygame.locals import *
from Resistencia import Resistencia
from Switch import Switch
from Protoboard import Protoboard
from Cableado import Cableado
from Basurero import Basurero
from Pila import Pila
from Menu import Menu
from Led import Led
import math
from Datos import *

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

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)  # conexion bidireccional A->B | B->A
        nodo.conexiones.append(self)
        cableado.actualizarbosque(self, nodo)

    def eliminar_conexion(self, nodo, nodo_objetivo):
        if nodo_objetivo in self.conexiones:  # ve que no se haya eliminado ya la conexion con ese nodo
            nodo.conexiones.remove(nodo_objetivo)
            nodo_objetivo.conexiones.remove(nodo)
            cableado.buscar_conexiones(nodo, nodo_objetivo)
conectores = []
boton_cable = False  # Estado del boton del cable (activado = true o desactivado = false)
boton_led = False  # Estado del boton de la led (activado = true o desactivado = false)
boton_switch = False  # Estado del boton del switch (activado = true o desactivado = false)
boton_edicion = False  # Estado del boton de edición (activado = true o desactivado = false)
boton_basurero = False  # Estado del boton del basurero (activado=true o desactivado = false)
boton_switch16=False
boton_switch4=False
global verificador
verificador = False  # Estado de verificador a la hora de eliminar un elemento
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
        pygame.draw.line(screen, ("black"), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho),
                         3)
        # Línea inferior
        pygame.draw.line(screen, ("black"), (self.x, self.y + self.ancho), (self.x + self.largo, self.y + self.ancho),
                         3)

        for i in range(self.ancho):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))

        alto = 10
        pygame.draw.line(screen, (17, 17, 222), (self.x + alto, self.y + alto),
                         (self.x + self.largo - 10, self.y + alto), 1)
        pygame.draw.line(screen, (222, 17, 17), (self.x + alto, self.y + 53), (self.x + self.largo - 10, self.y + 53),
                         1)
        pygame.draw.line(screen, (222, 17, 17), (self.x + alto, self.y + self.ancho - 10),
                         (self.x + self.largo - 10, self.y + self.ancho - 10), 1)
        pygame.draw.line(screen, (17, 17, 222), (self.x + alto, self.y + self.ancho - 53),
                         (self.x + self.largo - 10, self.y + self.ancho - 53), 1)

        # crear CANAL Central
        mitad_largo = self.ancho // 2
        pygame.draw.line(screen, (207, 207, 207), (self.x, self.y + mitad_largo),
                         (self.x + self.largo, self.y + mitad_largo), 30)

        # Llamar al metodo para dibujar conectores

        self.dibujar_conectores(screen)

    def dibujar_conectores(self, screen):
        # Espaciado entre conectores
        separacion_x = 20
        # Coordenadas iniciales para conectores
        inicio_x = self.x + 35
        inicio_y = self.y + 20
        # Número de filas y columnas de conectores
        num_filas = 5
        num_columnas = 30

        dibujar_1(screen, inicio_x - 3, inicio_y + 45, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 77, inicio_y + 45, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x + 175, inicio_y + 55, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 175, inicio_y + 40, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x + 275, inicio_y + 55, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 275, inicio_y + 40, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x + 375, inicio_y + 55, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 375, inicio_y + 40, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x + 475, inicio_y + 55, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 475, inicio_y + 40, 10, (84, 84, 84))
        dibujar_3(screen, inicio_x + 575, inicio_y + 55, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 575, inicio_y + 40, 10, (84, 84, 84))

        dibujar_1(screen, inicio_x - 3, inicio_y + self.ancho - 95, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 77, inicio_y + self.ancho - 95, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x + 175, inicio_y + self.ancho - 85, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 175, inicio_y + self.ancho - 100, 10, (84, 84, 84))
        dibujar_1(screen, inicio_x + 275, inicio_y + self.ancho - 85, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 275, inicio_y + self.ancho - 100, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x + 375, inicio_y + self.ancho - 85, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 375, inicio_y + self.ancho - 100, 10, (84, 84, 84))
        dibujar_2(screen, inicio_x + 475, inicio_y + self.ancho - 85, 10, (84, 84, 84))
        dibujar_5(screen, inicio_x + 475, inicio_y + self.ancho - 100, 10, (84, 84, 84))
        dibujar_3(screen, inicio_x + 575, inicio_y + self.ancho - 85, 10, (84, 84, 84))
        dibujar_0(screen, inicio_x + 575, inicio_y + self.ancho - 100, 10, (84, 84, 84))

        dibujar_mas(screen, inicio_x - 20, inicio_y + 357, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x - 20, inicio_y + 337, (17, 17, 222))
        dibujar_a(screen, inicio_x - 20, inicio_y + 285, 10, 10, (84, 84, 84))
        dibujar_b(screen, inicio_x - 20, inicio_y + 265, 10, (84, 84, 84))
        dibujar_c(screen, inicio_x - 20, inicio_y + 245, 10, 10, (84, 84, 84))
        dibujar_d(screen, inicio_x - 20, inicio_y + 225, 10, 10, (84, 84, 84))
        dibujar_e(screen, inicio_x - 20, inicio_y + 205, 10, 10, (84, 84, 84))
        dibujar_f(screen, inicio_x - 20, inicio_y + 145, 10, 10, (84, 84, 84))
        dibujar_g(screen, inicio_x - 20, inicio_y + 125, 10, 10, (84, 84, 84))
        dibujar_h(screen, inicio_x - 20, inicio_y + 105, 10, 10, (84, 84, 84))
        dibujar_i(screen, inicio_x - 20, inicio_y + 85, 10, 10, (84, 84, 84))
        dibujar_j(screen, inicio_x - 20, inicio_y + 65, 10, 10, (84, 84, 84))
        dibujar_mas(screen, inicio_x - 20, inicio_y + 20, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x - 20, inicio_y + 2, (17, 17, 222))

        dibujar_mas(screen, inicio_x + self.largo - 55, inicio_y + 357, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x + self.largo - 55, inicio_y + 337, (17, 17, 222))
        dibujar_a(screen, inicio_x + self.largo - 55, inicio_y + 285, 10, 10, (84, 84, 84))
        dibujar_b(screen, inicio_x + self.largo - 55, inicio_y + 265, 10, (84, 84, 84))
        dibujar_c(screen, inicio_x + self.largo - 55, inicio_y + 245, 10, 10, (84, 84, 84))
        dibujar_d(screen, inicio_x + self.largo - 55, inicio_y + 225, 10, 10, (84, 84, 84))
        dibujar_e(screen, inicio_x + self.largo - 55, inicio_y + 205, 10, 10, (84, 84, 84))
        dibujar_f(screen, inicio_x + self.largo - 55, inicio_y + 145, 10, 10, (84, 84, 84))
        dibujar_g(screen, inicio_x + self.largo - 55, inicio_y + 125, 10, 10, (84, 84, 84))
        dibujar_h(screen, inicio_x + self.largo - 55, inicio_y + 105, 10, 10, (84, 84, 84))
        dibujar_i(screen, inicio_x + self.largo - 55, inicio_y + 85, 10, 10, (84, 84, 84))
        dibujar_j(screen, inicio_x + self.largo - 55, inicio_y + 65, 10, 10, (84, 84, 84))
        dibujar_mas(screen, inicio_x + self.largo - 55, inicio_y + 20, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x + self.largo - 55, inicio_y + 2, (17, 17, 222))
        for i in range(2):
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                nombre_c1 = f"conector1_{i}_{j}"
                # se crea un conector y se verifica si ya existe
                conector_existente = None
                for conector in conectores:
                    if conector.nombre == nombre_c1:
                        conector_existente = conector  # la bandera ahora tiene conector
                        break
                # si existe solo se cambian las coordenadas
                if conector_existente:
                    conector_existente.x = x_pos
                    conector_existente.y = y_pos
                # si no existe se crea un nuevo conector y se agrega a la lista
                else:
                    conector = Conector(nombre_c1, x_pos, y_pos)
                    conectores.append(conector)
                conector.dibujar(screen)
        for i in range(2):
            for j in range(num_columnas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                nombre_c2 = f"conector2_{i}_{j}"
                conector_existente = None
                for conector in conectores:
                    if conector.nombre == nombre_c2:
                        conector_existente = conector
                        break

                if conector_existente:
                    conector_existente.x = x_pos
                    conector_existente.y = y_pos + self.ancho - 64
                else:
                    conector = Conector(nombre_c2, x_pos, y_pos + self.ancho - 64)
                    conectores.append(conector)
                conector.dibujar(screen)
        for j in range(num_columnas):
            primer_conector_columna = None  # guarda el primer nodo de cada columna
            for i in range(num_filas):
                y_pos = inicio_y + i * 20
                x_pos = inicio_x + j * separacion_x
                nombre_c3 = f"conector3_{i}_{j}"

                conector_existente = None
                for conector in conectores:
                    if conector.nombre == nombre_c3:
                        conector_existente = conector
                        break

                if conector_existente:
                    conector_existente.x = x_pos
                    conector_existente.y = y_pos + 70
                    conector = conector_existente
                else:
                    conector = Conector(nombre_c3, x_pos, y_pos + 70)
                    conectores.append(conector)

                conector.dibujar(screen)
                # asigna el primer conector de la columna
                if i == 0:
                    primer_conector_columna = conector
                else:
                    # verifica si la conexion ya existe y evita code duplicado
                    if conector not in primer_conector_columna.conexiones:
                        primer_conector_columna.agregar_conexion(conector)  # si no la agrega

        # solo repito el proceso
        for j in range(num_columnas):
            primer_conector_columna = None
            for i in range(num_filas):
                x_pos = inicio_x + j * separacion_x
                y_pos = inicio_y + i * 20
                nombre_c4 = f"conector4_{i}_{j}"

                conector_existente = None
                for conector in conectores:
                    if conector.nombre == nombre_c4:
                        conector_existente = conector
                        break

                if conector_existente:
                    conector_existente.x = x_pos
                    conector_existente.y = y_pos + 210
                    conector = conector_existente
                else:
                    conector = Conector(nombre_c4, x_pos, y_pos + 210)
                    conectores.append(conector)
                conector.dibujar(screen)
                if i == 0:
                    primer_conector_columna = conector
                else:
                    if conector not in primer_conector_columna.conexiones:
                        primer_conector_columna.agregar_conexion(conector)
class Pila:
    def __init__(self, pila_x, pila_y):
        self.pila_x = pila_x
        self.pila_y = pila_y
        self.color_cabeza_pila = (240, 134, 21)
        self.color_cuerpo_pila = (0, 0, 0)
        self.color_componentes_pila = (170, 170, 170)
        self.largo = 750
        self.ancho = 550

        conector_existente_pila1 = None
        for conector in conectores:
            if conector.nombre == "pila+":
                conector_existente_pila1 = conector
                break

        if conector_existente_pila1:
            conector_existente_pila1.x = self.pila_x + 65
            conector_existente_pila1.y = self.pila_y - 15
        else:
            conector_pila1 = Conector("pila+", self.pila_x + 65, self.pila_y - 15)
            conectores.append(conector_pila1)

        conector_existente_pila2 = None
        for conector in conectores:
            if conector.nombre == "pila-":
                conector_existente_pila2 = conector
                break

        if conector_existente_pila2:
            conector_existente_pila2.x = self.pila_x + 35
            conector_existente_pila2.y = self.pila_y - 15
        else:
            conector_pila2 = Conector("pila-", self.pila_x + 35, self.pila_y - 15)
            conectores.append(conector_pila2)

            conector_pila1.fase = True
            conector_pila2.neutro = True
    def dibujarPila(self, screen):
        # Dibujo parte superior pila
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y + 30), (self.pila_x, self.pila_y),
                         3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y + 30),
                         (self.pila_x + 100, self.pila_y + 30), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x + 100, self.pila_y + 30),
                         (self.pila_x + 100, self.pila_y), 3)
        pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y), (self.pila_x + 100, self.pila_y),
                         3)
        # Ciclo que permite rellenar la pila
        for i in range(100):
            pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x, self.pila_y),
                             (self.pila_x + i, self.pila_y + 30), 3)
            pygame.draw.line(screen, (self.color_cabeza_pila), (self.pila_x + 100, self.pila_y + 30),
                             (self.pila_x + 100 - i, self.pila_y), 3)
        # Dibujo parte inferior pila
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 100, self.pila_y + 30),
                         (self.pila_x + 100, self.pila_y + 120), 3)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 100, self.pila_y + 120),
                         (self.pila_x, self.pila_y + 120), 3)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x, self.pila_y + 120),
                         (self.pila_x, self.pila_y + 30), 3)
        # Ciclo que permite rellenar la parte interior de la pila
        for i in range(100):
            pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x, self.pila_y + 30),
                             (self.pila_x + i, self.pila_y + 120))
            pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 100, self.pila_y + 120),
                             (self.pila_x + 100 - i, self.pila_y + 30))
        # Componente negativo (-)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 30, self.pila_y - 2),
                         (self.pila_x + 30, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 30, self.pila_y - 16),
                         (self.pila_x + 40, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 40, self.pila_y - 16),
                         (self.pila_x + 40, self.pila_y - 2), 3)
        # Componente Positivo (+)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 2),
                         (self.pila_x + 60, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 16),
                         (self.pila_x + 60, self.pila_y - 16), 3)
        pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 70, self.pila_y - 2),
                         (self.pila_x + 70, self.pila_y - 16), 3)
        # Ciclo para rellenar componente 1
        for i in range(10):
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 60, self.pila_y - 16),
                             (self.pila_x + 60 + i, self.pila_y - 2), 3)
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 70, self.pila_y - 2),
                             (self.pila_x + 70 - i, self.pila_y - 16), 3)

        # Ciclo para rellenar componente 2
        for i in range(10):
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 30, self.pila_y - 16),
                             (self.pila_x + 30 + i, self.pila_y - 2), 3)
            pygame.draw.line(screen, (self.color_componentes_pila), (self.pila_x + 40, self.pila_y - 2),
                             (self.pila_x + 40 - i, self.pila_y - 16), 3)
        # Negativo
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 40, self.pila_y + 15),
                         (self.pila_x + 30, self.pila_y + 15), 2)
        # Positivo
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 70, self.pila_y + 15),
                         (self.pila_x + 60, self.pila_y + 15), 2)
        pygame.draw.line(screen, (self.color_cuerpo_pila), (self.pila_x + 65, self.pila_y + 10),
                         (self.pila_x + 65, self.pila_y + 20), 2)
class Menu_f:
    def __init__(self):
        self.x = 0
        self.y = 50
        self.color_pulsar = (187, 143, 206)
        self.color_cursor = (143, 162, 206)
        self.color = (162, 206, 143)
        self.color_cable = (162, 206, 143)
        self.color_led = (162, 206, 143)
        self.color_switch = (162, 206, 143)
        self.color_res = (162, 206, 143)
        self.color_ship = (162, 206, 143)
        self.color_motor = (162, 206, 143)
        self.color_proto = (162, 206, 143)
        self.color_editar = (162, 206, 143)
        self.color_borrar = (162, 206, 143)
        self.ancho_boton = 0  # Atributo para almacenar el ancho
        self.font = pygame.font.Font(None, 22)
        self.cable_pulsado = False
        self.led_pulsado = False
        self.switch_pulsado = False
        self.res_pulsado = False
        self.ship_pulsado = False
        self.motor_pulsado = False
        self.proto_pulsado = False
        self.editar_pulsado = False
        self.borrar_pulsado = False
        self.switch_4_pulsado =False
        self.switch_16_pulsado =False
    def div_boton(self, screen, x, y, color):
        self.ancho = self.ancho_boton
        self.alto = 60
        pygame.draw.line(screen, color, (x, y), (x + self.ancho, y), 3)
        pygame.draw.line(screen, color, (x + self.ancho, y), (x + self.ancho, y + self.alto), 3)
        pygame.draw.line(screen, color, (x + self.ancho, y + self.alto), (x, y + self.alto), 3)
        pygame.draw.line(screen, color, (x, y), (x, y + self.alto), 3)

        # Rellenar el área del botón usando líneas horizontales
        for i in range(y, y + self.alto):  # Recorre de arriba hacia abajo (en el eje y)
            pygame.draw.line(screen, color, (x, i),
                             (x + self.ancho, i))  # Dibuja una línea horizontal desde el borde izquierdo al derecho
    def dibujar(self, screen):
        ancho_pantalla, alto_pantalla = screen.get_size()

        # Calcular el ancho de la primera división
        numero_divisiones = 9
        self.ancho_boton = ancho_pantalla // numero_divisiones

        # Dibujar una línea horizontal que se ajuste a la pantalla
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (ancho_pantalla, self.y), 3)
        pygame.draw.line(screen, (0, 0, 0), (self.x, 10), (ancho_pantalla, 10), 3)

        # Dividir la línea horizontal en 9 partes
        separacion_vertical = ancho_pantalla // numero_divisiones

        # Lista de textos para cada división
        textos = ["CABLE", "LED", "SWITCH", "RESISTENCIA", "SHIP", "MOTOR", "PROTOBOARD", "EDITAR", "BORRAR"]

        # Crear superficie para el botón
        boton_cable_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón CABLE
        boton_cable_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_led_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón LED
        boton_led_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_switch_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón Switch
        boton_switch_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_resistencia_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón resistencia
        boton_resistencia_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_ship_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón ship
        boton_ship_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_motor_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón motor
        boton_motor_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_proto_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón protoboart
        boton_proto_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_edicion_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón edición
        boton_edicion_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_basurero_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Boton basurero
        boton_basurero_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        x_inic = 0
        # Dibujar el botón en la superficie del botón
        self.div_boton(boton_cable_surface, x_inic, 3, self.color_cable)
        self.div_boton(boton_led_surface, 0, 3, self.color_led)
        self.div_boton(boton_switch_surface, 0, 3, self.color_switch)
        self.div_boton(boton_resistencia_surface, 0, 3, self.color_res)
        self.div_boton(boton_ship_surface, 0, 3, self.color_ship)
        self.div_boton(boton_motor_surface, 0, 3, self.color_motor)
        self.div_boton(boton_proto_surface, 0, 3, self.color_proto)
        self.div_boton(boton_edicion_surface, 0, 3, self.color_editar)
        self.div_boton(boton_basurero_surface, 0, 3, self.color_borrar)

        # Blitear la superficie del botón
        screen.blit(boton_cable_surface, (0, 10))
        screen.blit(boton_led_surface, (x_inic + self.ancho_boton, 10))
        screen.blit(boton_switch_surface, (x_inic + (self.ancho_boton * 2), 10))
        screen.blit(boton_resistencia_surface, (x_inic + (self.ancho_boton * 3), 10))
        screen.blit(boton_ship_surface, (x_inic + (self.ancho_boton * 4), 10))
        screen.blit(boton_motor_surface, (x_inic + (self.ancho_boton * 5), 10))
        screen.blit(boton_proto_surface, (x_inic + (self.ancho_boton * 6), 10))
        screen.blit(boton_edicion_surface, (x_inic + (self.ancho_boton * 7), 10))
        screen.blit(boton_basurero_surface, (x_inic + (self.ancho_boton * 8), 10))

        # Dibujar líneas verticales en las posiciones correspondientes y agregar texto
        for i in range(9):  # 9 secciones
            x_pos = separacion_vertical * (i + 1)
            pygame.draw.line(screen, (0, 0, 0), (x_pos, 10), (x_pos, self.y), 3)

            # Renderizar el texto
            texto_renderizado = self.font.render(textos[i], True, (0, 0, 0))  # Color negro para el texto
            # Posicionar el texto en el centro de cada división
            texto_rect = texto_renderizado.get_rect(center=(x_pos - self.ancho_boton // 2, self.y - 20))
            screen.blit(texto_renderizado, texto_rect)

    def manejar_eventos(self, event):  # Agregar screen como argumento
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pos

            # Coordenadas y dimensiones del área del botón CABLE
            boton_cable_x = 0
            boton_cable_y = 3
            boton_cable_ancho = self.ancho_boton
            boton_cable_alto = 45

            if boton_cable_x <= mouse_x <= boton_cable_x + boton_cable_ancho and boton_cable_y <= mouse_y <= boton_cable_y + boton_cable_alto:
                # Cambiar el color del botón CABLE
                if (self.cable_pulsado == True):
                    self.cable_pulsado = False
                    self.color_cable = self.color
                else:
                    self.cable_pulsado = True
                    self.color_cable = self.color_pulsar

            # Coordenadas y dimensiones del área del botón led
            boton_led_x = self.ancho_boton
            boton_led_y = 3
            boton_led_ancho = self.ancho_boton
            boton_led_alto = 45

            if boton_led_x <= mouse_x <= boton_led_x + boton_led_ancho and boton_led_y <= mouse_y <= boton_led_y + boton_led_alto:
                # Cambiar el color del botón led
                if (self.led_pulsado == True):
                    self.led_pulsado = False
                    self.color_led = self.color
                else:
                    self.led_pulsado = True
                    self.color_led = self.color_pulsar
            # Coordenadas y dimensiones del área del botón SWITCH
            boton_switch_x = 2 * self.ancho_boton
            boton_switch_y = 3
            boton_switch_ancho = self.ancho_boton
            boton_switch_alto = 45

            if boton_switch_x <= mouse_x <= boton_switch_x + boton_switch_ancho and boton_switch_y <= mouse_y <= boton_switch_y + boton_switch_alto:
                # Cambiar el color del botón SWITCH
                if (self.switch_pulsado == True):
                    self.switch_pulsado = False
                    self.color_switch = self.color
                else:
                    self.switch_pulsado = True
                    self.color_switch = self.color_pulsar

            # Coordenadas y dimensiones del área del botón RESISTENCIA
            boton_resistencia_x = 3 * self.ancho_boton
            boton_resistencia_y = 3
            boton_resistencia_ancho = self.ancho_boton
            boton_resistencia_alto = 45

            if boton_resistencia_x <= mouse_x <= boton_resistencia_x + boton_resistencia_ancho and boton_resistencia_y <= mouse_y <= boton_resistencia_y + boton_resistencia_alto:
                # Cambiar el color del botón RESISTENCIA
                if (self.res_pulsado == True):
                    self.res_pulsado = False
                    self.color_res = self.color
                else:
                    self.res_pulsado = True
                    self.color_res = self.color_pulsar

            # Coordenadas y dimensiones del área del botón SHiP
            boton_shp_x = 4 * self.ancho_boton
            boton_shp_y = 3
            boton_shp_ancho = self.ancho_boton
            boton_shp_alto = 45

            if boton_shp_x <= mouse_x <= boton_shp_x + boton_shp_ancho and boton_shp_y <= mouse_y <= boton_shp_y + boton_shp_alto:
                # Cambiar el color del botón SHP
                if (self.ship_pulsado == True):
                    self.ship_pulsado = False
                    self.color_ship = self.color
                else:
                    self.ship_pulsado = True
                    self.color_ship = self.color_pulsar

            # Coordenadas y dimensiones del área del botón MOTOR
            boton_motor_x = 5 * self.ancho_boton
            boton_motor_y = 3
            boton_motor_ancho = self.ancho_boton
            boton_motor_alto = 45

            if boton_motor_x <= mouse_x <= boton_motor_x + boton_motor_ancho and boton_motor_y <= mouse_y <= boton_motor_y + boton_motor_alto:
                # Cambiar el color del botón MOTOR
                if (self.motor_pulsado == True):
                    self.motor_pulsado = False
                    self.color_motor = self.color
                else:
                    self.motor_pulsado = True
                    self.color_motor = self.color_pulsar

            # Coordenadas y dimensiones del área del botón PROTO
            boton_proto_x = 6 * self.ancho_boton
            boton_proto_y = 3
            boton_proto_ancho = self.ancho_boton
            boton_proto_alto = 45

            if boton_proto_x <= mouse_x <= boton_proto_x + boton_proto_ancho and boton_proto_y <= mouse_y <= boton_proto_y + boton_proto_alto:
                # Cambiar el color del botón PROTO
                if (self.proto_pulsado == True):
                    self.proto_pulsado = False
                    self.color_proto = self.color
                else:
                    self.proto_pulsado = True
                    self.color_proto = self.color_pulsar

            # Coordenadas y dimensiones del área del botón EDITAR
            boton_editar_x = 7 * self.ancho_boton
            boton_editar_y = 3
            boton_editar_ancho = self.ancho_boton
            boton_editar_alto = 45

            if boton_editar_x <= mouse_x <= boton_editar_x + boton_editar_ancho and boton_editar_y <= mouse_y <= boton_editar_y + boton_editar_alto:
                # Cambiar el color del botón EDITAR
                if (self.editar_pulsado == True):
                    self.editar_pulsado = False
                    self.color_editar = self.color
                else:
                    self.editar_pulsado = True
                    self.color_editar = self.color_pulsar

            # Coordenadas y dimensiones del área del botón BORRAR
            boton_borrar_x = 8 * self.ancho_boton
            boton_borrar_y = 3
            boton_borrar_ancho = self.ancho_boton
            boton_borrar_alto = 45

            if boton_borrar_x <= mouse_x <= boton_borrar_x + boton_borrar_ancho and boton_borrar_y <= mouse_y <= boton_borrar_y + boton_borrar_alto:
                # Cambiar el color del botón BORRAR
                if (self.borrar_pulsado == True):
                    self.borrar_pulsado = False
                    self.color_borrar = self.color
                else:
                    self.borrar_pulsado = True
                    self.color_borrar = self.color_pulsar
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
                    color = (234, 79, 235)  # morado
                elif conector_inicio.neutro and conector_fin.neutro:
                    color = (61, 205, 234)  # azul cielo dark
                else:
                    color = "black"
            else:
                color = "black"
            pygame.draw.line(screen, color, (cable[0].x, cable[0].y), (cable[1].x, cable[1].y), 3)

    def comienzo_cable(self, conector_origen):
        self.inicio_cable = conector_origen
        self.dibujando_cable = True

    def energy_protoboard(self, pila_turno):
        for nodo in conectores:  # ve los padres de p+ y p- segun eso da energy o no
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

            elif self.inicio_cable.nombre in ["pila+", "pila-"]:
                for nodo in conectores:
                    if nodo.y == conector_siguiente.y:  # misma fila (solo c1 y c2)
                        self.inicio_cable.agregar_conexion(nodo)

            elif self.inicio_cable.nombre.startswith(
                    ("conector1_", "conector2_")) and conector_siguiente.nombre.startswith(("pila")):
                for nodo in conectores:
                    if nodo.y == self.inicio_cable.y:  # misma fila (solo c1 y c2)
                        conector_siguiente.agregar_conexion(nodo)

            else:
                for nodo in conectores:
                    if nodo.x == conector_siguiente.x:  # ver si estan en la misma columna | se limita el alcance
                        if conector_siguiente.nombre.startswith("conector3_"):
                            if nodo.nombre.startswith("conector3_") and nodo.nombre != self.inicio_cable.nombre:
                                self.inicio_cable.agregar_conexion(nodo)
                        elif conector_siguiente.nombre.startswith("conector4_"):  # limita el rango de add solo a c4_
                            if nodo.nombre.startswith("conector4_") and nodo.nombre != self.inicio_cable.nombre:
                                self.inicio_cable.agregar_conexion(nodo)

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

    def buscar_conexiones(self, nodo, nodo_objetivo):
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
        # ----- QUITAR OBJETOS -----
        for nodo in conectores:
            if not nodo.nombre.startswith("pila"):
                nodo.fase = False
                nodo.neutro = False
            nodo.padre = nodo

        cables.clear()
        guardar_led.clear()
        guardar_switch.clear()
        # --------- FIN ---------
        return
class Led:
    def __init__(self, color, x, y, x1, x2, y1, y2):
        self.color = color
        self.x = x
        self.y = y
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def led_apagada(self, screen):
        patita1 = punto_mas_cercano((self.x1, self.y1), conectores, distancia_maxima)
        patita2 = punto_mas_cercano((self.x2, self.y2), conectores, distancia_maxima)
        conector1 = None
        conector2 = None
        for i in conectores:
            if i.x == patita1.x and i.y == patita1.y:
                conector1 = i
            elif i.x == patita2.x and i.y == patita2.y:
                conector2 = i
        if conector1 == None or conector2 == None:
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
            pygame.draw.line(screen, self.color, (start_x, start_y), (end_x, end_y), 2)
class Switch:
    def __init__(self, x, y, x1, x2, x3, x4, y1, y2, y3, y4):
        self.x = x
        self.y = y
        self.x1 = x1  # patita 1 izquierda / derecha
        self.x2 = x2  # patita 2  derecha / izquierda
        self.x3 = x3  # patita 3
        self.x4 = x4  # patita 4
        self.y1 = y1  # patita 1
        self.y2 = y2  # patita 1
        self.y3 = y3  # patita 1
        self.y4 = y4  # patita 1
        self.estado = False
    def switch_proto(self, screen):
        lado = 40  # Tamaño del switch (cuadrado)
        body_color = (150, 150, 150)
        circle_radius = 8  # Radio del "círculo" en el medio
        # Dibujar patitas
        pygame.draw.line(screen, (0, 0, 0), (self.x1, self.y1), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 1
        pygame.draw.line(screen, (0, 0, 0), (self.x2, self.y2), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 2
        pygame.draw.line(screen, (0, 0, 0), (self.x3, self.y3), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 3
        pygame.draw.line(screen, (0, 0, 0), (self.x4, self.y4), (self.x + lado // 2, self.y + lado // 2), 2)  # patita 4
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
class Basurero:
    def __init__(self):
        # No presenta atributos
        pass
    def eliminar_led(self, x, y):
        mi_led=buscar_led(x,y)
        if mi_led is not None:
            guardar_led.remove(mi_led)
        else:
            print("No se ha encontrado un led dentro del rango de clic")
    def eliminar_switch(self, x, y):
        rango_click = 20
        mi_switch = None
        # Buscador de led en la lista de los switchs
        for switch in guardar_switch:
            # si se clickea en el rango correspondiente, se borra de la lista switch
            if switch.x - rango_click <= x <= switch.x + rango_click and switch.y - rango_click <= y <= switch.y + rango_click:
                mi_switch = switch
        if mi_switch is not None:
            guardar_switch.remove(mi_switch)
        else:
            print("No se ha encontrado un led dentro del rango de clic")
    def eliminar_cable(self, x, y):
        rango_click = 10
        global verificador
        # Buscador de cable en la lista de los cables
        for cable in cables:
            # si se clickea en el rango correspondiente, se borra de la lista cable
            if cable[0].x - rango_click <= x <= cable[0].x + rango_click and cable[0].y - rango_click <= y <= cable[0].y + rango_click:
                start = cable[1]
                end = cable[0]
                cables.remove(cable)
                # print("Click en el origen del cable")

                if start and end:
                    end.eliminar_conexion(start, end)
                    if end.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in conectores:
                            if nodo.y == end.y:
                                nodo.eliminar_conexion(nodo, start)
                    # -------------------- elimina columnas ------------------------
                    else:
                        # print("--------------------------------")
                        cont = 0
                        for nodo in conectores:
                            if nodo.x == start.x:
                                if start.nombre.startswith("conector3_"):
                                    # print(nodo.nombre,"\t",cont)
                                    cont += 1
                                    nodo.eliminar_conexion(nodo, end)
                                elif end.nombre.startswith("conector4_"):
                                    nodo.eliminar_conexion(nodo, end)
                verificador = True

            elif cable[1].x - rango_click <= x <= cable[1].x + rango_click and cable[1].y - rango_click <= y <= cable[
                1].y + rango_click:
                start = cable[1]
                end = cable[0]
                cables.remove(cable)
                # print("Click en el destino del cable")

                if start and end:
                    start.eliminar_conexion(start, end)
                    if start.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in conectores:
                            if nodo.y == start.y:
                                nodo.eliminar_conexion(nodo, end)
                    # -------------------- elimina columnas ------------------------
                    else:
                        # print("--------------------------------")
                        cont = 0
                        for nodo in conectores:
                            if nodo.x == start.x:
                                if start.nombre.startswith("conector3_"):
                                    # print(nodo.nombre,"\t",cont)
                                    cont += 1
                                    nodo.eliminar_conexion(nodo, end)

                                elif start.nombre.startswith("conector4_"):
                                    nodo.eliminar_conexion(nodo, end)
                verificador = True
def buscar_led(x,y):
    rango_click = 10
    mi_led = None
    # Buscador de led en la lista de los leds
    for led in guardar_led:
        # si se clickea en el rango correspondiente, se borra de la lista led
        if led.x - rango_click <= x <= led.x + rango_click and led.y - rango_click <= y <= led.y + rango_click:
            mi_led = led
    return mi_led
def buscar_switch(x,y):
    rango_clik = 10
    mi_switch = None
    for switch in guardar_switch:
        if switch.x - rango_clik <= x <= switch.x + rango_clik and switch.y - rango_clik <= y <= switch.y+rango_clik:
            mi_switch = switch
    return mi_switch
def dibujar_a(screen, x, y, ancho, alto, color):
    pygame.draw.line(screen, color, (x, y + alto), (x + ancho // 2, y), 2)  # Línea diagonal izquierda
    pygame.draw.line(screen, color, (x + ancho // 2, y), (x + ancho, y + alto), 2)  # Línea diagonal derecha
    pygame.draw.line(screen, color, (x + ancho // 4, y + alto // 2), (x + ancho - ancho // 4, y + alto // 2),
                     2)  # Barra horizontal
def dibujar_b(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), ((x + alto // 2), y), 2)
    pygame.draw.line(screen, color, ((x + alto // 2), y), ((x + alto // 2), (y + ((alto // 2) - 3))), 2)
    pygame.draw.line(screen, color, (x + alto // 2, (y + ((alto // 2) - 3))), ((x), (y + ((alto // 2) - 3))), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + alto // 2), (y + alto)), 2)
    pygame.draw.line(screen, color, ((x + alto // 2), (y + alto)), ((x + alto // 2), (y + (alto // 2))), 2)
    pygame.draw.line(screen, color, ((x + alto // 2), (y + (alto // 2))), (x, y + alto // 2), 2)
def dibujar_c(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, ((x + ancho), y), ((x + ancho), (y + (alto // 3))), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
    pygame.draw.line(screen, color, ((x + ancho), (y + alto)), ((x + ancho), (y + alto - (alto // 3))), 2)
def dibujar_d(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), (x + alto // 5, y), 2)
    pygame.draw.line(screen, color, (x + alto // 5, y), (x + ancho, y + alto), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), (x + ancho, y + alto), 2)
def dibujar_e(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + (alto // 2))), ((x + ancho), (y + alto // 2)), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
def dibujar_f(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto // 2)), ((x + ancho), (y + alto // 2)), 2)
def dibujar_g(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
    pygame.draw.line(screen, color, ((x + ancho), (y + alto)), ((x + ancho), (y + alto - alto // 3)), 2)
    pygame.draw.line(screen, color, ((x + ancho), (y + alto // 2)), (x + alto // 3, (y + alto // 2)), 2)
def dibujar_h(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, (y + alto // 2)), ((x + ancho), (y + alto // 2)), 2)
    pygame.draw.line(screen, color, (x + ancho, y), (x + ancho, (y + alto)), 2)
def dibujar_i(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, ((x + (ancho // 2)), y), ((x + (ancho // 2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
def dibujar_j(screen, x, y, alto, ancho, color):
    pygame.draw.line(screen, color, ((x + (ancho // 2)), y), ((x + (ancho // 2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho // 2), (y + alto)), 2)
def dibujar_mas(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x + 5, y - 5), (x + 5, y + 5), 2)
def dibujar_menos(screen, x, y, color):
    pygame.draw.line(screen, color, (x + 5, y - 5), (x + 5, y + 5), 2)
def dibujar_1(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x + 5, y + 10), 2)
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
def dibujar_2(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), (x + 5, y), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y + alto), (x + alto, y + alto), 2)
    pygame.draw.line(screen, color, (x + alto, y + alto), (x + alto, y), 2)
def dibujar_3(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x + alto, y + alto), (x + alto, y), 2)
def dibujar_4(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), (x + 5, y + alto), 2)
def dibujar_5(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y + alto), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x + alto, y + alto), (x + alto, y), 2)
def dibujar_0(screen, x, y, alto, color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y + alto), (x + alto, y + alto), 2)
    pygame.draw.line(screen, color, (x + alto, y + alto), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
def switch_presionado(switch, mouse_pos):
    lado = 40  # Tamaño del switch (cuadrado)
    x, y = mouse_pos
    if switch.x <= x <= switch.x + lado and switch.y <= y <= switch.y + lado:
        return True
    return False
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

def dibujar_conectores(screen, conectores):  # le da color a los puntos segun el tipo de energy
    for conector in conectores:
        if not conector.nombre.startswith("pila"):
            if conector.fase:
                pygame.draw.line(screen, "red", (conector.x, conector.y), (conector.x + conector.largo, conector.y),6)
            elif conector.neutro:
                pygame.draw.line(screen, "blue", (conector.x, conector.y),(conector.x + conector.largo, conector.y),6)

# Main
pygame.init()
# --------- esto lo tengo que trabajar para fullscreen ----------------
# Obtener el tamaño de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Crear la ventana con el tamaño ajustado
screen = pygame.display.set_mode((1000, 650), pygame.RESIZABLE)

pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()
# ---------- fin a trabajar ----------
# Crear el cableado
cableado = Cableado()

#Crear la resistencia
resistencia = Resistencia()

##Crear el basurero
basurero = Basurero()

fullscreen = False
running = True
x1 = 0
x2 = 0
y1 = 0
y2 = 0
x3 = 0
x4 = 0
y3 = 0
y4 = 0
guardar_led = []
led_coordenadas = []
guardar_switch = []
switch_coordenadas = []
ultimo_conector = None
mm = Menu_f()
switch16=Switch_16(350,265)
# editar led
led_a_editar = None
conector_1_editar = None
conector_2_editar = None
# editar switch
switch_editar=None
c_1_editar=None
c_2_editar=None
c_3_editar=None
c_4_editar=None

def buscar_conector_por_nombre(nombre, lista_conectores):
    for conector in lista_conectores:
        if conector.nombre == nombre:
            return conector
    return None

def distancia(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

def punto_mas_cercano(pos_mouse, lista_conectores):
    punto_cercano = None
    distancia_minima = 10000

    for conector in lista_conectores:
        conector_pos = (conector.x, conector.y)  # Extrae las coordenadas del conector
        dist = distancia(pos_mouse, conector_pos)
        if dist < distancia_minima and dist <= 10:
            distancia_minima = dist
            punto_cercano = conector
    return punto_cercano

x_proto = (screen.get_width() - 650) // 2
y_proto = (screen.get_height() - 300) // 2
protoboard = Protoboard(x_proto, y_proto)

# Crear y dibujar Pila
x_pila = (screen.get_width() - 950) // 2
y_pila = (screen.get_height() - 50) // 2
pila = Pila(x_pila, y_pila,conectores)

# Crear y dibujar Menú
x_menu = x_proto
y_menu = y_proto - 170
menu = Menu(x_menu,y_menu)


while running:
    screen.fill("white")  # directo el color sin variables extra

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
    #dibujar menu
    mm.dibujar(screen)

    #dibujar swuitch de 16
    switch16.dibujar(screen)


    # Crear funcionalidad de basurero

    clock = pygame.time.Clock()

    distancia_maxima = 10
    cableado.dibujar_cables()

    cableado.dibujar_cables(screen,cables)
    resistencia.dibujar_resistencia(screen,resistencias)

    for i in guardar_led:
        i.led_apagada(screen,conectores)

    for i in guardar_switch:
        i.switch_proto(screen,conectores)

    # Manejo de eventos de la pantalla
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE or event.type == pygame.QUIT:
            running = False
        mm.manejar_eventos(event)
        if event.type == VIDEORESIZE:
            if not fullscreen:
                if event.w > 1000 or event.h > 650:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                else:
                    screen = pygame.display.set_mode((1000, 650), pygame.RESIZABLE)

        # Manejo de eventos especial para que cuando se quiera eliminar un item, se elimine bien y no se quiera agregar un cable

        # Manejo de eventos normal para cables, led y switch
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()  # Obtén la posición del mouse
            for switch in guardar_switch:
                if switch_presionado(switch, mouse_pos):  # Verifica si un switch fue presionado
                    patita1 = punto_mas_cercano((switch.x1, switch.y1), conectores)
                    patita2 = punto_mas_cercano((switch.x2, switch.y2), conectores)

                    conector_p1 = None
                    conector_p2 = None
                    for i in conectores:
                        if i.x == patita1.x and i.y == patita1.y:
                            conector_p1 = i
                        elif i.x == patita2.x and i.y == patita2.y:
                            conector_p2 = i
                    if conector_p1 is None or conector_p2 is None:
                        print("existe problemas en los conectores")
                    elif switch.estado:  # Si el switch está encendido, lo apagamos
                        conector_p1.eliminar_conexion(conector_p1, conector_p2)
                        switch.estado = False
                        print("Switch apagado")
                    else:  # Si el switch está apagado, lo encendemos
                        conector_p1.agregar_conexion(conector_p2)
                        switch.estado = True
                        print("Switch encendido")
            mouse_pos = event.pos
            conector_cercano = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
            switch16.detectar_click(mouse_pos)
            x, y = event.pos
            if mm.borrar_pulsado:
                if mm.led_pulsado:
                    basurero.eliminar_led(x, y)
                elif mm.switch_pulsado:
                    basurero.eliminar_switch(x, y)
                elif mm.cable_pulsado:
                    basurero.eliminar_cable(x, y)
                else:
                    print("No se ha seleccionado un elemento para borrar")
            elif mm.editar_pulsado:
                if mm.led_pulsado:
                    if led_a_editar is None:
                        print("buscando led")
                        led_a_editar = buscar_led(x, y)
                    elif conector_1_editar is None:
                        print("buscando conector 1")
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                    elif conector_2_editar is None:
                        print("buscando conector 2")
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            print("conector 2 valido")
                            conector_2_editar = conector_2_aux
                            led_a_editar.x = (conector_1_editar.x + conector_2_editar.x) / 2
                            led_a_editar.y = (conector_1_editar.y + conector_2_editar.y) / 2
                            led_a_editar.x1 = conector_1_editar.x
                            led_a_editar.y1 = conector_1_editar.y
                            led_a_editar.x2 = conector_2_editar.x
                            led_a_editar.y2 = conector_2_editar.y
                            led_a_editar = None
                            conector_1_editar = None
                            conector_2_editar = None
                            print("led editado")
                    else:
                        print("error al editar led")
                    # busca el led que se quiere editar
                    # seleccionar los conectores nuevos
                    # actualizar los conectores al led
                    print("editar led")

                if mm.switch_pulsado:
                    if switch_editar is None:
                        print("buscando switch")
                        switch_editar = buscar_switch(x, y)
                    elif c_1_editar is None:
                        print("buscando conector 1")
                        c_1_editar = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                    elif c_2_editar is None:
                        print("buscando conector 2")
                        c_2_aux = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                        if c_2_aux is not None and c_2_aux != c_1_editar:
                            c_2_editar = c_2_aux
                        else:
                            print("conector 2 no válido, es igual al conector 1")
                    elif c_3_editar is None:
                        print("buscando conector 3")
                        c_3_aux = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                        if c_3_aux is not None and c_3_aux != c_1_editar and c_3_aux != c_2_editar:
                            c_3_editar = c_3_aux
                        else:
                            print("conector 3 no válido, es igual a conector 1 o conector 2")
                    elif c_4_editar is None:
                        print("buscando conector 4")
                        c_4_aux = punto_mas_cercano(mouse_pos, conectores, distancia_maxima)
                        if c_4_aux is not None and c_4_aux != c_1_editar and c_4_aux != c_2_editar and c_4_aux != c_3_editar:
                            c_4_editar = c_4_aux
                            print("conectores válidos")
                            # Asignar las posiciones de las patitas del switch
                            switch_editar.x1 = c_1_editar.x
                            switch_editar.y1 = c_1_editar.y
                            switch_editar.x2 = c_2_editar.x
                            switch_editar.y2 = c_2_editar.y
                            switch_editar.x3 = c_3_editar.x
                            switch_editar.y3 = c_3_editar.y
                            switch_editar.x4 = c_4_editar.x
                            switch_editar.y4 = c_4_editar.y
                            # Reiniciar las variables de edición
                            switch_editar = None
                            c_1_editar = None
                            c_2_editar = None
                            c_3_editar = None
                            c_4_editar = None
                            print("switch editado")
                        else:
                            print("conector 4 no válido, es igual a conector 1, 2 o 3")
                    else:
                        print("error al editar switch")
                    # Proceso de edición del switch
                    print("editar switch")
                else:
                    print("No se ha seleccionado un elemento para editar")

            elif mm.led_pulsado:
                if not conector_cercano:
                    pass
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
                        tupla1 = (x1, y1)
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

                        guardar_led.append(led_a)

            elif mm.switch_pulsado:
                if not conector_cercano:
                    pass
                elif x1 == 0:
                    x1 = conector_cercano.x
                    y1 = conector_cercano.y
                elif x2 == 0:
                    x2 = conector_cercano.x
                    y2 = conector_cercano.y
                elif x3 == 0:
                    x3 = conector_cercano.x
                    y3 = conector_cercano.y
                else:
                    x4 = conector_cercano.x
                    y4 = conector_cercano.y
                    tupla1 = (x1, y1)
                    tupla2 = (x2, y2)
                    tupla3 = (x3, y3)
                    tupla4 = (x4, y4)
                    switch_coordenadas.append(tupla1)
                    switch_coordenadas.append(tupla2)
                    switch_coordenadas.append(tupla3)
                    switch_coordenadas.append(tupla4)
                    if (((x1 + 40) >= x2) or ((x1 - 40) <= x2) or ((x1 + 20) <= x2) or ((x1 - 20) <= x2)) and (
                            ((y1 + 40) <= y2) or ((y1 - 40) >= y2) or ((y1 + 20) <= y2) or ((y1 - 20) <= y2)) and (
                            x1 - x2) <= 40 and (x2 - x1) <= 40 and (y2 - y1) <= 40 and (y1 - y2) <= 40:
                        x_mitad, y_mitad = (((x1 + x2) / 2) - 10, ((y1 + y2) / 2) - 10)
                        switch_a = Switch(x_mitad, y_mitad, x1, x2, x3, x4, y1, y2, y3, y4)
                        switch_a.switch_proto(screen)
                        x1, x2, y1, y2, x3, x4, y3, y4 = 0, 0, 0, 0, 0, 0, 0, 0
                        guardar_switch.append(switch_a)

            elif mm.cable_pulsado:
                for conector in conectores:
                    if conector_cercano == conector:
                        if not cableado.dibujando_cable:
                            cableado.comienzo_cable(conector)
                        else:
                            cableado.finalizar_cable(conector,conectores,cables)
                            ultimo_conector = conector_cercano

    cableado.dibujar_cable_actual()

    for c in conectores:  # busca las pilas y las envia a cambiar o no estado fase / neutro
        if c.nombre == "pila+":
            if not c.conexiones:
                c.padre = c
            cableado.energy_protoboard(c)
        if c.nombre == "pila-":
            if not c.conexiones:
                c.padre = c
            cableado.energy_protoboard(c)

    dibujar_conectores(screen, conectores)
    pygame.display.flip()
    mainClock.tick(30)

pygame.quit()