import pygame
class Basurero:
    def __init__(self,guardar_led,guardar_switch,conectores,cables,resistencias,cables_coordenadas):
        self.guardar_led=guardar_led
        self.guardar_switch=guardar_switch
        self.conectores=conectores
        self.cables=cables
        self.resistencias=resistencias
        self.cables_coordenadas=cables_coordenadas

    def eliminar_led(self,x,y):
        rango_click = 10
        #Buscador de led en la lista de los leds
        for led in self.guardar_led:
            #si se clickea en el rango correspondiente, se borra de la lista led
            if led.x - rango_click <= x <= led.x + rango_click and led.y - rango_click <= y <= led.y + rango_click:
                self.guardar_led.remove(led)

    def eliminar_switch(self,x,y):
        rango_click = 20
        #Buscador de led en la lista de los switchs
        for switch in self.guardar_switch:
            #si se clickea en el rango correspondiente, se borra de la lista switch
            if switch.x - rango_click <= x <= switch.x + rango_click and switch.y - rango_click <= y <= switch.y + rango_click:
                self.guardar_switch.remove(switch)

    def eliminar_cable(self,conector_cercano):
        #Buscador de cable en la lista de los cables
        for cable in range (len(self.cables_coordenadas)):
            if conector_cercano == self.cables_coordenadas[cable]:
                print("se encontro :)")
                print("esta en este indice: ",cable)
                if cable % 2 == 0:
                    indice = cable // 2
                    print("valor indice: ",indice)
                    self.cables.pop(indice)
                    self.cables_coordenadas.pop(cable)
                    self.cables_coordenadas.pop(cable - 1)
                    break
                else:
                    indice = (cable - 1) // 2
                    print("valor indice: ",indice)
                    self.cables.pop(indice)
                    self.cables_coordenadas.pop(cable)
                    self.cables_coordenadas.pop(cable - 1)
                    break
        print("nuevo listado de cables: ",self.cables)
        print("nuevo listado de coordenadas de cables: ",self.cables_coordenadas)


    def eliminar_resistencia(self,x,y):
        rango_click = 10

        #Buscador de resistencia en la lista de las resistencias
        for resistencia in self.resistencias:
            #si se clickea en el rango correspondiente, se borra de la lista resistencia
            if resistencia[0].x - rango_click <= x <= resistencia[0].x + rango_click and resistencia[0].y - rango_click <= y <= resistencia[0].y + rango_click:
                start = resistencia[1]
                end = resistencia[0]
                self.resistencias.remove(resistencia)
                print("Click en el origen de la resistencia")

                if start and end:
                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

                    # elimina conexiones en filas y columnas
                    if start.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in self.conectores:
                            if nodo.y == start.y:
                                nodo.eliminar_conexion(nodo, end)
                                end.eliminar_conexion(end, nodo)

                    elif start.nombre.startswith(("conector3_", "conector4_")):
                        for nodo in self.conectores:
                            if nodo.x == start.x:
                                nodo.eliminar_conexion(nodo, end)
                                end.eliminar_conexion(end, nodo)

                    # lo mismo para end
                    if end.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in self.conectores:
                            if nodo.y == end.y:
                                nodo.eliminar_conexion(nodo, start)
                                start.eliminar_conexion(start, nodo)

                    elif end.nombre.startswith(("conector3_", "conector4_")):
                        for nodo in self.conectores:
                            if nodo.x == end.x:
                                nodo.eliminar_conexion(nodo, start)
                                start.eliminar_conexion(start, nodo)

            elif resistencia[1].x - rango_click <= x <= resistencia[1].x + rango_click and resistencia[1].y - rango_click <= y <= resistencia[1].y + rango_click:
                start = resistencia[1]
                end = resistencia[0]
                self.resistencias.remove(resistencia)
                print("Click en el destino de la resistencia")

                if start and end:
                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

                    # elimina conexiones en filas y columnas
                    if start.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in self.conectores:
                            if nodo.y == start.y:
                                nodo.eliminar_conexion(nodo, end)
                                end.eliminar_conexion(end, nodo)

                    elif start.nombre.startswith(("conector3_", "conector4_")):
                        for nodo in self.conectores:
                            if nodo.x == start.x:
                                nodo.eliminar_conexion(nodo, end)
                                end.eliminar_conexion(end, nodo)

                    # lo mismo para end
                    if end.nombre.startswith(("conector1_", "conector2_")):
                        for nodo in self.conectores:
                            if nodo.y == end.y:
                                nodo.eliminar_conexion(nodo, start)
                                start.eliminar_conexion(start, nodo)

                    elif end.nombre.startswith(("conector3_", "conector4_")):
                        for nodo in self.conectores:
                            if nodo.x == end.x:
                                nodo.eliminar_conexion(nodo, start)
                                start.eliminar_conexion(start, nodo)