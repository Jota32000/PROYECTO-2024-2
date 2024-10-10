import pygame

from Datos import *

class Basurero:
    def __init__(self):
        #No presenta atributos
        pass
    def eliminar_led(self,x,y,guardar_led):
        rango_click = 10
        global verificador
        #Buscador de led en la lista de los leds
        for led in guardar_led:
            #si se clickea en el rango correspondiente, se borra de la lista led
            if led.x - rango_click <= x <= led.x + rango_click and led.y - rango_click <= y <= led.y + rango_click:
                guardar_led.remove(led)
            verificador = True
    def eliminar_switch(self,x,y,guardar_switch):
        rango_click = 20
        global verificador
        #Buscador de led en la lista de los switchs
        for switch in guardar_switch:
            #si se clickea en el rango correspondiente, se borra de la lista switch
            if switch.x - rango_click <= x <= switch.x + rango_click and switch.y - rango_click <= y <= switch.y + rango_click:
                guardar_switch.remove(switch)
            verificador = True
    def eliminar_cable(self,x,y,conectores,cables):
        rango_click = 10
        global verificador
        #Buscador de cable en la lista de los cables
        for cable in cables:
            #si se clickea en el rango correspondiente, se borra de la lista cable
            if cable[0].x - rango_click <= x <= cable[0].x + rango_click and cable[0].y - rango_click <= y <= cable[0].y + rango_click:
                start = cable[1]
                end = cable[0]
                cables.remove(cable)
                #print("Click en el origen del cable")

                if start and end:

                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

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
                verificador = True

            elif cable[1].x - rango_click <= x <= cable[1].x + rango_click and cable[1].y - rango_click <= y <= cable[1].y + rango_click:
                start = cable[1]
                end = cable[0]
                cables.remove(cable)
                #print("Click en el destino del cable")

                if start and end:
                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

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
                verificador = True
    def eliminar_resistencia(self,x,y,conectores,resistencias):
        rango_click = 10
        global verificador
        #Buscador de resistencia en la lista de las resistencias
        for resistencia in resistencias:
            #si se clickea en el rango correspondiente, se borra de la lista resistencia
            if resistencia[0].x - rango_click <= x <= resistencia[0].x + rango_click and resistencia[0].y - rango_click <= y <= resistencia[0].y + rango_click:
                start = resistencia[1]
                end = resistencia[0]
                resistencias.remove(resistencia)
                print("Click en el origen de la resistencia")

                if start and end:
                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

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
                verificador = True

            elif resistencia[1].x - rango_click <= x <= resistencia[1].x + rango_click and resistencia[1].y - rango_click <= y <= resistencia[1].y + rango_click:
                start = resistencia[1]
                end = resistencia[0]
                resistencias.remove(resistencia)
                print("Click en el destino de la resistencia")

                if start and end:
                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

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
                verificador = True