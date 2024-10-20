import pygame

class Menu:
    def __init__(self):
        self.x = 0
        self.y = 50
        self.color = (162, 206, 143)
        self.color_cable = (162, 206, 143)
        self.color_led = (162, 206, 143)
        self.color_switch = (162, 206, 143)
        self.color_switch4 = (162, 206, 143)
        self.color_switch16 = (162, 206, 143)
        self.color_res = (162, 206, 143)
        self.color_chip = (162, 206, 143)
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
        self.chip_pulsado = False
        self.motor_pulsado = False
        self.proto_pulsado = False
        self.editar_pulsado = False
        self.borrar_pulsado = False
        self.boton_switch2_pulsado = False
        self.boton_switch16_pulsado=False
        self.contador_click = 0

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
        textos = ["CABLE", "LED", "SWITCH", "RESISTENCIA", "CHIP", "MOTOR", "PROTOBOARD", "EDITAR", "BORRAR"]

        # Crear superficie para el botón LED (semi-transparente)
        boton_cable_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón CABLE
        boton_cable_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_led_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón LED
        boton_led_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_switch_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón Switch
        boton_switch_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia

        if (self.switch_pulsado):
            boton_switch2_surface = pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)  # Botón Switch 4 pines
            boton_switch2_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
            boton_switch16_surface=pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)  # Botón Switch 4 pines
            boton_switch16_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia

        if (self.cable_pulsado and self.editar_pulsado == False and self.borrar_pulsado == False):
            texto_cable_1 = ("Selecciona 2 posiciones en la protoboard para colocar el cable")
            screen.blit(self.font.render(texto_cable_1, True, (0, 0, 0)), (self.x + 250, self.y + 50)) # Texto impreso en pantalla

        elif (self.led_pulsado and self.editar_pulsado == False and self.borrar_pulsado == False):
            texto_led = ("Selecciona 2 posiciones de la led en la protoboard")
            screen.blit(self.font.render(texto_led, True, (0, 0, 0)), (self.x + 250, self.y + 50)) # Texto impreso en pantalla
        
        elif (self.switch_pulsado and self.editar_pulsado == False and self.borrar_pulsado == False):
            texto_switch = ("Por favor, selecciona una opción de switch")
            screen.blit(self.font.render(texto_switch, True, (0, 0, 0)), (self.x + 350, self.y + 50)) # Texto impreso en pantalla

            if (self.boton_switch2_pulsado):
                switch_2 = ("Selecciona cuatro puntos en la protoboard para colocar un switch")
                screen.blit(self.font.render(switch_2, True, (0, 0, 0)), (self.x + 350, self.y + 70)) # Texto impreso en pantalla
            
            elif (self.boton_switch16_pulsado):
                switch_16 = ("Selecciona 16 puntos en la protoboard para colocar un switch")
                screen.blit(self.font.render(switch_16, True, (0, 0, 0)), (self.x + 350, self.y + 70)) # Texto impreso en pantalla
                
        elif (self.res_pulsado and self.editar_pulsado == False and self.borrar_pulsado == False):
            texto_res = ("Selecciona 2 posiciones en la protoboard para colocar la resistencia")
            screen.blit(self.font.render(texto_res, True, (0, 0, 0)), (self.x + 250, self.y + 50)) # Texto impreso en pantalla

        elif (self.chip_pulsado and self.editar_pulsado == False and self.borrar_pulsado == False):
            chip = ("Selecciona una posición en la protoboard para colocar el chip")
            screen.blit(self.font.render(chip, True, (0, 0, 0)), (self.x + 350, self.y + 50)) # Texto impreso en pantalla
        
        elif (self.motor_pulsado):
            texto_motor = ("Motor apagado")
            screen.blit(self.font.render(texto_motor, True, (0, 0, 0)), (self.x + 430, self.y + 50)) # Texto impreso en pantalla

        elif (self.proto_pulsado and self.editar_pulsado == False and self.borrar_pulsado == False):
            pass    # Por el momento, este botón se encuentra en caso de futuras modificaciones
        
        elif (self.editar_pulsado):
            texto_edicion = ("Elige el componente a editar")
            screen.blit(self.font.render(texto_edicion, True, (0, 0, 0)), (self.x + 380, self.y + 50)) # Texto impreso en pantalla

            if (self.cable_pulsado):
                edicion_cable_1 = ("Primero selecciona los dos extremos del cable a editar")
                edicion_cable_2 = ("Luego selecciona dos nuevos puntos en la protoboard para colocar el cable")
                screen.blit(self.font.render(edicion_cable_1, True, (0, 0, 0)), (self.x + 250, self.y + 70))
                screen.blit(self.font.render(edicion_cable_2, True, (0, 0, 0)), (self.x + 250, self.y + 90)) # Texto impreso en pantalla

            elif (self.led_pulsado):
                edicion_led_1 = ("Primero selecciona la parte central del led a editar")
                edicion_led_2 = ("Luego selecciona dos puntos en la protoboard para colocar la led")
                screen.blit(self.font.render(edicion_led_1, True, (0, 0, 0)), (self.x + 250, self.y + 70))
                screen.blit(self.font.render(edicion_led_2, True, (0, 0, 0)), (self.x + 250, self.y + 90)) # Texto impreso en pantalla

            elif (self.switch_pulsado and self.boton_switch2_pulsado):
                edicion_switch_1 = ("Primero selecciona la parte central del switch a editar")
                edicion_switch_2 = ("Luego selecciona cuatro puntos en la protoboard para colocar el switch")
                screen.blit(self.font.render(edicion_switch_1, True, (0, 0, 0)), (self.x + 380, self.y + 70)) # Texto impreso en pantalla
                screen.blit(self.font.render(edicion_switch_2, True, (0, 0, 0)), (self.x + 380, self.y + 90)) # Texto impreso en pantalla

            elif (self.switch_pulsado and self.boton_switch16_pulsado):
                edicion_switch_1 = ("Primero selecciona la parte central del switch a editar")
                edicion_switch_2 = ("Luego selecciona ocho puntos en la protoboard para colocar el switch")
                screen.blit(self.font.render(edicion_switch_1, True, (0, 0, 0)), (self.x + 380, self.y + 70)) # Texto impreso en pantalla
                screen.blit(self.font.render(edicion_switch_2, True, (0, 0, 0)), (self.x + 380, self.y + 90)) # Texto impreso en pantalla

            elif (self.res_pulsado):
                edicion_res_1 = ("Primero selecciona los dos extremos de la resistencia a editar")
                edicion_res_2 = ("Luego selecciona dos nuevos puntos en la protoboard para colocar la resistencia")
                screen.blit(self.font.render(edicion_res_1, True, (0, 0, 0)), (self.x + 250, self.y + 70)) # Texto impreso en pantalla
                screen.blit(self.font.render(edicion_res_2, True, (0, 0, 0)), (self.x + 250, self.y + 90)) # Texto impreso en pantalla
            
            elif (self.chip_pulsado):
                pass    # Falta añadirlo todavía
        
        elif (self.borrar_pulsado):
            texto_borrar = ("Elige el componente a borrar")
            screen.blit(self.font.render(texto_borrar, True, (0, 0, 0)), (self.x + 380, self.y + 50)) # Texto impreso en pantalla

            if (self.cable_pulsado):
                borrar_cable_1 = ("Selecciona algún extremo de un cable para borrarlo")
                screen.blit(self.font.render(borrar_cable_1, True, (0, 0, 0)), (self.x + 320, self.y + 70)) # Texto impreso en pantalla
            
            elif (self.led_pulsado):
                borrar_led_1 = ("Selecciona la parte central de una led para borrarla")
                screen.blit(self.font.render(borrar_led_1, True, (0, 0, 0)), (self.x + 300, self.y + 70)) # Texto impreso en pantalla

            elif (self.switch_pulsado):
                borrar_switch = ("Selecciona que tipo de switch desea borrar")
                screen.blit(self.font.render(borrar_switch, True, (0, 0, 0)), (self.x + 380, self.y + 70)) # Texto impreso en pantalla
                
                if (self.boton_switch2_pulsado):
                    borrar_switch_2 = ("Selecciona la parte central del switch para borrarlo")
                    screen.blit(self.font.render(borrar_switch_2, True, (0, 0, 0)), (self.x + 380, self.y + 90)) # Texto impreso en pantalla
                
                elif (self.boton_switch16_pulsado):
                    borrar_switch_16 = ("Selecciona la parte central del switch para borrarlo")
                    screen.blit(self.font.render(borrar_switch_16, True, (0, 0, 0)), (self.x + 380, self.y + 90)) # Texto impreso en pantalla
            
            elif (self.res_pulsado):
                borrar_res_1 = ("Selecciona algún extremo de una resistencia para borrarlo")
                screen.blit(self.font.render(borrar_res_1, True, (0, 0, 0)), (self.x + 300, self.y + 70)) # Texto impreso en pantalla
            
            elif (self.chip_pulsado):
                pass    # Falta añadirlo todavía


        boton_resistencia_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón resistencia
        boton_resistencia_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_chip_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón chip
        boton_chip_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_motor_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón motor
        boton_motor_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_proto_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón protoboart
        boton_proto_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_edicion_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón edición
        boton_edicion_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_basurero_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Boton basurero
        boton_basurero_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        x_inic = 0
        # Dibujar el botón en la superficie del botón LED
        self.div_boton(boton_cable_surface, x_inic, 3, self.color_cable)
        self.div_boton(boton_led_surface, 0, 3, self.color_led)
        self.div_boton(boton_switch_surface, 0, 3, self.color_switch)
        if(self.switch_pulsado):
            #este hace la separacion vertical del boton
            self.div_boton(boton_switch2_surface, 0, 35,self.color_switch4)
            self.div_boton(boton_switch16_surface,0,33,self.color_switch16)
        self.div_boton(boton_resistencia_surface, 0, 3, self.color_res)
        self.div_boton(boton_chip_surface, 0, 3, self.color_chip)
        self.div_boton(boton_motor_surface, 0, 3, self.color_motor)
        self.div_boton(boton_proto_surface, 0, 3, self.color_proto)
        self.div_boton(boton_edicion_surface, 0, 3, self.color_editar)
        self.div_boton(boton_basurero_surface, 0, 3, self.color_borrar)

        # Blitear la superficie del botón
        screen.blit(boton_cable_surface, (0, 10))
        screen.blit(boton_led_surface, (x_inic + self.ancho_boton, 10))
        screen.blit(boton_switch_surface, (x_inic + (self.ancho_boton * 2), 10))
        if(self.switch_pulsado):
            screen.blit(boton_switch2_surface, (x_inic + (self.ancho_boton * 2), 20))
            screen.blit(boton_switch16_surface, (x_inic + (self.ancho_boton * 2), 60))
        screen.blit(boton_resistencia_surface, (x_inic + (self.ancho_boton * 3), 10))
        screen.blit(boton_chip_surface, (x_inic + (self.ancho_boton * 4), 10))
        screen.blit(boton_motor_surface, (x_inic + (self.ancho_boton * 5), 10))
        screen.blit(boton_proto_surface, (x_inic + (self.ancho_boton * 6), 10))
        screen.blit(boton_edicion_surface, (x_inic + (self.ancho_boton * 7), 10))
        screen.blit(boton_basurero_surface, (x_inic + (self.ancho_boton * 8), 10))

        # Dibujar líneas verticales en las posiciones correspondientes y agregar texto
        for i in range(9):  # 9 secciones
            x_pos = separacion_vertical * (i + 1)
            pygame.draw.line(screen, (0, 0, 0), (x_pos, 10), (x_pos, self.y), 3)
            # Renderizar el texto
            if textos[i] == "SWITCH" and self.switch_pulsado:
                texto_renderizado2 = self.font.render("Switch 4 pines", True, (0, 0, 0))
                texto_rect2 = texto_renderizado2.get_rect(center=(x_pos - self.ancho_boton // 2, 70))
                screen.blit(texto_renderizado2, texto_rect2)
                pygame.draw.line(screen, (0, 0, 0), (x_pos, 50), (x_pos, 130), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton*2, 50), (self.ancho_boton*2, 130), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton*2, 90), (x_pos, 90), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton*2, 130), (x_pos, 130), 3)
                texto_renderizado3= self.font.render("Switch 16 pines", True, (0, 0, 0))
                texto_rect3 = texto_renderizado3.get_rect(center=(x_pos - self.ancho_boton // 2, 110))
                screen.blit(texto_renderizado3, texto_rect3)
            texto_renderizado = self.font.render(textos[i], True, (0, 0, 0))  # Color negro para el texto
            # Posicionar el texto en el centro de cada división
            texto_rect = texto_renderizado.get_rect(center=(x_pos - self.ancho_boton // 2, self.y - 20))
            screen.blit(texto_renderizado, texto_rect)
                                
    def manejar_eventos(self, event):  # Agregar screen como argumento
        color_pulsar = (187, 143, 206)
        contador_click = 0
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
                    self.color_cable = color_pulsar

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
                    self.color_led = color_pulsar
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
                    self.color_switch = color_pulsar
                    contador_click = 0

            # Coordenadas y dimensiones del área del botón SWITCH de 4 pines
            boton_switch4_x = 2 * self.ancho_boton
            boton_switch4_y = 35  # Asumiendo que empieza a partir de esta coordenada vertical
            boton_switch4_ancho = self.ancho_boton
            boton_switch4_alto = 45  # Ajusta la altura según el tamaño del botón

            if boton_switch4_x <= mouse_x <= boton_switch4_x + boton_switch4_ancho and boton_switch4_y <= mouse_y <= boton_switch4_y + boton_switch4_alto:
                # Cambiar el color del botón SWITCH de 4 pines
                if self.boton_switch2_pulsado:
                    self.boton_switch2_pulsado = False
                    self.color_switch4 = self.color  # Regresar al color original
                else:
                    self.boton_switch2_pulsado = True
                    self.color_switch4 = color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón SWITCH 16
            switch16_x = 2 * self.ancho_boton
            switch16_y = 100
            switch16_ancho = self.ancho_boton
            switch16_alto = 45
            if self.switch_pulsado and boton_switch_x <= mouse_x <= switch16_x + switch16_ancho and switch16_y <= mouse_y <= switch16_y +switch16_alto:
                #print(f"{contador_click}")
                if (self.boton_switch16_pulsado == True):
                    self.boton_switch16_pulsado = False
                    self.color_switch16 = self.color
                else:
                    self.boton_switch16_pulsado = True
                    self.color_switch16 = color_pulsar

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
                    self.color_res = color_pulsar

            # Coordenadas y dimensiones del área del botón CHiP
            boton_shp_x = 4 * self.ancho_boton
            boton_shp_y = 3
            boton_shp_ancho = self.ancho_boton
            boton_shp_alto = 45

            if boton_shp_x <= mouse_x <= boton_shp_x + boton_shp_ancho and boton_shp_y <= mouse_y <= boton_shp_y + boton_shp_alto:
                # Cambiar el color del botón SHP
                if (self.chip_pulsado == True):
                    self.chip_pulsado = False
                    self.color_chip = self.color
                else:
                    self.chip_pulsado = True
                    self.color_chip = color_pulsar

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
                    self.color_motor = color_pulsar

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
                    self.color_proto = color_pulsar

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
                    self.color_editar = color_pulsar

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
                    self.color_borrar = color_pulsar