# python 3.9 2024-2.3
#pycharm de jetbrains
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
from Motor import Motor
from Display import Display

conectores = []
cables = []
cables_coordenadas = []
resistencias = []
resistencias_coordenadas = []
guardar_led = []
guardar_switch = []
switch_coordenadas = []
guardar_switch16 = []
guardar_chip = []
guardar_chipNOT=[]
guardar_chipOR=[]
guardar_display=[]

def buscar_led(x, y):
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
        if (cable.conector_inicio == conector1 and cable.conector_fin == conector2) or (
                cable.conector_inicio == conector2 and cable.conector_fin == conector1):
            return cable
    return None

def buscar_resistencia(conector1, conector2):
    for resistencia in resistencias:
        if (resistencia.conector_inicio == conector1 and resistencia.conector_fin == conector2) or (
                resistencia.conector_inicio == conector2 and resistencia.conector_fin == conector1):
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

def buscar_pin(x, y, cantidad, lado_x, lado_y):
    pines = []
    i = 0
    while i < cantidad:
        x_aux = x + (i * lado_x)
        y_aux = y + (i * lado_y)
        pin = punto_mas_cercano((x_aux, y_aux), conectores)
        pines.append(pin)
        i += 1
    return pines

# Main
pygame.init()
# Obtener el tamaño de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Crear la ventana con el tamaño ajustado
screen = pygame.display.set_mode((1000, 650), pygame.RESIZABLE)

extension_x, extension_y = 2000, 1300  # Tamaño de la región de contenido
content_surface = pygame.Surface((extension_x, extension_y))
content_surface.fill("WHITE")
scroll_x, scroll_y = 0, 0
scroll_speed = 50 # Velocidad de desplazamiento

pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()
# Crear el cableado
cableado = Cableado(conectores, cables)
# Crear la resistencia
resistencia = Resistencia(conectores, resistencias)
# Crear el basurero
basurero = Basurero(guardar_led, guardar_switch, conectores, cables, resistencias, guardar_switch16,guardar_chip,guardar_chipOR,guardar_chipNOT,guardar_display)
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
switch_editar = None
c_1_editar = None
c_2_editar = None
c_3_editar = None
c_4_editar = None
nuevo_cable = None
cable_editar = None
# editar switch 16
c16_1 = 0
c16_2 = 0
# chip and datos
editar_andX=None
editar_andY=None
c_x = 0
c_y = 0
#chip or datos
editar_orX=None
editar_orY=None
c_or_x=0
c_or_y=0
#chip not datos
editar_notX=None
editar_notY=None
c_not_x=0
c_not_y=0

# switch 4
c4_x = 0
c4_y = 0
nueva_resistencia = None
#display
dis_x=0
dis_y=0

x_proto = (screen.get_width() - 650) // 2
y_proto = (screen.get_height() - 300) // 2
protoboard = Protoboard(x_proto, y_proto, conectores)
pantalla_secundaria = True # Variable que permite intercalar entre la pantalla principal y secundaria
# Crear y dibujar Pila
x_pila = (screen.get_width() - 950) // 2
y_pila = (screen.get_height() - 50) // 2

# Crear conectores Pila + -
pila_mas = Conector("pila+", x_pila + 65, y_pila - 15, conectores)
pila_menos = Conector("pila-", x_pila + 35, y_pila - 15, conectores)
pila_mas.fase = True
pila_menos.neutro = True
conectores.append(pila_mas)
conectores.append(pila_menos)
pila = Pila(x_pila, y_pila)
motor=Motor(x_pila,y_pila+50)

conector = Conector("1", 0, 0, conectores)
font = pygame.font.Font(None, 24)  # Usa la fuente predeterminada con tamaño 24

