import pygame
import math
from pygame.locals import *
from Resistencia import Resistencia
from Switch import Switch
from Protoboard import Protoboard
from Cableado import Cableado
from Basurero import Basurero
from Pila import Pila
from Menu import Menu
from Led import Led
from Switch_16 import Switch_16
from Conector import Conector

conectores = []
boton_cable = False  # Estado del boton del cable (activado = true o desactivado = false)
boton_led = False  # Estado del boton de la led (activado = true o desactivado = false)
boton_switch = False  # Estado del boton del switch (activado = true o desactivado = false)
boton_edicion = False  # Estado del boton de edición (activado = true o desactivado = false)
boton_basurero = False  # Estado del boton del basurero (activado=true o desactivado = false)
boton_switch16=False
boton_switch4=False

cables = []
cables_coordenadas = []
resistencias = []
guardar_led = []
guardar_switch = []
switch_coordenadas = []

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
        self.switch_4_pulsado = False
        self.switch_16_pulsado = False

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
def buscar_cable(conector1, conector2):
    for cable in cables:
        if (cable.conector_inicio == conector1 and cable.conector_fin == conector2) or (cable.conector_inicio == conector2 and cable.conector_fin == conector1):
               return cable
    return None
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
cableado = Cableado(conectores,cables)

#Crear la resistencia
resistencia = Resistencia()

##Crear el basurero
basurero = Basurero(guardar_led, guardar_switch, conectores, cables, resistencias,cables_coordenadas)

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
nuevo_cable = None
cable_editar = None

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
protoboard = Protoboard(x_proto, y_proto,conectores)

# Crear y dibujar Pila
x_pila = (screen.get_width() - 950) // 2
y_pila = (screen.get_height() - 50) // 2

# Crear conectores Pila + -
pila_mas = Conector("pila+",x_pila + 65, y_pila - 15,conectores)
pila_menos = Conector("pila-",x_pila + 35, y_pila - 15,conectores)

pila_mas.fase=True
pila_menos.neutro=True

conectores.append(pila_mas)
conectores.append(pila_menos)

pila = Pila(x_pila, y_pila)

# Crear y dibujar Menú
x_menu = x_proto
y_menu = y_proto - 170
menu = Menu(x_menu,y_menu)

conector=Conector("1",0,0,conectores)

