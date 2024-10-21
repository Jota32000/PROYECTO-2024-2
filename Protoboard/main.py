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
from Chip import Chip
conectores = []
cables = []
cables_coordenadas = []
resistencias = []
resistencias_coordenadas = []
guardar_led = []
guardar_switch = []
switch_coordenadas = []
guardar_switch16=[]
guardar_chip=[]

def buscar_led(x,y):
    rango_click = 10
    mi_led = None
    # Buscador de led en la lista de los leds
    for led in guardar_led:
        # si se clickea en el rango correspondiente, se borra de la lista led
        if led.x - rango_click <= x <= led.x + rango_click and led.y - rango_click <= y <= led.y + rango_click:
            mi_led = led
    return mi_led

def buscar_switch(conector):
    rango_clik = 20
    mi_switch = None
    for switch in guardar_switch:
        # retorna el conector del switch
        if (switch.x - rango_clik <= conector.x <= switch.x + rango_clik and
            switch.y - rango_clik <= conector.y <= switch.y + rango_clik):
            mi_switch = switch
            break
    return mi_switch
def buscar_cable(conector1, conector2):
    for cable in cables:
        if (cable.conector_inicio == conector1 and cable.conector_fin == conector2) or (cable.conector_inicio == conector2 and cable.conector_fin == conector1):
               return cable
    return None
def buscar_resistencia(conector1, conector2):
    for resistencia in resistencias:
        if (resistencia.conector_inicio == conector1 and resistencia.conector_fin == conector2) or (resistencia.conector_inicio == conector2 and resistencia.conector_fin == conector1):
            return resistencia
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

def buscar_pin(x,y,cantidad,lado_x,lado_y):
    pines=[]
    i=0
    while i<cantidad:
        x_aux= x+(i*lado_x)
        y_aux=y+(i*lado_y)
        pin=punto_mas_cercano((x_aux,y_aux),conectores)
        pines.append(pin)
        i+=1
    return pines

# Main
pygame.init()
# Obtener el tamaño de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Crear la ventana con el tamaño ajustado
screen = pygame.display.set_mode((1000, 650), pygame.RESIZABLE)

pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()
# Crear el cableado
cableado = Cableado(conectores,cables)

#Crear la resistencia
resistencia = Resistencia(conectores,resistencias)

#Crear el basurero
basurero = Basurero(guardar_led, guardar_switch, conectores, cables, resistencias,guardar_switch16,guardar_chip)

fullscreen = False
running = True
x1, x2, x3, x4 = 0, 0, 0, 0
y1, y2, y3, y4 = 0, 0, 0, 0

ultimo_conector = None
mm = Menu()

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
#editar switch 16
c16_1=0
c16_2=0
#chip datos
c_x=0
c_y=0
#switch 4
c4_x=0
c4_y=0
nueva_resistencia = None

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
conector=Conector("1",0,0,conectores)