while running:
    # Manejo de eventos de la pantalla
    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE or event.type == pygame.QUIT:
            running = False
        mm.manejar_eventos(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pantalla_secundaria = not pantalla_secundaria # cambio de estado de la variable continuamente    
        if not pantalla_secundaria:
            mm.pantalla_secundaria(screen)
        else:
            content_surface.fill("white")  # directo el color sin variables extra
            protoboard.crear(content_surface) # crear protoboard
            conector.dibujar(content_surface) # crear conectores de la protoboard
            pila.dibujarPila(content_surface) # dibujo de pila
            motor.div_boton(content_surface)
            mm.dibujar(content_surface,screen) # dibujar menu
            for i in guardar_led:
                i.led_apagada(content_surface)
            for i in guardar_switch:
                i.switch_proto(content_surface)
            for i in cables:
                i.dibujar_cables(content_surface)
            for i in guardar_switch16:
                i.dibujar(content_surface)
            for i in resistencias:
                i.dibujar_resistencia(content_surface)
            for i in guardar_chip:
                i.dibujar(content_surface)
                i.chip_and()
                texto = font.render("AND", True, (225,225,225))
                texto_escalado = pygame.transform.scale(texto, (texto.get_width() * 2, texto.get_height()))
                texto_rect = texto.get_rect(center=(i.x + i.largo // 2.5, i.y + i.ancho//1.5))
                content_surface.blit(texto_escalado, texto_rect)
            for i in guardar_chipOR:
                i.dibujar(content_surface)
                i.chip_or()
                texto = font.render("OR", True, (225, 225, 225))
                texto_escalado = pygame.transform.scale(texto, (texto.get_width() * 2, texto.get_height()))
                texto_rect = texto.get_rect(center=(i.x + i.largo // 2.5, i.y + i.ancho // 1.5))
                content_surface.blit(texto_escalado, texto_rect)
            for i in guardar_chipNOT:
                i.dibujar(content_surface)
                i.chip_not()
                texto = font.render("NOT", True, (225, 225, 225))
                texto_escalado = pygame.transform.scale(texto, (texto.get_width() * 2, texto.get_height()))
                texto_rect = texto.get_rect(center=(i.x + i.largo // 2.5, i.y + i.ancho // 1.5))
                content_surface.blit(texto_escalado, texto_rect)
            for i in guardar_display:
                i.dibujar(content_surface)
            
            keys = pygame.key.get_pressed()
    
            # Desplazamiento en ambas direcciones con límites
            if keys[pygame.K_UP] and scroll_y > 0:
                scroll_y -= scroll_speed
            if keys[pygame.K_DOWN] and scroll_y < extension_y - screen_height:
                scroll_y += scroll_speed
            if keys[pygame.K_LEFT] and scroll_x > 0:
                scroll_x -= scroll_speed
            if keys[pygame.K_RIGHT] and scroll_x < extension_x - screen_width:
                scroll_x += scroll_speed
            screen.blit(content_surface, (-scroll_x, -scroll_y))
            
        if event.type == VIDEORESIZE:
            if not fullscreen:
                if event.w > 1000 or event.h > 650:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                else:
                    screen = pygame.display.set_mode((1000, 650), pygame.RESIZABLE)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()  # Obtén la posición del mouse
            for switch4 in guardar_switch:
                switch4.detectar_click(mouse_pos)
            for switch16 in guardar_switch16:
                switch16.detectar_click(mouse_pos)
            mouse_pos = event.pos
            conector_cercano = punto_mas_cercano(mouse_pos, conectores)

            x, y = event.pos
            if mm.borrar_pulsado:  # Opciones para eliminar componentes
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
                elif mm.and_pulsado:
                    basurero.eliminar_chip_and(conector_cercano)
                elif mm.or_pulsado:
                    basurero.eliminar_chip_or(conector_cercano)
                elif mm.not_pulsado:
                    basurero.eliminar_chip_not(conector_cercano)
                elif mm.motor_pulsado:
                    basurero.eliminar_display(conector_cercano)
                conectores[0].padre = conectores[0]
                conectores[0].fase = True
                conectores[1].padre = conectores[1]
                conectores[1].neutro = True
            elif mm.editar_pulsado:  # Opciones para editar componentes
                if mm.led_pulsado:
                    if led_a_editar is None:
                        led_a_editar = buscar_led(x, y)
                    elif conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            conector_2_editar = conector_2_aux
                            led_a_editar.conector1 = conector_1_editar
                            led_a_editar.conector2 = conector_2_editar
                            led_a_editar.x = (conector_1_editar.x + conector_2_editar.x) // 2
                            led_a_editar.y = (conector_1_editar.y + conector_2_editar.y) // 2
                            led_a_editar = None
                            conector_1_editar = None
                            conector_2_editar = None
                            mm.led_pulsado = False
                            mm.color_led = (162, 206, 143)
                            mm.editar_pulsado = False
                            mm.color_editar = (162, 206, 143)
                    else:
                        print("error al editar led")
                elif mm.cable_pulsado:
                    if c_1_editar is None:
                        c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif c_2_editar is None:
                        c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_2_aux is not None and c_2_aux != c_1_editar:
                            c_2_editar = c_2_aux
                            cable_editar = buscar_cable(c_1_editar, c_2_editar)
                            if cable_editar is None:
                                c_1_editar = None
                                c_2_editar = None
                    elif (not cable_editar is None) and c_3_editar is None:
                        c_3_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_3_aux is not None and c_3_aux != c_1_editar and c_3_aux != c_2_editar:
                            c_3_editar = c_3_aux
                    elif (not cable_editar is None) and c_4_editar is None:
                        c_4_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_4_aux is not None and c_4_aux != c_1_editar and c_4_aux != c_2_editar and c_4_aux != c_3_editar:
                            c_4_editar = c_4_aux
                            # Asignar los conectores al cable
                            cable_editar.conector_inicio = c_3_editar
                            cable_editar.conector_fin = c_4_editar
                            # quitar la conexion anterior
                            c_1_editar.eliminar_conexion(c_1_editar, c_2_editar)  # los antiguos
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
                    if c_1_editar is None:
                        c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif c_2_editar is None:
                        c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_2_aux is not None and c_2_aux != c_1_editar:
                            c_2_editar = c_2_aux
                            cable_editar = buscar_resistencia(c_1_editar, c_2_editar)
                            if cable_editar is None:
                                c_1_editar = None
                                c_2_editar = None
                    elif (not cable_editar is None) and c_3_editar is None:
                        c_3_aux = punto_mas_cercano(mouse_pos, conectores)
                        if c_3_aux is not None and c_3_aux != c_1_editar and c_3_aux != c_2_editar:
                            c_3_editar = c_3_aux
                    elif (not cable_editar is None) and c_4_editar is None:
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
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            basurero.eliminar_switch(conector_1_editar)
                            c4_x = conector_2_aux.x
                            c4_y = conector_2_aux.y
                            if c4_x != 0 and c4_y != 0:
                                switch4 = Switch(conector_2_aux)
                                pines_superior = buscar_pin(c4_x, c4_y, 2, 60, 0)
                                switch4.pin2 = pines_superior[1]
                                pines_inferior = buscar_pin(c4_x, c4_y + 60, 2, 60, 0)
                                switch4.pin3 = pines_inferior[0]
                                switch4.pin4 = pines_inferior[1]
                                guardar_switch.append(switch4)
                                if (switch4.pin2.fase or switch4.pin2.neutro):
                                    switch4.bandera = 21
                                elif (switch4.pin4.fase or switch4.pin4.neutro):
                                    switch4.bandera = 4
                                switch4.pin1.agregar_conexion(switch4.pin2)
                                switch4.pin3.agregar_conexion(switch4.pin4)
                                c4_x, c4_y = 0, 0  # Resetear las coordenadas
                                mm.switch_pulsado = False
                                mm.color_switch = (162, 206, 143)
                                mm.boton_switch2_pulsado = False
                                mm.color_switch4 = (162, 206, 143)
                elif mm.boton_switch16_pulsado:
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
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
                                mm.editar_pulsado = False
                                mm.color_editar = (162, 206, 143)
                                conector_1_editar = None
                                conector_2_editar = None
                elif mm.and_pulsado:
                    if editar_andX is None:
                        editar_andX=punto_mas_cercano(mouse_pos,conectores)
                    elif editar_andY is None:
                        aux_andY=punto_mas_cercano(mouse_pos,conectores)
                        if aux_andY is not None and aux_andY != editar_andX:
                            basurero.eliminar_chip_and(editar_andX)
                            c_x = aux_andY.x
                            c_y = aux_andY.y
                            if c_y != 0 and c_y != 0:
                                chip = Chip(aux_andY)
                                pines_superior = buscar_pin(c_x, c_y, 7, 30, 0)
                                chip.pin2 = pines_superior[1]
                                chip.pin3 = pines_superior[2]
                                chip.pin4 = pines_superior[3]
                                chip.pin5 = pines_superior[4]
                                chip.pin6 = pines_superior[5]
                                chip.pin7 = pines_superior[6]
                                pines_inferior = buscar_pin(c_x, c_y + 30, 7, 30, 0)
                                chip.pin8 = pines_inferior[0]
                                chip.pin9 = pines_inferior[1]
                                chip.pin10 = pines_inferior[2]
                                chip.pin11 = pines_inferior[3]
                                chip.pin12 = pines_inferior[4]
                                chip.pin13 = pines_inferior[5]
                                chip.pin14 = pines_inferior[6]
                                guardar_chip.append(chip)
                                c_x, c_y = 0, 0  # Resetear las coordenadas
                                mm.chip_pulsado = False
                                mm.color_ship = (162, 206, 143)
                                mm.and_pulsado = False
                                mm.color_shipAND = (162, 206, 143)
                                editar_orX = None
                                editar_orY = None
                                aux_andY = None
                elif mm.or_pulsado:
                    if editar_orX is None:
                        editar_orX=punto_mas_cercano(mouse_pos,conectores)
                    elif editar_orY is None:
                        aux_or=punto_mas_cercano(mouse_pos,conectores)
                        if aux_or is not None and aux_or != editar_orX:
                            basurero.eliminar_chip_or(editar_orX)
                            c_or_x = aux_or.x
                            c_or_y = aux_or.y
                            if c_or_x != 0 and c_or_y != 0:
                                chip = Chip(aux_or)
                                pines_superior = buscar_pin(c_or_x, c_or_y, 7, 30, 0)
                                chip.pin2 = pines_superior[1]
                                chip.pin3 = pines_superior[2]
                                chip.pin4 = pines_superior[3]
                                chip.pin5 = pines_superior[4]
                                chip.pin6 = pines_superior[5]
                                chip.pin7 = pines_superior[6]
                                pines_inferior = buscar_pin(c_or_x, c_or_y + 30, 7, 30, 0)
                                chip.pin8 = pines_inferior[0]
                                chip.pin9 = pines_inferior[1]
                                chip.pin10 = pines_inferior[2]
                                chip.pin11 = pines_inferior[3]
                                chip.pin12 = pines_inferior[4]
                                chip.pin13 = pines_inferior[5]
                                chip.pin14 = pines_inferior[6]
                                guardar_chipOR.append(chip)
                                c_or_x, c_or_y = 0, 0  # Resetear las coordenadas
                                mm.chip_pulsado = False
                                mm.color_ship = (162, 206, 143)
                                mm.or_pulsado = False
                                mm.color_shipOR = (162, 206, 143)
                                editar_orX = None
                                editar_orY = None
                                aux_or = None
                elif mm.not_pulsado:
                    if editar_notX  is None:
                        editar_notX=punto_mas_cercano(mouse_pos,conectores)
                    elif editar_notY is None:
                        aux_not=punto_mas_cercano(mouse_pos,conectores)
                        if aux_not is not None and aux_not != editar_notX:
                            basurero.eliminar_chip_not(editar_notX)
                            c_not_x = aux_not.x
                            c_not_y = aux_not.y
                            if c_not_x != 0 and c_not_y != 0:
                                chip = Chip(aux_not)
                                pines_superior = buscar_pin(c_not_x, c_not_y, 7, 30, 0)
                                chip.pin2 = pines_superior[1]
                                chip.pin3 = pines_superior[2]
                                chip.pin4 = pines_superior[3]
                                chip.pin5 = pines_superior[4]
                                chip.pin6 = pines_superior[5]
                                chip.pin7 = pines_superior[6]
                                pines_inferior = buscar_pin(c_not_x, c_not_y + 30, 7, 30, 0)
                                chip.pin8 = pines_inferior[0]
                                chip.pin9 = pines_inferior[1]
                                chip.pin10 = pines_inferior[2]
                                chip.pin11 = pines_inferior[3]
                                chip.pin12 = pines_inferior[4]
                                chip.pin13 = pines_inferior[5]
                                chip.pin14 = pines_inferior[6]
                                guardar_chipNOT.append(chip)
                                c_not_x, c_not_y = 0, 0  # Resetear las coordenadas
                                mm.chip_pulsado = False
                                mm.color_ship = (162, 206, 143)
                                mm.not_pulsado = False
                                mm.color_shipNOT = (162, 206, 143)
                                editar_notX = None
                                editar_notY = None
                                aux_not = None

                elif mm.motor_pulsado:
                    if editar_notX  is None:
                        editar_notX=punto_mas_cercano(mouse_pos,conectores)
                    elif editar_notY is None:
                        aux_not = punto_mas_cercano(mouse_pos, conectores)
                        if aux_not is not None and aux_not != editar_notX:
                            basurero.eliminar_display(editar_notX)
                            dis_x = aux_not.x
                            dis_y = aux_not.y
                            if dis_x != 0 and dis_y != 0:
                                display = Display(conector_cercano)
                                pines_superior = buscar_pin(dis_x, dis_y, 5, 30, 0)
                                display.pin2 = pines_superior[1]
                                display.pin3 = pines_superior[2]
                                display.pin4 = pines_superior[3]
                                display.pin5 = pines_superior[4]
                                pines_inferior = buscar_pin(dis_x, dis_y + (30 * 5), 5, 30, 0)
                                display.pin6 = pines_inferior[0]
                                display.pin7 = pines_inferior[1]
                                display.pin8 = pines_inferior[2]
                                display.pin9 = pines_inferior[3]
                                display.pin10 = pines_inferior[4]
                                guardar_display.append(display)
                                dis_x, dis_y = 0, 0  # Resetear las coordenadas
                                editar_notX = None
                                editar_notY = None
                                aux_not = None
            elif mm.led_pulsado:
                if mm.led1_pulsado:
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            conector_2_editar = conector_2_aux
                            led_a = Led((165, 0, 0),(255, 0, 0), conector_1_editar, conector_2_editar)
                            guardar_led.append(led_a)
                            conector_1_editar = None
                            conector_2_editar = None
                            mm.led_pulsado = False
                            mm.color_led = (162, 206, 143)
                            mm.led1_pulsado = False
                            mm.color_led1 = (162, 206, 143)
                if mm.led2_pulsado:
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            conector_2_editar = conector_2_aux
                            led_a = Led((39, 150, 44),(0, 255, 12), conector_1_editar, conector_2_editar)
                            guardar_led.append(led_a)
                            conector_1_editar = None
                            conector_2_editar = None
                            mm.led_pulsado = False
                            mm.color_led = (162, 206, 143)
                            mm.led2_pulsado = False
                            mm.color_led2 = (162, 206, 143)
                if mm.led3_pulsado:
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            conector_2_editar = conector_2_aux
                            led_a = Led((236, 243, 91),(243, 255, 0 ), conector_1_editar, conector_2_editar)
                            guardar_led.append(led_a)
                            conector_1_editar = None
                            conector_2_editar = None
                            mm.led_pulsado = False
                            mm.color_led = (162, 206, 143)
                            mm.led3_pulsado = False
                            mm.color_led3 = (162, 206, 143)
                if mm.led4_pulsado:
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            conector_2_editar = conector_2_aux
                            led_a = Led((42, 49, 126 ),(0, 19, 255  ), conector_1_editar, conector_2_editar)
                            guardar_led.append(led_a)
                            conector_1_editar = None
                            conector_2_editar = None
                            mm.led_pulsado = False
                            mm.color_led = (162, 206, 143)
                            mm.led4_pulsado = False
                            mm.color_led4 = (162, 206, 143)
                if mm.led5_pulsado:
                    if conector_1_editar is None:
                        conector_1_editar = punto_mas_cercano(mouse_pos, conectores)
                    elif conector_2_editar is None:
                        conector_2_aux = punto_mas_cercano(mouse_pos, conectores)
                        if conector_2_aux is not None and conector_2_aux != conector_1_editar:
                            conector_2_editar = conector_2_aux
                            led_a = Led((134, 62, 156),(197, 0, 255), conector_1_editar, conector_2_editar)
                            guardar_led.append(led_a)
                            conector_1_editar = None
                            conector_2_editar = None
                            mm.led_pulsado = False
                            mm.color_led = (162, 206, 143)
                            mm.led5_pulsado = False
                            mm.color_led5 = (162, 206, 143)
            elif mm.switch_pulsado:
                if mm.boton_switch16_pulsado:
                    if not conector_cercano:
                        pass
                    elif c16_1 == 0:
                        c16_1 = conector_cercano.x
                        c16_2 = conector_cercano.y
                        if c16_1 != 0 and c16_2 != 0:
                            switch16 = Switch_16(conector_cercano)
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
                if mm.boton_switch2_pulsado:
                    if not conector_cercano:
                        pass
                    elif c4_x == 0:
                        c4_x = conector_cercano.x
                        c4_y = conector_cercano.y
                        if c4_x != 0 and c4_y != 0:
                            switch4 = Switch(conector_cercano)
                            pines_superior = buscar_pin(c4_x, c4_y, 2, 60, 0)
                            switch4.pin2 = pines_superior[1]
                            pines_inferior = buscar_pin(c4_x, c4_y+60, 2, 60, 0)
                            switch4.pin3 = pines_inferior[0]
                            switch4.pin4 = pines_inferior[1]
                            guardar_switch.append(switch4)
                            if (switch4.pin2.fase or switch4.pin2.neutro):
                                switch4.bandera=21
                            elif (switch4.pin4.fase or switch4.pin4.neutro):
                                switch4.bandera = 4
                            switch4.pin1.agregar_conexion(switch4.pin2)
                            switch4.pin3.agregar_conexion(switch4.pin4)
                            c4_x, c4_y = 0, 0  # Resetear las coordenadas
                            mm.switch_pulsado = False
                            mm.color_switch = (162, 206, 143)
                            mm.boton_switch2_pulsado = False
                            mm.color_switch4 = (162, 206, 143)

            elif mm.chip_pulsado:
                if mm.and_pulsado:
                    if not conector_cercano:
                        pass
                    elif c_x == 0:
                        c_x = conector_cercano.x
                        c_y = conector_cercano.y
                        if c_x != 0 and c_y != 0:
                            chip = Chip(conector_cercano)
                            pines_superior = buscar_pin(c_x, c_y, 7, 30, 0)
                            chip.pin2 = pines_superior[1]
                            chip.pin3 = pines_superior[2]
                            chip.pin4 = pines_superior[3]
                            chip.pin5 = pines_superior[4]
                            chip.pin6 = pines_superior[5]
                            chip.pin7 = pines_superior[6]
                            pines_inferior = buscar_pin(c_x, c_y + 30, 7, 30, 0)
                            chip.pin8 = pines_inferior[0]
                            chip.pin9 = pines_inferior[1]
                            chip.pin10 = pines_inferior[2]
                            chip.pin11 = pines_inferior[3]
                            chip.pin12 = pines_inferior[4]
                            chip.pin13 = pines_inferior[5]
                            chip.pin14 = pines_inferior[6]
                            guardar_chip.append(chip)
                            c_x, c_y = 0, 0  # Resetear las coordenadas
                            mm.chip_pulsado = False
                            mm.color_ship = (162, 206, 143)
                            mm.and_pulsado = False
                            mm.color_shipAND = (162, 206, 143)
                if mm.or_pulsado:
                    if not conector_cercano:
                        pass
                    elif c_or_x == 0:
                        c_or_x = conector_cercano.x
                        c_or_y = conector_cercano.y
                        if c_or_x != 0 and c_or_y != 0:
                            chip = Chip(conector_cercano)
                            pines_superior = buscar_pin(c_or_x, c_or_y, 7, 30, 0)
                            chip.pin2 = pines_superior[1]
                            chip.pin3 = pines_superior[2]
                            chip.pin4 = pines_superior[3]
                            chip.pin5 = pines_superior[4]
                            chip.pin6 = pines_superior[5]
                            chip.pin7 = pines_superior[6]
                            pines_inferior = buscar_pin(c_or_x, c_or_y + 30, 7, 30, 0)
                            chip.pin8 = pines_inferior[0]
                            chip.pin9 = pines_inferior[1]
                            chip.pin10 = pines_inferior[2]
                            chip.pin11 = pines_inferior[3]
                            chip.pin12 = pines_inferior[4]
                            chip.pin13 = pines_inferior[5]
                            chip.pin14 = pines_inferior[6]
                            guardar_chipOR.append(chip)
                            c_or_x, c_or_y = 0, 0  # Resetear las coordenadas
                            mm.chip_pulsado = False
                            mm.color_ship = (162, 206, 143)
                            mm.or_pulsado = False
                            mm.color_shipOR = (162, 206, 143)
                if mm.not_pulsado:
                    if not conector_cercano:
                        pass
                    elif c_not_x == 0:
                        c_not_x = conector_cercano.x
                        c_not_y = conector_cercano.y
                        if c_not_x != 0 and c_not_y != 0:
                            chip = Chip(conector_cercano)
                            pines_superior = buscar_pin(c_not_x, c_not_y, 7, 30, 0)
                            chip.pin2 = pines_superior[1]
                            chip.pin3 = pines_superior[2]
                            chip.pin4 = pines_superior[3]
                            chip.pin5 = pines_superior[4]
                            chip.pin6 = pines_superior[5]
                            chip.pin7 = pines_superior[6]
                            pines_inferior = buscar_pin(c_not_x, c_not_y + 30, 7, 30, 0)
                            chip.pin8 = pines_inferior[0]
                            chip.pin9 = pines_inferior[1]
                            chip.pin10 = pines_inferior[2]
                            chip.pin11 = pines_inferior[3]
                            chip.pin12 = pines_inferior[4]
                            chip.pin13 = pines_inferior[5]
                            chip.pin14 = pines_inferior[6]
                            guardar_chipNOT.append(chip)
                            c_not_x, c_not_y = 0, 0  # Resetear las coordenadas
                            mm.chip_pulsado = False
                            mm.color_ship = (162, 206, 143)
                            mm.not_pulsado = False
                            mm.color_shipNOT = (162, 206, 143)

            elif mm.cable_pulsado:
                if c_1_editar is None:
                    c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                elif c_2_editar is None:
                    c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                    if c_2_aux is not None and c_2_aux != c_1_editar:
                        c_2_editar = c_2_aux
                        nuevo_cable = Cableado(c_1_editar, c_2_editar)
                        if c_1_editar.fase or c_1_editar.neutro:
                            nuevo_cable.bandera=1
                        else:
                            nuevo_cable.bandera=2
                        if nuevo_cable.validar_cable(cables):
                            cables.append(nuevo_cable)
                            cables_coordenadas.append(c_1_editar)
                            cables_coordenadas.append(c_2_editar)
                            nuevo_cable.conector_inicio.agregar_conexion(nuevo_cable.conector_fin)
                        nuevo_cable = None
                        c_1_editar = None
                        c_2_editar = None
                    else:
                        print("conector 2 no válido, es igual al conector 1")

            elif mm.res_pulsado:
                if c_1_editar is None:
                    c_1_editar = punto_mas_cercano(mouse_pos, conectores)
                elif c_2_editar is None:
                    c_2_aux = punto_mas_cercano(mouse_pos, conectores)
                    if c_2_aux is not None and c_2_aux != c_1_editar:
                        c_2_editar = c_2_aux
                        nueva_resistencia = Resistencia(c_1_editar, c_2_editar)
                        if c_1_editar.fase or c_1_editar.neutro:
                            nueva_resistencia.bandera=1
                        else:
                            nueva_resistencia.bandera=2
                        if nueva_resistencia.validar_resistencia(resistencias):
                            resistencias.append(nueva_resistencia)
                            resistencias_coordenadas.append(c_1_editar)
                            resistencias_coordenadas.append(c_2_editar)
                            nueva_resistencia.conector_inicio.agregar_conexion(nueva_resistencia.conector_fin)
                        nueva_resistencia = None
                        c_1_editar = None
                        c_2_editar = None
                    else:
                        print("conector 2 no válido, es igual al conector 1")

            elif mm.motor_pulsado:
                if not conector_cercano:
                    pass
                elif dis_x == 0:
                    dis_x = conector_cercano.x
                    dis_y = conector_cercano.y
                    if dis_x != 0 and dis_y != 0:
                        display = Display(conector_cercano)
                        pines_superior = buscar_pin(dis_x, dis_y, 5, 30, 0)
                        display.pin2 = pines_superior[1]
                        display.pin3 = pines_superior[2]
                        display.pin4 = pines_superior[3]
                        display.pin5 = pines_superior[4]
                        pines_inferior = buscar_pin(dis_x, dis_y + (30*5), 5, 30, 0)
                        display.pin6 = pines_inferior[0]
                        display.pin7 = pines_inferior[1]
                        display.pin8 = pines_inferior[2]
                        display.pin9 = pines_inferior[3]
                        display.pin10 = pines_inferior[4]
                        guardar_display.append(display)
                        dis_x, dis_y = 0, 0  # Resetear las coordenadas

            elif motor.verificar_click(event.pos):
                print("Botón presionado, el color cambió.")
                if motor.estado_boton:
                    for c in conectores:
                        if not c.nombre.startswith("pila"):
                            c.fase = None
                            c.neutro = None
                else:
                    for c in conectores:
                        c.fase = c.padre.fase
                        c.neutro = c.padre.neutro

    if not mm.editar_pulsado and not mm.res_pulsado:
        cableado.dibujar_cable_actual(screen, c_1_editar)
    elif not mm.editar_pulsado and not mm.cable_pulsado:
        resistencia.dibujar_resistencia_actual(screen, c_1_editar)
    pygame.display.flip()
    mainClock.tick(30)
pygame.quit()