while running:
    screen.fill("white")  # directo el color sin variables extra

    protoboard.crear(screen)
    conector.dibujar(screen)

    pila.dibujarPila(screen)
    #dibujar menu
    mm.dibujar(screen)

    #dibujar swuitch de 16
    switch16.dibujar(screen)

    # Crear funcionalidad de basurero

    for i in cables:
        i.dibujar_cables(screen)

    for i in guardar_led:
        i.led_apagada(screen)

    for i in guardar_switch:
        i.switch_proto(screen,conectores)
    #for resistencia

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
            conector_cercano = punto_mas_cercano(mouse_pos, conectores)
            switch16.detectar_click(mouse_pos)
            x, y = event.pos
            if mm.borrar_pulsado: # Opciones para eliminar componentes
                if mm.led_pulsado:
                    basurero.eliminar_led(x, y)
                elif mm.switch_pulsado:
                    basurero.eliminar_switch(x, y)
                elif mm.cable_pulsado:
                    #print("conector cercano: ",conector_cercano)
                    basurero.eliminar_cable(conector_cercano)
                else:
                    print("No se ha seleccionado un elemento para borrar")
            elif mm.editar_pulsado: # Opciones para editar componentes
                if mm.led_pulsado:
                    if led_a_editar is None:
                        print("buscando led")
                        led_a_editar = buscar_led(x, y)
                    elif conector_1_editar is None:
                        print("buscando conector 1")
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        print("buscando conector 2")
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            print("conector 2 valido")
                            conector_2_editar = conector_2_aux
                            led_a_editar.conector1 = conector_1_editar
                            led_a_editar.conector2 = conector_2_editar
                            led_a_editar.x = (conector_1_editar.x + conector_2_editar.x) // 2
                            led_a_editar.y = (conector_1_editar.y + conector_2_editar.y) // 2
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

                elif mm.switch_pulsado:
                    if switch_editar is None:
                        print("buscando switch")
                        switch_editar = buscar_switch(x, y)
                    elif c_1_editar is None:
                        print("buscando conector 1")
                        c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif c_2_editar is None:
                        print("buscando conector 2")
                        c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_2_aux is not None and c_2_aux != c_1_editar:
                            c_2_editar = c_2_aux
                        else:
                            print("conector 2 no válido, es igual al conector 1")
                    elif c_3_editar is None:
                        print("buscando conector 3")
                        c_3_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_3_aux is not None and c_3_aux != c_1_editar and c_3_aux != c_2_editar:
                            c_3_editar = c_3_aux
                        else:
                            print("conector 3 no válido, es igual a conector 1 o conector 2")
                    elif c_4_editar is None:
                        print("buscando conector 4")
                        c_4_aux = punto_mas_cercano(mouse_pos, conectores)
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

                elif mm.cable_pulsado:
                    if c_1_editar is None:
                        print("buscando conector 1")
                        c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif c_2_editar is None:
                        print("buscando conector 2")
                        c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_2_aux is not None and c_2_aux != c_1_editar:
                            print("conector 2 valido")
                            c_2_editar = c_2_aux
                            cable_editar = buscar_cable(c_1_editar, c_2_editar)
                            if cable_editar is None:
                                print("Cable no encontrado")
                                c_1_editar = None
                                c_2_editar = None
                    elif (not cable_editar is None) and c_3_editar is None:
                        print("buscando conector 3")
                        c_3_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_3_aux is not None and c_3_aux != c_1_editar and c_3_aux != c_2_editar:
                            c_3_editar = c_3_aux
                    elif (not cable_editar is None) and c_4_editar is None:
                        print("buscando conector 4")
                        c_4_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_4_aux is not None and c_4_aux != c_1_editar and c_4_aux != c_2_editar and c_4_aux != c_3_editar:
                            c_4_editar = c_4_aux
                            # Asignar los conectores al cable
                            cable_editar.conector_inicio = c_3_editar
                            cable_editar.conector_fin = c_4_editar
                            # quitar la conexion anterior
                            c_1_editar.eliminar_conexion(c_1_editar, c_2_editar)
                            c_3_editar.agregar_conexion(c_4_editar)
                            # agregar la nuevas conexiones
                            # Reiniciar las variables de edicion
                            c_1_editar = None
                            c_2_editar = None
                            c_3_editar = None
                            c_4_editar = None
                            cable_editar = None
                        else:
                            print("conector 4 no válido, es igual a conector 1, 2 o 3")

            elif mm.led_pulsado:
                if conector_1_editar is None:
                    print("buscando conector 1")
                    conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                elif conector_2_editar is None:
                    print("buscando conector 2")
                    conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                    if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                        print("conector 2 valido")
                        conector_2_editar = conector_2_aux

                        led_a = Led("green", conector_1_editar, conector_2_editar)
                        guardar_led.append(led_a)
                        print("led editado")
                        conector_1_editar = None
                        conector_2_editar = None
                else:
                    print("error al editar led")
                    # busca el led que se quiere editar
                    # seleccionar los conectores nuevos
                    # actualizar los conectores al led
                    print("editar led")

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
                        switch_a.switch_proto(screen, conectores)
                        x1, x2, y1, y2, x3, x4, y3, y4 = 0, 0, 0, 0, 0, 0, 0, 0
                        guardar_switch.append(switch_a)

            elif mm.cable_pulsado:
                if c_1_editar is None:
                    c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                elif c_2_editar is None:
                    c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                    if c_2_aux is not None and c_2_aux != c_1_editar:
                        c_2_editar = c_2_aux
                        nuevo_cable = Cableado(c_1_editar, c_2_editar)
                        if nuevo_cable.validar_cable(cables):
                            #print("coordenadas del cable: ",c_1_editar,c_2_editar)
                            cables.append(nuevo_cable)
                            cables_coordenadas.append(c_1_editar)
                            cables_coordenadas.append(c_2_editar)
                            nuevo_cable.conector_inicio.agregar_conexion(nuevo_cable.conector_fin)
                        else:
                            print("cable no válido")
                        nuevo_cable = None
                        c_1_editar = None
                        c_2_editar = None
                    else:
                        print("conector 2 no válido, es igual al conector 1")
    if not mm.editar_pulsado:
        cableado.dibujar_cable_actual(screen, c_1_editar)
    pygame.display.flip()
    mainClock.tick(30)
pygame.quit()