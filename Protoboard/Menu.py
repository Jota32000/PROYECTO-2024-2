import pygame

class Menu:
    def __init__(self):
        self.x = 0
        self.y = 50
        self.color_pulsar = (187, 143, 206)
        self.color_cursor = (143, 162, 206)
        self.color = (162, 206, 143)
        self.color_cable = (162, 206, 143)
        self.color_led = (162, 206, 143)
        self.color_switch = (162, 206, 143)
        self.color_switch4 = (162, 206, 143)
        self.color_switch16 = (162, 206, 143)
        self.color_res = (162, 206, 143)
        self.color_ship = (162, 206, 143)
        self.color_motor = (162, 206, 143)
        self.color_proto = (162, 206, 143)
        self.color_editar = (162, 206, 143)
        self.color_borrar = (162, 206, 143)
        self.color_switch_seleccionado = (162, 0, 0)
        self.ancho_boton = 0  # Atributo para almacenar el ancho
        self.font = pygame.font.Font(None, 22)
        self.cable_pulsado = False
        self.led_pulsado = False
        self.switch_pulsado = False
        self.res_pulsado = False
        self.ship_pulsado = False
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
        x_borde = self.x + 5
        y_borde = self.y + 5
        l1 = self.l1 - 5
        l2 = self.l2 - 5
        # Dibujar las líneas rectas entre las esquinas
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + self.l1, self.y), 20)  # Línea superior
        pygame.draw.line(screen, self.color, (self.x + self.l1, self.y), (self.x + self.l1, self.y + self.l2),
                         20)  # Línea derecha
        pygame.draw.line(screen, self.color, (self.x + self.l1, self.y + self.l2), (self.x, self.y + self.l2),
                         20)  # Línea inferior
        pygame.draw.line(screen, self.color, (self.x, self.y + self.l2), (self.x, self.y), 20)  # Línea izquierda
        for i in range(self.l2):
            pygame.draw.line(screen, self.color, (self.x + 4, self.y + 4 + i), (self.x + self.l1 - 4, self.y + i))
        # Dibujar el borde del rectángulo con esquinas redondeadas
        pygame.draw.arc(screen, self.border_color, (x_borde, y_borde, 2 * self.border_radius, 2 * self.border_radius),
                        0.5 * math.pi, math.pi, self.border_thickness)  # Esquina superior izquierda
        pygame.draw.arc(screen, self.border_color, (
        x_borde + l1 - 2 * self.border_radius, y_borde, 2 * self.border_radius, 2 * self.border_radius), 0,
                        0.5 * math.pi, self.border_thickness)  # Esquina superior derecha
        pygame.draw.arc(screen, self.border_color, (
        x_borde, y_borde + l2 - 2 * self.border_radius, 2 * self.border_radius, 2 * self.border_radius), math.pi,
                        1.5 * math.pi, self.border_thickness)  # Esquina inferior izquierda
        pygame.draw.arc(screen, self.border_color, (
        x_borde + l1 - 2 * self.border_radius, y_borde + l2 - 2 * self.border_radius, 2 * self.border_radius,
        2 * self.border_radius), 1.5 * math.pi, 2 * math.pi, self.border_thickness)  # Esquina inferior derecha

        pygame.draw.line(screen, self.border_color, (x_borde + self.border_radius, y_borde),
                         (x_borde + l1 - self.border_radius, y_borde), self.border_thickness)  # Línea superior
        pygame.draw.line(screen, self.border_color, (x_borde + l1, y_borde + self.border_radius),
                         (x_borde + l1, y_borde + l2 - self.border_radius), self.border_thickness)  # Línea derecha
        pygame.draw.line(screen, self.border_color, (x_borde + l1 - self.border_radius, y_borde + l2),
                         (x_borde + self.border_radius, y_borde + l2), self.border_thickness)  # Línea inferior
        pygame.draw.line(screen, self.border_color, (x_borde, y_borde + l2 - self.border_radius),
                         (x_borde, y_borde + self.border_radius), self.border_thickness)  # Línea izquierda

        # Dibujar los iconos y componentes
        self.dibujar_icono(screen, 100, self.x + 20, self.y + 10)
        self.dib_cable(screen, self.x + 95, self.y - 15)
        self.dibujar_icono(screen, 100, self.x + 145, self.y + 10)
        self.dib_led(screen, self.x + 170, self.y + 35)
        self.dibujar_icono(screen, 100, self.x + 270, self.y + 10)
        self.dib_switch(screen, self.x + 300, self.y + 40)
        self.dibujar_icono(screen, 100, self.x + 395, self.y + 10)
        self.dib_editor(screen, self.x + 420, self.y + 25)
        self.dibujar_icono(screen, 100, self.x + 520, self.y + 10)
        self.dib_basurero(screen, self.x + 535, self.y + 30)

        # Crear superficie para los botones semi-transparentes (para mostrar las áreas donde se puede hacer clic)
        boton_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # SRCALPHA para transparencia
        boton_led_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón LED
        boton_switch_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón Switch
        boton_basurero_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Boton basurero
        boton_edicion_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón edición
        boton_cable_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # Botón cable

        # Dibujar los botones en sus respectivas superficies
        self.dibujar_icono(boton_surface, 0, 0, 0)
        self.dib_led(boton_led_surface, 25, 15)
        self.dib_switch(boton_switch_surface, 25, 15)
        self.dib_basurero(boton_basurero_surface, 25, 15)
        self.dib_cable(boton_cable_surface, 25, 15)
        self.dib_editor(boton_edicion_surface, 25, 15)

        # Crear superficie para el botón LED (semi-transparente)
        boton_cable_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón CABLE
        boton_cable_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_led_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón LED
        boton_led_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_switch_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón Switch
        boton_switch_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        if(self.switch_pulsado):
            boton_switch2_surface = pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)  # Botón Switch 4 pines
            boton_switch2_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
            boton_switch16_surface=pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)  # Botón Switch 4 pines
            boton_switch16_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_resistencia_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón resistencia
        boton_resistencia_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_ship_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón ship
        boton_ship_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
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
        self.div_boton(boton_ship_surface, 0, 3, self.color_ship)
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
        screen.blit(boton_ship_surface, (x_inic + (self.ancho_boton * 4), 10))
        screen.blit(boton_motor_surface, (x_inic + (self.ancho_boton * 5), 10))
        screen.blit(boton_proto_surface, (x_inic + (self.ancho_boton * 6), 10))
        screen.blit(boton_edicion_surface, (x_inic + (self.ancho_boton * 7), 10))
        screen.blit(boton_basurero_surface, (x_inic + (self.ancho_boton * 8), 10))

    def dib_editor(self, screen, x, y):
        color = (229, 184, 0)
        cabeza = (255, 96, 96)
        # dibujo lapiz
        pygame.draw.line(screen, color, (x + 25, y), (x + 25, y + 70), 15)
        pygame.draw.line(screen, "white", (x + 20, y + 71), (x + 25, y + 80), 5)
        pygame.draw.line(screen, "white", (x + 30, y + 71), (x + 25, y + 80), 5)
        # cabeza lapiz
        pygame.draw.line(screen, cabeza, (x + 18, y), (x + 32, y), 5)
        # ciclo para relleno
        for i in range(6):
            pygame.draw.line(screen, "white", (x + 20, y + 70), (x + 20 + i, y + 70 + 1 * i), 5)
            pygame.draw.line(screen, "white", (x + 30, y + 70), (x + 20 + i, y + 70 + 1 * i), 5)
        pygame.draw.line(screen, "black", (x + 23, y + 80), (x + 27, y + 80), 4)

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

    def dib_led(self, screen, x, y):
        width = 50  # Ancho del LED
        height = 35  # Alto del LED
        color = (199, 9, 9)
        terminal = 30  # Longitud de los terminales
        radius = 10  # Radio de las esquinas redondeadas
        pin_y = y + 3
        # Dibujar las esquinas redondeadas
        pygame.draw.arc(screen, color, (x, y - radius - 4 + height - 2 * radius, 2 * radius, 2 * radius), 0.5 * math.pi,
                        math.pi, 5)  # Esquina superior izquierda
        pygame.draw.arc(screen, color, (x + width - 2 * radius, y, 2 * radius, 2 * radius), 0, 0.5 * math.pi,
                        5)  # Esquina superior derecha
        pygame.draw.arc(screen, color, (x + width - 2 * radius, y + height - 2 * radius, 2 * radius, 2 * radius),
                        1.5 * math.pi, 2 * math.pi, 5)  # Esquina inferior derecha
        pygame.draw.arc(screen, color, (x, y + height - 2 * radius, 2 * radius, 2 * radius), math.pi, 1.5 * math.pi,
                        5)  # Esquina inferior izquierda

        # Dibujar las líneas rectas entre las esquinas
        pygame.draw.line(screen, color, (x + radius, y), (x + width - radius, y), 5)  # Línea superior
        pygame.draw.line(screen, color, (x + width, y + radius), (x + width, y + height - radius), 5)  # Línea derecha
        pygame.draw.line(screen, color, (x + width - radius, y + height), (x + radius, y + height), 5)  # Línea inferior
        pygame.draw.line(screen, color, (x, y + height - radius), (x, y + radius), 5)  # Línea izquierda
        for i in range(height - 4):
            pygame.draw.line(screen, color, (x + 3, pin_y + i), (x + width - 3, pin_y + i))
        # Dibujar los terminales del LED (líneas)
        pygame.draw.line(screen, self.border_color, (x + width // 4, y + height),
                         (x + width // 4, y + height + terminal), 2)
        pygame.draw.line(screen, self.border_color, (x + 3 * width // 4, y + height),
                         (x + 3 * width // 4, y + height + terminal), 2)

    def dib_switch(self, screen, x, y):
        lado = 40  # Tamaño del switch (cuadrado)
        pin_length = 20  # Longitud de los pines
        body_color = (150, 150, 150)
        pin_color = (0, 0, 0)
        circle_radius = 10  # Radio del "círculo" en el medio
        pygame.draw.line(screen, body_color, (x, y), (x + lado, y), 2)
        pygame.draw.line(screen, body_color, (x + lado, y), (x + lado, y + lado), 2)
        pygame.draw.line(screen, body_color, (x + lado, y + lado), (x, y + lado), 2)
        pygame.draw.line(screen, body_color, (x, y + lado), (x, y), 2)
        for i in range(lado):
            pygame.draw.line(screen, body_color, (x, y + i), (x + lado, y + i))
        # Dibujar los pines del switch
        pygame.draw.line(screen, pin_color, (x, y + lado // 2), (x - pin_length, y + lado // 2), 3)
        pygame.draw.line(screen, pin_color, (x + lado, y + lado // 2), (x + lado + pin_length, y + lado // 2), 3)
        # Dibujar el "círculo" en el centro
        for angle in range(0, 360, 10):
            start_x = x + lado // 2
            start_y = y + lado // 2
            end_x = start_x + int(circle_radius * math.cos(math.radians(angle)))
            end_y = start_y + int(circle_radius * math.sin(math.radians(angle)))
            pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 2)

    def dib_basurero(self, screen, x, y):
        largo = 70
        sum = 10
        base = 50
        color = (190, 190, 190)
        pygame.draw.line(screen, color, (x, y), (x + largo, y), 10)
        pygame.draw.line(screen, color, (x + sum, y), (x + sum * 2, y + largo), 16)
        pygame.draw.line(screen, color, (x + sum * 2, y + largo), (x + base, y + largo), 5)
        pygame.draw.line(screen, color, (x + base, y + largo), (x + largo - sum, y), 16)
        pygame.draw.line(screen, color, (x + sum * 2, y - sum), (x + sum * 5, y - sum), 4)
        pygame.draw.line(screen, color, (x + sum * 2, y), (x + sum * 2, y - sum), 4)
        pygame.draw.line(screen, color, (x + sum * 5, y - sum), (x + sum * 5, y), 4)

        for i in range(largo):
            pygame.draw.line(screen, color, (x + sum * 2, y + i), (x + base, y + i))
        pygame.draw.line(screen, (161, 152, 152), (x + sum + 15, y + sum + 5), (x + sum + 15, y + base + sum), 3)
        pygame.draw.line(screen, (161, 152, 152), (x + sum * 3.5, y + sum + 5), (x + sum * 3.5, y + base + sum), 3)
        pygame.draw.line(screen, (161, 152, 152), (x + sum * 4.5, y + sum + 5), (x + sum * 4.5, y + base + sum), 3)

    def dibujar_recuadro_escogido(self, screen, lado, x, y):
        color = "red"
        grosor_borde = 5
        # Dibujar cuadrado
        pygame.draw.line(screen, color, (x, y), (x + lado, y), grosor_borde)  # Línea superior
        pygame.draw.line(screen, color, (x, y), (x, y + lado), grosor_borde)  # Línea izquierda
        pygame.draw.line(screen, color, (x + lado, y), (x + lado, y + lado), grosor_borde)  # Línea derecha
        pygame.draw.line(screen, color, (x, y + lado), (x + lado, y + lado), grosor_borde)  # Línea inferior
        for i in range(lado):
            pygame.draw.line(screen, color, (x, y + i), (x + lado, y + i))
        # borde adicional
        pygame.draw.line(screen, self.border_color, (x, y), (x + lado, y), self.border_thickness)  # Borde superior
        pygame.draw.line(screen, self.border_color, (x, y), (x, y + lado), self.border_thickness)  # Borde izquierdo
        pygame.draw.line(screen, self.border_color, (x + lado, y), (x + lado, y + lado),
                         self.border_thickness)  # Borde derecho
        pygame.draw.line(screen, self.border_color, (x, y + lado), (x + lado, y + lado),
                         self.border_thickness)  # Borde inferior

    def manejar_eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pos

            # Coordenadas y dimensiones del área del boton cable
            boton_cable_x = self.x + 20
            boton_cable_y = self.y + 10
            boton_cable_ancho = 100
            boton_cable_alto = 100

            if boton_cable_x <= mouse_x <= boton_cable_x + boton_cable_ancho and boton_cable_y <= mouse_y <= boton_cable_y + boton_cable_alto:
                self.accion_boton_cable()

            # Coordenadas y dimensiones del área del botón LED
            boton_led_x = self.x + 145
            boton_led_y = self.y + 10
            boton_led_ancho = 100
            boton_led_alto = 100

            # Verificar si el clic está dentro del área del botón LED
            if boton_led_x <= mouse_x <= boton_led_x + boton_led_ancho and boton_led_y <= mouse_y <= boton_led_y + boton_led_alto:
                self.accion_boton_led()

            # Coordenadas y dimensiones del área del botón Switch
            boton_switch_x = self.x + 270
            boton_switch_y = self.y + 10
            boton_switch_ancho = 100
            boton_switch_alto = 100

            # Verificar si el clic está dentro del área del botón Switch
            if boton_switch_x <= mouse_x <= boton_switch_x + boton_switch_ancho and boton_switch_y <= mouse_y <= boton_switch_y + boton_switch_alto:
                # Cambiar el color del botón SWITCH
                if (self.switch_pulsado == True):
                    self.switch_pulsado = False
                    self.color_switch = self.color
                else:
                    self.switch_pulsado = True
                    self.color_switch = self.color_pulsar
                    self.contador_click = 0

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
                    self.color_switch4 = self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón SWITCH 16
            switch16_x = 2 * self.ancho_boton
            switch16_y = 100
            switch16_ancho = self.ancho_boton
            switch16_alto = 45
            if self.switch_pulsado and boton_switch_x <= mouse_x <= switch16_x + switch16_ancho and switch16_y <= mouse_y <= switch16_y +switch16_alto:
                print(f"{self.contador_click}")
                if (self.boton_switch16_pulsado == True):
                    self.boton_switch16_pulsado = False
                    self.color_switch16 = self.color
                else:
                    self.boton_switch16_pulsado = True
                    self.color_switch16 = self.color_pulsar

            # Coordenadas y dimensiones del área del botón RESISTENCIA
            boton_resistencia_x = 3 * self.ancho_boton
            boton_resistencia_y = 3
            boton_resistencia_ancho = self.ancho_boton
            boton_resistencia_alto = 45

            # Verificar si el clic está dentro del área del botón Edición
            if boton_edicion_x <= mouse_x <= boton_edicion_x + boton_edicion_ancho and boton_edicion_y <= mouse_y <= boton_edicion_y + boton_edicion_alto:
                self.accion_boton_edicion()

            # Coordenadas y dimensiones del área del botón Basurero
            boton_basurero_x = self.x + 520
            boton_basurero_y = self.y + 10
            boton_basurero_ancho = 100
            boton_basurero_alto = 100

            # Verificar si el clic está dentro del área del botón basurero
            if boton_basurero_x <= mouse_x <= boton_basurero_x + boton_basurero_ancho and boton_basurero_y <= mouse_y <= boton_basurero_y + boton_basurero_alto:
                self.accion_boton_basurero()

    def accion_boton_cable(self):
        print("Botón Cable presionado")
        self.boton_led = False
        self.boton_switch = False
        self.boton_edicion = False
        self.boton_basurero = False

        if self.boton_cable == False:
            self.boton_cable = not self.boton_cable
        else:
            self.boton_cable = not self.boton_cable  # Desactivar el cable

    def accion_boton_led(self):
        print("Botón LED presionado")
        self.boton_cable = False
        self.boton_switch = False
        self.boton_edicion = False
        self.boton_basurero = False
        if self.boton_led == False:
            self.boton_led = not self.boton_led
        else:
            self.boton_led = not self.boton_led  # Desactivar el LED
        # print("led_b",boton_led)

    def accion_boton_switch(self):
        print("Botón Switch presionado")
        self.boton_cable = False
        self.boton_led = False
        self.boton_edicion = False
        self.boton_basurero = False

        if self.boton_switch == False:
            self.boton_switch = not self.boton_switch
        else:
            self.boton_switch = not self.boton_switch  # Desactivar el switch
        # print(boton_switch)

    def accion_boton_edicion(self):
        print("Botón Edición presionado")
        self.boton_cable = False
        self.boton_led = False
        self.boton_switch = False
        self.boton_basurero = False

        if self.boton_edicion == True:
            self.boton_edicion = not self.boton_edicion
        else:
            self.boton_edicion = not self.boton_edicion  # Desactivar la edición

            if boton_borrar_x <= mouse_x <= boton_borrar_x + boton_borrar_ancho and boton_borrar_y <= mouse_y <= boton_borrar_y + boton_borrar_alto:
                # Cambiar el color del botón BORRAR
                if (self.borrar_pulsado == True):
                    self.borrar_pulsado = False
                    self.color_borrar = self.color
                else:
                    self.borrar_pulsado = True
                    self.color_borrar = self.color_pulsar

