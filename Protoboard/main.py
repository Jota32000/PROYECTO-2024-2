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

def switch_presionado(switch, mouse_pos):
    lado = 20  # Tamaño del switch (cuadrado)
    x, y = mouse_pos
    if switch.x <= x <= switch.x + lado and switch.y <= y <= switch.y + lado:
        return True
    return False
#Main
pygame.init()
# --------- esto lo tengo que trabajar para fullscreen ----------------
# Obtener el tamaño de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Crear la ventana con el tamaño ajustado
screen = pygame.display.set_mode((1000,650),pygame.RESIZABLE)

pygame.display.set_caption("Protoboard")
mainClock = pygame.time.Clock()

#Crear el cableado
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

ultimo_conector= None

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

    screen.fill("white") # directo el color sin variables extra

    # Crear y dibujar Protoboard
    protoboard.crear(screen,conectores)

    pila.dibujarPila(screen)

    menu.dibujar(screen)

    # Crear funcionalidad de basurero

    clock = pygame.time.Clock()

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
        if event.type == VIDEORESIZE:
            if not fullscreen:
                if event.w > 1000 or event.h > 650:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                else:
                    screen = pygame.display.set_mode((1000, 650), pygame.RESIZABLE)

        # Manejo de eventos especial para que cuando se quiera eliminar un item, se elimine bien y no se quiera agregar un cable
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu.boton_basurero:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                basurero.eliminar_cable(mouse_x, mouse_y,conectores,cables)
                if verificador == False:
                    basurero.eliminar_led(mouse_x, mouse_y,guardar_led)
                    basurero.eliminar_switch(mouse_x, mouse_y,guardar_switch)
                    basurero.eliminar_resistencia(mouse_x, mouse_y,conectores,resistencias)
                verificador = False
                menu.boton_basurero = False

        # Manejo de eventos normal para cables, led y switch
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu.boton_basurero == False:
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
            x, y = event.pos

            if menu.boton_led:
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

                        tupla1 = (x1,y1)
                        tupla2 = (x2, y2)
                        led_coordenadas.append(tupla1)
                        led_coordenadas.append(tupla2)
                        x_mitad, y_mitad = ((x1 + x2) / 2, (y1 + y2) / 2)
                        c_apagada = (110, 0, 0)  # Color rojo oscuro para apagado
                        name_inicio = None
                        name_fin = None
                        for c in conectores:
                            if c.x == x1 and c.y == y1:
                                name_inicio = c.nombre
                            elif c.x == x2 and c.y == y2:
                                name_fin = c.nombre

                        led_a = Led(c_apagada, x_mitad, y_mitad, x1, x2, y1, y2,name_inicio, name_fin)
                        # Dibujar el LED
                        led_a.led_apagada(screen,conectores)
                        # Restablecer variables
                        x1, x2, y1, y2 = 0, 0, 0, 0
                        menu.boton_led = False
                        guardar_led.append(led_a)

            elif menu.boton_switch:
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

                        name_inicio = None
                        name_fin = None
                        for c in conectores:
                            if c.x == x1 and c.y == y1:
                                name_inicio = c.nombre
                            elif c.x == x2 and c.y == y2:
                                name_fin = c.nombre
                        switch_a = Switch(x_mitad, y_mitad, x1, x2, y1, y2,name_inicio,name_fin)
                        switch_a.switch_proto(screen,conectores)
                        x1, x2, y1, y2 = 0, 0, 0, 0
                        menu.boton_switch = False
                        guardar_switch.append(switch_a)

            elif conector_cercano and menu.boton_cable:
                for conector in conectores:
                    if conector_cercano == conector:
                        if not cableado.dibujando_cable:
                            cableado.comienzo_cable(conector)
                        else:
                            cableado.finalizar_cable(conector,conectores,cables)
                            ultimo_conector = conector_cercano
                            menu.boton_cable = False

            elif conector_cercano and menu.boton_cable == False and menu.boton_edicion == False and menu.boton_basurero == False:
                for conector in conectores:
                    if conector_cercano == conector:
                        if not resistencia.dibujando_resistencia:
                            resistencia.comienzo_resistencia(conector)
                        else:
                            resistencia.finalizar_resistencia(conector,conectores,resistencias)
                            ultimo_conector = conector_cercano
                 
            elif menu.boton_edicion:
                i = 0
                rango_click = 10
                mouse_pos = pygame.mouse.get_pos()
                conector_cercano = punto_mas_cercano(mouse_pos, conectores) #obtencion de punto cercano
                if conector_cercano == None:
                    pass
                else:
                    edicion_coordenadas.append(conector_cercano)

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
                            start.eliminar_conexion(start, end) #bien
                            if start.nombre.startswith(("conector1_", "conector2_")):
                                 for nodo in conectores:
                                    if nodo.y == start.y:
                                        nodo.eliminar_conexion(nodo, start)
                            # -------------------- elimina columnas ------------------------
                            else:
                                #print("--------------------------------")
                                cont=0
                                for nodo in conectores:
                                    if nodo.x == end.x: # No tocar (end.x)
                                        if start.nombre.startswith("conector3_"): 
                                            cont+=1
                                            nodo.eliminar_conexion(nodo, start)
                                        elif start.nombre.startswith("conector4_"):
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
                        menu.boton_edicion = False
                       
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
                        menu.boton_edicion = False
                    
                while i < len(led_coordenadas)  and len(edicion_coordenadas) > 0:
                    if led_coordenadas[i][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and led_coordenadas[i][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y: 
                        #print("entró en el origen del LED")
                        x = edicion_coordenadas[len(edicion_coordenadas) - 2].x #coordenada x que el usuario escogio para cambiar
                        y = edicion_coordenadas[len(edicion_coordenadas) - 2].y #coordenada y que el usuario escogio para cambiar
                        x_origen = led_coordenadas[i][0] # inicio led
                        y_origen = led_coordenadas[i][1]
                        x_destino = led_coordenadas[i+1][0] # fin led
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

                            name_inicio = None
                            name_fin = None

                            for c in conectores:
                                if x == c.x and y == c.y:
                                    name_inicio = c.nombre

                                if x_destino == c.x and y_destino == c.y:
                                    name_fin = c.nombre

                            # Cambiar color del LED según si ambos conectores tienen corriente
                            if corriente_conector1 and corriente_conector2:
                                led_a = Led(c_encendida, x_mitad, y_mitad, x, x_destino, y, y_destino,name_inicio,name_fin)
                            else:
                                led_a = Led(c_apagada, x_mitad, y_mitad, x, x_destino, y, y_destino,name_inicio,name_fin)
                            led_a.led_apagada(screen) # Dibujar el LED
                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0 # Restablecer variables
                            edicion_coordenadas.clear() # Limpieza de lista edicion coordenadas
                            guardar_led.insert(i, led_a) # Insertar directamente el LED en la posición original
                            led_coordenadas[i] = x,y
                            menu.boton_edicion = False
                            break

                    elif led_coordenadas[i+1][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and led_coordenadas[i+1][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y: 
                        #print("Entró en el destino del LED")
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

                            name_inicio = None
                            name_fin = None

                            for c in conectores:
                                if x == c.x and y == c.y:
                                    name_fin = c.nombre
                                if x_origen == c.x and y_origen == c.y:
                                    name_inicio = c.nombre


                            # Cambiar color del LED según si ambos conectores tienen corriente
                            if corriente_conector1 and corriente_conector2:
                                led_a = Led(c_encendida, x_mitad, y_mitad, x_origen, x, y_origen, y,name_inicio,name_fin)
                            else:
                                led_a = Led(c_apagada, x_mitad, y_mitad, x_origen, x, y_origen, y,name_inicio,name_fin)

                            # Dibujar el LED
                            led_a.led_apagada(screen,conectores)
                            # Restablecer variables
                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0
                            edicion_coordenadas.clear()
                            guardar_led.insert(i, led_a) # Inserta directamente en la posicion correspondiente las nuevas coordenadas
                            led_coordenadas[i+1] = x,y # Actualiza las coordenadas en la lista de las posiciones de cada led
                            menu.boton_edicion = False
                            break
                    i+=2
                i = 0

                while i < len(switch_coordenadas) and len(edicion_coordenadas) > 0:
                    if switch_coordenadas[i][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and switch_coordenadas[i][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y:
                        #print("Entró en el origen del switch")
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

                            name_inicio = None
                            name_fin = None

                            for c in conectores:
                                if x == c.x and y == c.y:
                                    name_inicio = c.nombre
                                if x_destino == c.x and y_destino == c.y:
                                    name_fin = c.nombre
                            switch_a = Switch(x_mitad, y_mitad, x, x_destino, y, y_destino,name_inicio,name_fin) # Dibujar el switch
                            switch_a.switch_proto(screen)

                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0
                            edicion_coordenadas.clear() # Limpieza de lista edicion coordenadas
                            guardar_switch.insert(i, switch_a) # Insertar directamente el switch en la posición original
                            switch_coordenadas[i] = (x,y) # Actualiza las coordenadas en la lista de las posiciones de cada switch
                            menu.boton_edicion = False
                            break

                    elif switch_coordenadas[i+1][0] == edicion_coordenadas[len(edicion_coordenadas) - 1].x and switch_coordenadas[i+1][1] == edicion_coordenadas[len(edicion_coordenadas) - 1].y:   
                        #print("Entró en el destino del switch")
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
                            name_inicio = None
                            name_fin = None

                            for c in conectores:
                                if x == c.x and y == c.y:
                                    name_fin = c.nombre
                                if x_origen == c.x and y_origen == c.y:
                                    name_inicio = c.nombre
                            switch_a = Switch(x_mitad, y_mitad, x_origen, x, y_origen, y,name_inicio,name_fin) # Dibujar el switch
                            switch_a.switch_proto(screen,conectores)

                            x_origen, x_destino, y_origen, y_destino = 0, 0, 0, 0
                            edicion_coordenadas.clear() # Limpieza de lista edicion coordenadas
                            guardar_switch.insert(i, switch_a) # Insertar directamente el switch en la posición original
                            switch_coordenadas[i+1] = (x,y) # Actualiza las coordenadas en la lista de las posiciones de cada switch
                            menu.boton_edicion = False
                            break
                    i+=2

        #Manejo de evento del menú
        menu.manejar_eventos(event)
    cableado.dibujar_cable_actual(screen,conectores)
    resistencia.dibujar_resistencia_actual(screen)

    # Opcion de menú escogida según usuario

    if menu.boton_cable:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 20,y_menu + 15)
        menu.dib_cable(screen, x_menu + 95, y_menu - 15)    
    
    elif menu.boton_led:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 145,y_menu + 15)
        menu.dib_led(screen, x_menu + 170, y_menu + 35)
                
    elif menu.boton_switch:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 270,y_menu + 15)
        menu.dib_switch(screen, x_menu + 300, y_menu + 40)     
        
    elif menu.boton_edicion:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 395,y_menu + 15)         
        menu.dib_editor(screen, x_menu + 420, y_menu + 25)

    elif menu.boton_basurero:
        menu.dibujar_recuadro_escogido(screen,100,x_menu + 520,y_menu + 15)     
        menu.dib_basurero(screen, x_menu + 535, y_menu + 30)

    pygame.display.flip()
    mainClock.tick(30)

pygame.quit()
#se guardo
