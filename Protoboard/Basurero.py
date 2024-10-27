class Basurero:
    def __init__(self,guardar_led,guardar_switch,conectores,cables,resistencias,guardar_switch16,guardar_chip_and,guardar_chip_or,guardar_chip_not):
        self.guardar_led=guardar_led
        self.guardar_switch=guardar_switch
        self.conectores=conectores
        self.cables=cables
        self.resistencias=resistencias
        self.guardar_switch16=guardar_switch16
        self.guardar_chip_and=guardar_chip_and
        self.guardar_chip_or=guardar_chip_or
        self.guardar_chip_not=guardar_chip_not

    def eliminar_led(self,conector_cercano):
        #Buscador de led en la lista de los leds
        for led in self.guardar_led:
            conector_inicio = led.conector1
            conector_fin = led.conector2
            if conector_cercano == conector_inicio or conector_cercano == conector_fin:
                self.guardar_led.remove(led)
    def eliminar_switch(self,conector):
        #Buscador de led en la lista de los switchs
        for switch in self.guardar_switch:
            #si se clickea en el rango correspondiente, se borra de la lista switch
            if conector == switch.pin1:
                a, b = switch.pines2(0)  # Llama a pines2 para desconectar
                if a is not None and b is not None:
                    if switch.bandera == 2:
                        b.eliminar_conexion(b, a)
                    else:
                        a.eliminar_conexion(a, b)
                self.guardar_switch.remove(switch)
                print("Switch removida con éxito")
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
    def eliminar_switch16(self,conector):
        #Buscador de led en la lista de los switchs 16
        for switch in self.guardar_switch16:
            #si se clickea en el rango correspondiente, se borra de la lista switch16
            if conector == switch.pin1:
                a, b = switch.pines2(0)  # Llama a pines2 para desconectar
                if a is not None and b is not None:
                    if switch.bandera == 2:
                        b.eliminar_conexion(b, a)
                    else:
                        a.eliminar_conexion(a, b)
                self.guardar_switch16.remove(switch)
    def eliminar_chip_and(self,conector):
        for chip in self.guardar_chip_and:
            if conector is not None:
               if (chip.x,chip.y) == (conector.x,conector.y):
                   self.guardar_chip_and.remove(chip)
    def eliminar_chip_or(self,conector):
        for chip in self.guardar_chip_or:
            if conector is not None:
               if (chip.x,chip.y) == (conector.x,conector.y):
                   self.guardar_chip_or.remove(chip)
    def eliminar_chip_not(self,conector):
        for chip in self.guardar_chip_not:
            if conector is not None:
               if (chip.x,chip.y) == (conector.x,conector.y):
                   self.guardar_chip_not.remove(chip)
    
