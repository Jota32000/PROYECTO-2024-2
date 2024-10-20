class Basurero:
    def __init__(self,guardar_led,guardar_switch,conectores,cables,resistencias,cables_coordenadas,resistencias_coordenadas):
        self.guardar_led=guardar_led
        self.guardar_switch=guardar_switch
        self.conectores=conectores
        self.cables=cables
        self.resistencias=resistencias
        self.cables_coordenadas=cables_coordenadas
        self.resistencias_coordenadas=resistencias_coordenadas
    
    def eliminar_led(self,conector_cercano):
        #Buscador de led en la lista de los leds
        for led in self.guardar_led:
            conector_inicio = led.conector1
            conector_fin = led.conector2
            if conector_cercano == conector_inicio or conector_cercano == conector_fin:
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
        for cable in self.cables:
            # ahora el extremo del nodo que presionas es donde se elimina
            conector_inicio = cable.conector_inicio
            conector_fin = cable.conector_fin

            if conector_cercano == conector_inicio:
                if conector_inicio.nombre.startswith("pila"):
                    conector_fin.eliminar_conexion(conector_fin, conector_inicio)
                else:
                    conector_inicio.eliminar_conexion(conector_inicio,conector_fin)
                self.cables.remove(cable)

            elif conector_cercano == conector_fin:
                if conector_fin.nombre.startswith("pila"):
                    conector_inicio.eliminar_conexion(conector_inicio, conector_fin)
                else:
                    conector_fin.eliminar_conexion(conector_fin,conector_inicio)
                self.cables.remove(cable)



    def eliminar_resistencia(self,conector_cercano):
        # la resistencia sigue la misma logica
        for resistencia in self.resistencias:
            conector_inicio = resistencia.conector_inicio
            conector_fin = resistencia.conector_fin
            if conector_cercano == conector_inicio:
                if conector_inicio.nombre.startswith("pila"):
                    conector_fin.eliminar_conexion(conector_fin, conector_inicio)
                else:
                    conector_inicio.eliminar_conexion(conector_inicio, conector_fin)
                self.resistencias.remove(resistencia)
            elif conector_cercano == conector_fin:
                if conector_fin.nombre.startswith("pila"):
                    conector_inicio.eliminar_conexion(conector_inicio, conector_fin)
                else:
                    conector_fin.eliminar_conexion(conector_fin, conector_inicio)
                self.resistencias.remove(resistencia)
