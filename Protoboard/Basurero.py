class Basurero:
    def __init__(self,guardar_led,guardar_switch,conectores,cables,resistencias,cables_coordenadas,resistencias_coordenadas):
        self.guardar_led=guardar_led
        self.guardar_switch=guardar_switch
        self.conectores=conectores
        self.cables=cables
        self.resistencias=resistencias
        self.cables_coordenadas=cables_coordenadas
        self.resistencias_coordenadas=resistencias_coordenadas
    
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
        conector_1 = None
        conector_2 = None
        for cable in range (len(self.cables_coordenadas)):
            if conector_cercano == self.cables_coordenadas[cable]:
                if cable % 2 == 0:
                    indice = cable // 2
                else:
                    indice = (cable - 1) // 2
                self.cables.pop(indice)
                conector_1 = (self.cables_coordenadas[cable])
                conector_2 = (self.cables_coordenadas[cable - 1])
                self.cables_coordenadas.pop(cable)
                self.cables_coordenadas.pop(cable - 1)
                break
        if conector_1 != None or conector_2 != None: # elimina la conexión entre conector_1 y conector_2
            conector_1.eliminar_conexion(conector_1, conector_2)

    def eliminar_resistencia(self,conector_cercano):
        #Buscador de cable en la lista de las resistencias
        conector_1 = None
        conector_2 = None
        for resistencia in range (len(self.resistencias_coordenadas)):
            if conector_cercano == self.resistencias_coordenadas[resistencia]:
                if resistencia % 2 == 0:
                    indice = resistencia // 2
                else:
                    indice = (resistencia - 1) // 2
                self.resistencias.pop(indice)
                conector_1 = (self.resistencias_coordenadas[resistencia])
                conector_2 = (self.resistencias_coordenadas[resistencia - 1])
                self.resistencias_coordenadas.pop(resistencia)
                self.resistencias_coordenadas.pop(resistencia - 1)
                break
        if conector_1 != None or conector_2 != None: # elimina la conexión entre conector_1 y conector_2
            conector_1.eliminar_conexion(conector_1, conector_2)