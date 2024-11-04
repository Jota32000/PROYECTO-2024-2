class Basurero:
    def __init__(self,guardar_led,guardar_switch,conectores,cables,resistencias,guardar_switch16,guardar_chip,guardar_chipOR,guardar_chipNOT):
        self.guardar_led=guardar_led
        self.guardar_switch=guardar_switch
        self.conectores=conectores
        self.cables=cables
        self.resistencias=resistencias
        self.guardar_switch16=guardar_switch16
        self.guardar_chip_and=guardar_chip
        self.guardar_chip_or=guardar_chipOR
        self.guardar_chip_not=guardar_chipNOT

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
                if switch.bandera == 2:
                    #corriente desde abajo
                    switch.pin2.eliminar_conexion(switch.pin2, switch.pin1)
                    switch.pin1.eliminar_conexion(switch.pin1, switch.pin3)
                    switch.pin4.eliminar_conexion(switch.pin4, switch.pin3)
                elif switch.bandera == 21:
                    #arriba derecha
                    switch.pin3.eliminar_conexion(switch.pin3, switch.pin1)
                    switch.pin4.eliminar_conexion(switch.pin4, switch.pin3)
                    switch.pin1.eliminar_conexion(switch.pin1, switch.pin2)

                elif switch.bandera == 4:
                    #abajo derecha
                    switch.pin1.eliminar_conexion(switch.pin1, switch.pin3)  # borra los pines 1 --> 3
                    switch.pin2.eliminar_conexion(switch.pin2, switch.pin1)
                    switch.pin3.eliminar_conexion(switch.pin3, switch.pin4)
                else:
                    # corriente desde arriba
                    switch.pin4.eliminar_conexion(switch.pin4, switch.pin3) # borra los pines 4 --> 3
                    switch.pin3.eliminar_conexion(switch.pin3, switch.pin1)
                    switch.pin2.eliminar_conexion(switch.pin2, switch.pin1)
                self.guardar_switch.remove(switch)

    def eliminar_cable(self,conector_cercano):
        #Buscador de cable en la lista de los cables
        for cable in self.cables:
            # ahora el extremo del nodo que presionas es donde se elimina
            conector_inicio = cable.conector_inicio
            conector_fin = cable.conector_fin
            if conector_cercano == conector_inicio:
                if cable.bandera == 1:
                    conector_fin.eliminar_conexion(conector_fin, conector_inicio)
                else:
                    conector_inicio.eliminar_conexion(conector_inicio,conector_fin)
                self.cables.remove(cable)

            elif conector_cercano == conector_fin:
                if cable.bandera == 2:
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
                if resistencia.bandera==1:
                    conector_fin.eliminar_conexion(conector_fin, conector_inicio)
                else:
                    conector_inicio.eliminar_conexion(conector_inicio, conector_fin)
                self.resistencias.remove(resistencia)
            elif conector_cercano == conector_fin:
                if resistencia.bandera==2:
                    conector_inicio.eliminar_conexion(conector_inicio, conector_fin)
                else:
                    conector_fin.eliminar_conexion(conector_fin, conector_inicio)
                self.resistencias.remove(resistencia)
    def eliminar_switch16(self, conector):
        # buscador de switch en la lista de switchs 16
        for switch in self.guardar_switch16:
            # Si el conector coincide con el pin1 del switch se eliminan todas las conexiones
            if conector == switch.pin1:
                for i in range(8):
                    a, b = switch.pines2(i)  # obtener el par de pines correspondiente
                    if a is not None and b is not None:
                        # verifica el estado de bandera para eliminar la conexion adecuadamente
                        if switch.bandera == 2:
                            b.eliminar_conexion(b, a)
                        else:
                            a.eliminar_conexion(a, b)
                # remover el switch de la lista despues de eliminar todas las conexiones
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