while running:
    screen.fill("white")  # directo el color sin variables extra

    protoboard.crear(screen)
    conector.dibujar(screen)

    pila.dibujarPila(screen)
    #dibujar menu
    mm.dibujar(screen)
    clock = pygame.time.Clock()

    for i in guardar_led:
        i.led_apagada(screen)

    for i in guardar_switch:
        i.switch_proto(screen)

    for i in cables:
        i.dibujar_cables(screen)

    for i in guardar_switch16:
        i.dibujar(screen)

    for i in resistencias:
        i.dibujar_resistencia(screen)

    for i in guardar_chip:
        i.dibujar(screen)
    
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
            for switch4 in guardar_switch:
                switch4.detectar_click(mouse_pos)
            for switch16 in guardar_switch16:
                switch16.detectar_click(mouse_pos)
            mouse_pos = event.pos
            conector_cercano = punto_mas_cercano(mouse_pos, conectores)

            x, y = event.pos
            if mm.borrar_pulsado: # Opciones para eliminar componentes
                if mm.led_pulsado:
                    basurero.eliminar_led(conector_cercano)
                elif mm.switch_pulsado:
                   if mm.boton_switch16_pulsado:
                       basurero.eliminar_switch16(conector_cercano)
                   elif mm.boton_switch2_pulsado:
                        basurero.eliminar_switch(conector_cercano)
                elif mm.cable_pulsado:
                    basurero.eliminar_cable(conector_cercano)
                elif mm.res_pulsado:
                    basurero.eliminar_resistencia(conector_cercano)
                elif mm.chip_pulsado:
                    basurero.eliminar_chip(conector_cercano)
                else:
                    print("No se ha seleccionado un elemento para borrar")
                conectores[0].padre = conectores[0]
                conectores[0].fase = True
                conectores[1].padre = conectores[1]
                conectores[1].neutro = True
            elif mm.editar_pulsado: # Opciones para editar componentes
                if mm.led_pulsado:
                    if led_a_editar is None:
                        print("Escoge la led a editar (Clickea sobre ella)")
                        print("Luego clickea dos posiciones de la protoboard donde colocarla")
                        led_a_editar = buscar_led(x, y)
                    elif conector_1_editar is None:
                        #print("buscando conector 1")
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
                            print("led editado con éxito")
                    else:
                        print("error al editar led")
                    # busca el led que se quiere editar
                    # seleccionar los conectores nuevos
                    # actualizar los conectores al led
                    print("editar led")

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
                            c_1_editar.eliminar_conexion(c_1_editar, c_2_editar)# los antiguos
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

                elif mm.res_pulsado:
                    #print("Primero selecciona las 2 posiciones de la resistencia en la protoboard")
                    #print("Luego selecciona 2 posiciones nuevas donde deseas colocar la resistencia")
                    if c_1_editar is None:
                        print("buscando conector 1")
                        c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif c_2_editar is None:
                        print("buscando conector 2")
                        c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_2_aux is not None and c_2_aux != c_1_editar:
                            print("conector 2 valido")
                            c_2_editar = c_2_aux
                            cable_editar = buscar_resistencia(c_1_editar, c_2_editar)
                            if cable_editar is None:
                                print("resistencia no encontrado")
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


                elif mm.boton_switch2_pulsado:
                    print("hola")
                    if conector_1_editar is None:
                        print("buscando conector 1")
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        print("buscando conector 2")
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            basurero.eliminar_switch(conector_1_editar)
                            c4_x = conector_2_aux.x
                            c4_y = conector_2_aux.y
                            if c4_x != 0 and c4_y != 0:
                                switch4 = Switch(conector_2_aux)
                                pines_superior = buscar_pin(c4_x, c4_y, 2, 60, 0)
                                switch4.pin2 = pines_superior[1]
                                pines_inferior = buscar_pin(c4_x, c4_y, 2, 60, 0)
                                switch4.pin3 = pines_inferior[0]
                                switch4.pin4 = pines_inferior[1]
                                guardar_switch.append(switch4)
                                c4_x, c4_y = 0, 0  # Resetear las coordenadas
                                mm.switch_pulsado = False
                                mm.color_switch = (162, 206, 143)
                                mm.boton_switch2_pulsado = False
                                mm.color_switch4 = (162, 206, 143)
                                conector_1_editar = None
                                conector_2_editar = None

                elif mm.chip_pulsado:
                    if conector_1_editar is None:
                        print("buscando conector 1")
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        print("buscando conector 2")
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            basurero.eliminar_chip(conector_1_editar)
                            c_x = conector_2_aux.x
                            c_y = conector_2_aux.y
                            if c_x != 0 and c_y != 0:
                                chip = Chip(c_x, c_y)
                                guardar_chip.append(chip)
                                c_x, c_y = 0, 0  # Resetear las coordenadas
                                mm.chip_pulsado = False
                                mm.color_ship = (162, 206, 143)
                                conector_1_editar = None
                                conector_2_editar = None

                elif mm.boton_switch16_pulsado:
                    if conector_1_editar is None:
                        print("buscando conector 1")
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        print("buscando conector 2")
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            basurero.eliminar_switch16(conector_1_editar)
                            c16_1 = conector_2_aux.x
                            c16_2 = conector_2_aux.y
                            if c16_1 != 0 and c16_2 != 0:
                                switch16 = Switch_16(conector_2_aux)
                                pines_superior = buscar_pin(c16_1, c16_2, 8, 30, 0)
                                switch16.pin2 = pines_superior[1]
                                switch16.pin3 = pines_superior[2]
                                switch16.pin4 = pines_superior[3]
                                switch16.pin5 = pines_superior[4]
                                switch16.pin6 = pines_superior[5]
                                switch16.pin7 = pines_superior[6]
                                switch16.pin8 = pines_superior[7]
                                pines_inferior = buscar_pin(c16_1, c16_2 + 60, 8, 30, 0)
                                switch16.pin9 = pines_inferior[0]
                                switch16.pin10 = pines_inferior[1]
                                switch16.pin11 = pines_inferior[2]
                                switch16.pin12 = pines_inferior[3]
                                switch16.pin13 = pines_inferior[4]
                                switch16.pin14 = pines_inferior[5]
                                switch16.pin15 = pines_inferior[6]
                                switch16.pin16 = pines_inferior[7]
                                guardar_switch16.append(switch16)
                                c16_1, c16_2 = 0, 0  # Resetear las coordenadas
                                mm.switch_pulsado = False
                                mm.color_switch = (162, 206, 143)
                                mm.boton_switch16_pulsado = False
                                mm.color_switch16 = (162, 206, 143)
                                conector_1_editar = None
                                conector_2_editar = None

            elif mm.led_pulsado:
                #print("Botón LED encendido")
                #print("Elige dos puntos en la protoboard\n")
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
                if mm.boton_switch16_pulsado:
                    #print("Botón SWITCH 16 pines encendido")
                    #print("Elige un punto en la protoboard para colocarlo (corresponde a la esquina superior izquierda)\n")
                    if not conector_cercano:
                        pass
                    elif c16_1 == 0:
                        c16_1 = conector_cercano.x
                        c16_2 = conector_cercano.y
                        if c16_1!=0 and c16_2!=0:
                            switch16 = Switch_16(conector_cercano)
                            pines_superior =buscar_pin(c16_1,c16_2,8,30,0)
                            switch16.pin2 =pines_superior[1]
                            switch16.pin3 = pines_superior[2]
                            switch16.pin4 = pines_superior[3]
                            switch16.pin5 = pines_superior[4]
                            switch16.pin6 = pines_superior[5]
                            switch16.pin7 = pines_superior[6]
                            switch16.pin8 = pines_superior[7]
                            pines_inferior = buscar_pin(c16_1,c16_2+60,8,30,0)
                            switch16.pin9 = pines_inferior[0]
                            switch16.pin10 = pines_inferior[1]
                            switch16.pin11 = pines_inferior[2]
                            switch16.pin12 = pines_inferior[3]
                            switch16.pin13 = pines_inferior[4]
                            switch16.pin14 = pines_inferior[5]
                            switch16.pin15 = pines_inferior[6]
                            switch16.pin16 = pines_inferior[7]
                            guardar_switch16.append(switch16)
                            c16_1, c16_2 = 0, 0  # Resetear las coordenadas
                            mm.switch_pulsado = False
                            mm.color_switch=(162, 206, 143)
                            mm.boton_switch16_pulsado=False
                            mm.color_switch16=(162, 206, 143)
                if mm.boton_switch2_pulsado:
                    print("boton switch 2")
                    if not conector_cercano:
                        pass
                    elif c4_x == 0:
                        c4_x = conector_cercano.x
                        c4_y = conector_cercano.y
                        if c4_x != 0 and c4_y != 0:
                            switch4 = Switch(conector_cercano)
                            pines_superior = buscar_pin(c4_x, c4_y, 2, 60, 0)
                            switch4.pin2 = pines_superior[1]
                            pines_inferior = buscar_pin(c4_x, c4_y, 2, 60, 0)
                            switch4.pin3 = pines_inferior[0]
                            switch4.pin4 = pines_inferior[1]
                            guardar_switch.append(switch4)
                            c4_x, c4_y = 0, 0  # Resetear las coordenadas
                            mm.switch_pulsado = False
                            mm.color_switch = (162, 206, 143)
                            mm.boton_switch2_pulsado = False
                            mm.color_switch4 = (162, 206, 143)

            elif mm.chip_pulsado:
                print("boton chip")
                if not conector_cercano:
                    pass
                elif c_x == 0:
                    c_x = conector_cercano.x
                    c_y = conector_cercano.y
                    if c_x != 0 and c_y!= 0:
                        chip = Chip(c_x, c_y)
                        guardar_chip.append(chip)
                        c_x, c_y = 0, 0  # Resetear las coordenadas
                        mm.chip_pulsado = False
                        mm.color_ship = (162, 206, 143)

            elif mm.cable_pulsado:
                #print("Botón cable encendido")
                #print("Elige 2 puntos en la protoboard para colocar el cable\n")
                if c_1_editar is None:
                    c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                elif c_2_editar is None:
                    c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                    if c_2_aux is not None and c_2_aux != c_1_editar:
                        c_2_editar = c_2_aux
                        nuevo_cable = Cableado(c_1_editar, c_2_editar)
                        if nuevo_cable.validar_cable(cables):
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
                    

            elif mm.res_pulsado:
                #print("Botón RESISTENCIA encendido")
                #print("Elige 2 puntos en la protoboard para colocar la resistencia (de dimensiones 2X1 o 1X2\n")
                if c_1_editar is None:
                    c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                elif c_2_editar is None:
                    c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                    if c_2_aux is not None and c_2_aux != c_1_editar:
                        c_2_editar = c_2_aux
                        nueva_resistencia = Resistencia(c_1_editar, c_2_editar)
                        if nueva_resistencia.validar_resistencia(resistencias):
                            resistencias.append(nueva_resistencia)
                            resistencias_coordenadas.append(c_1_editar)
                            resistencias_coordenadas.append(c_2_editar)
                            nueva_resistencia.conector_inicio.agregar_conexion(nueva_resistencia.conector_fin)
                        else:
                            print("resistencia no válida")
                        nueva_resistencia = None
                        c_1_editar = None
                        c_2_editar = None
                    else:
                        print("conector 2 no válido, es igual al conector 1")

            elif mm.motor_pulsado:
                #print("Motor pulsado")
                for c in conectores:
                    if not c.nombre.startswith("pila"):
                        c.fase=None
                        c.neutro=None
            elif not mm.motor_pulsado:
                for c in conectores:
                    c.fase=c.padre.fase
                    c.neutro=c.padre.neutro

    if not mm.editar_pulsado and not mm.res_pulsado:
        cableado.dibujar_cable_actual(screen, c_1_editar)
    elif not mm.editar_pulsado and not mm.cable_pulsado:
        resistencia.dibujar_resistencia_actual(screen, c_1_editar)
    pygame.display.flip()
    mainClock.tick(30)
pygame.quit()

