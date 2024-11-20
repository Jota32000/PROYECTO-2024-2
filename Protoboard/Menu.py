import pygame
from Protoboard import Protoboard  
from Conector import Conector
class Menu:
    def __init__(self):
        self.x = 0
        self.y = 50
        self.color_pulsar = (187, 143, 206)
        self.color = (162, 206, 143)
        self.color_cable = (162, 206, 143)
        self.color_led = (162, 206, 143)
        self.color_led1 = (162, 206, 143)
        self.color_led2 = (162, 206, 143)
        self.color_led3 = (162, 206, 143)
        self.color_led4 = (162, 206, 143)
        self.color_led5 = (162, 206, 143)
        self.color_switch = (162, 206, 143)
        self.color_switch4 = (162, 206, 143)
        self.color_switch16 = (162, 206, 143)
        self.color_res = (162, 206, 143)
        self.color_ship = (162, 206, 143)
        self.color_shipAND = (162, 206, 143)
        self.color_shipNOT = (162, 206, 143)
        self.color_shipOR = (162, 206, 143)
        self.color_motor = (162, 206, 143)
        self.color_proto = (162, 206, 143)
        self.color_editar = (162, 206, 143)
        self.color_borrar = (162, 206, 143)
        self.color_switch_seleccionado = (162, 0, 0)
        self.ancho_boton = 0  # Atributo para almacenar el ancho
        self.font = pygame.font.Font(None, 22)
        self.cable_pulsado = False
        self.led_pulsado = False
        self.led1_pulsado = False
        self.led2_pulsado = False
        self.led3_pulsado = False
        self.led4_pulsado = False
        self.led5_pulsado = False
        self.switch_pulsado = False
        self.res_pulsado = False
        self.chip_pulsado = False
        self.motor_pulsado = False
        self.proto_pulsado = False
        self.editar_pulsado = False
        self.borrar_pulsado = False
        self.boton_switch2_pulsado = False
        self.boton_switch16_pulsado=False
        self.and_pulsado=False
        self.not_pulsado=False
        self.or_pulsado=False
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
        textos = ["CABLE", "LED", "SWITCH", "RESISTENCIA", "CHIP", "DISPLAY", "PROTOBOARD", "EDITAR", "BORRAR"]
        # Crear superficie para el botón LED (semi-transparente)
        boton_cable_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón CABLE
        boton_cable_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_led_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón LED
        boton_led_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        if (self.led_pulsado):
            boton_led1_surface=pygame.Surface((self.ancho_boton, 60), pygame.SRCALPHA)
            boton_led1_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
            boton_led2_surface = pygame.Surface((self.ancho_boton, 60), pygame.SRCALPHA)
            boton_led2_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
            boton_led3_surface = pygame.Surface((self.ancho_boton, 60), pygame.SRCALPHA)
            boton_led3_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
            boton_led4_surface = pygame.Surface((self.ancho_boton, 60), pygame.SRCALPHA)
            boton_led4_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
            boton_led5_surface = pygame.Surface((self.ancho_boton, 60), pygame.SRCALPHA)
            boton_led5_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
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
        if (self.chip_pulsado):
            boton_and_surface = pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)
            boton_and_surface.fill((0, 0, 0, 0))
            boton_or_surface = pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)
            boton_or_surface.fill((0, 0, 0, 0))
            boton_not_surface = pygame.Surface((self.ancho_boton, 70), pygame.SRCALPHA)
            boton_not_surface.fill((0, 0, 0, 0))
        boton_motor_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón motor
        boton_motor_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_proto_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón protoboart
        boton_proto_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_edicion_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Botón edición
        boton_edicion_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        boton_basurero_surface = pygame.Surface((self.ancho_boton, 39), pygame.SRCALPHA)  # Boton basurero
        boton_basurero_surface.fill((0, 0, 0, 0))  # Rellenar la superficie con transparencia
        x_inic = 0
        # Dibujar el botón en la superficie del botón
        self.div_boton(boton_cable_surface, x_inic, 3, self.color_cable)
        self.div_boton(boton_led_surface, 0, 3, self.color_led)
        if self.led_pulsado:
            self.div_boton(boton_led1_surface,0,35,self.color_led1)
            self.div_boton(boton_led2_surface, 0, 35, self.color_led2)
            self.div_boton(boton_led3_surface, 0, 35, self.color_led3)
            self.div_boton(boton_led4_surface, 0, 35, self.color_led4)
            self.div_boton(boton_led5_surface, 0, 35, self.color_led5)
        self.div_boton(boton_switch_surface, 0, 3, self.color_switch)
        if(self.switch_pulsado):
            #este hace la separacion vertical del boton
            self.div_boton(boton_switch2_surface, 0, 35,self.color_switch4)
            self.div_boton(boton_switch16_surface,0,33,self.color_switch16)
        self.div_boton(boton_resistencia_surface, 0, 3, self.color_res)
        self.div_boton(boton_ship_surface, 0, 3, self.color_ship)
        if (self.chip_pulsado):
            self.div_boton(boton_and_surface,0,35,self.color_shipAND)
            self.div_boton(boton_or_surface,0,35,self.color_shipOR)
            self.div_boton(boton_not_surface,0,35,self.color_shipNOT)
        self.div_boton(boton_motor_surface, 0, 3, self.color_motor)
        self.div_boton(boton_proto_surface, 0, 3, self.color_proto)
        self.div_boton(boton_edicion_surface, 0, 3, self.color_editar)
        self.div_boton(boton_basurero_surface, 0, 3, self.color_borrar)

        # Blitear la superficie del botón
        screen.blit(boton_cable_surface, (0, 10))
        screen.blit(boton_led_surface, (x_inic + self.ancho_boton, 10))
        if self.led_pulsado:
            screen.blit(boton_led1_surface, (x_inic + (self.ancho_boton), 20))
            screen.blit(boton_led2_surface, (x_inic + (self.ancho_boton), 48))
            screen.blit(boton_led3_surface, (x_inic + (self.ancho_boton), 76))
            screen.blit(boton_led4_surface, (x_inic + (self.ancho_boton), 104))
            screen.blit(boton_led5_surface, (x_inic + (self.ancho_boton), 132))
        screen.blit(boton_switch_surface, (x_inic + (self.ancho_boton * 2), 10))
        if(self.switch_pulsado):
            screen.blit(boton_switch2_surface, (x_inic + (self.ancho_boton * 2), 20))
            screen.blit(boton_switch16_surface, (x_inic + (self.ancho_boton * 2), 60))
        screen.blit(boton_resistencia_surface, (x_inic + (self.ancho_boton * 3), 10))
        screen.blit(boton_ship_surface, (x_inic + (self.ancho_boton * 4), 10))
        if (self.chip_pulsado):
            screen.blit(boton_and_surface,(x_inic + (self.ancho_boton * 4), 20))
            screen.blit(boton_or_surface, (x_inic + (self.ancho_boton * 4), 58))
            screen.blit(boton_not_surface, (x_inic + (self.ancho_boton * 4), 95))
        screen.blit(boton_motor_surface, (x_inic + (self.ancho_boton * 5), 10))
        screen.blit(boton_proto_surface, (x_inic + (self.ancho_boton * 6), 10))
        screen.blit(boton_edicion_surface, (x_inic + (self.ancho_boton * 7), 10))
        screen.blit(boton_basurero_surface, (x_inic + (self.ancho_boton * 8), 10))

        texto = "Presiona la barra espaciadora para ver instrucciones"
        font = pygame.font.Font(None, 24)
        texto_surface = font.render(texto,True,"black") # Renderizado del texto
        texto_rect = texto_surface.get_rect(center=(self.x + 220 ,self.y + 160)) # Obtener la superficie en la pantalla del texto 
        screen.blit(texto_surface,texto_rect) # Dibujar el texto en la pantalla en la posición deseada

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
            if textos[i]== "CHIP" and self.chip_pulsado:
                texto_renderizado4=self.font.render("Chip AND",True,(0,0,0))
                texto_rect4= texto_renderizado4.get_rect(center=(x_pos - self.ancho_boton // 2, 70))
                screen.blit(texto_renderizado4,texto_rect4)
                texto_renderizado5 = self.font.render("Chip OR", True, (0, 0, 0))
                texto_rect5 = texto_renderizado5.get_rect(center=(x_pos - self.ancho_boton // 2, 110))
                screen.blit(texto_renderizado5, texto_rect5)
                texto_renderizado6 = self.font.render("Chip NOT", True, (0, 0, 0))
                texto_rect6 = texto_renderizado6.get_rect(center=(x_pos - self.ancho_boton // 2, 150))
                screen.blit(texto_renderizado6, texto_rect6)
                pygame.draw.line(screen, (0, 0, 0), (x_pos, 50), (x_pos, 165), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton * 4, 50), (self.ancho_boton * 4, 165), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton * 4, 90), (x_pos, 90), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton * 4, 128), (x_pos, 128), 3)
                pygame.draw.line(screen, (0, 0, 0), (self.ancho_boton * 4, 165), (x_pos, 165), 3)
            if textos[i]=="LED" and self.led_pulsado:
                texto_renderizado5 = self.font.render("ROJO", True, (0, 0, 0))
                texto_rect5 = texto_renderizado5.get_rect(center=(x_pos - self.ancho_boton // 2, 67))
                screen.blit(texto_renderizado5, texto_rect5)
                texto_renderizado6 = self.font.render("VERDE", True, (0, 0, 0))
                texto_rect6 = texto_renderizado6.get_rect(center=(x_pos - self.ancho_boton // 2, 97))
                screen.blit(texto_renderizado6, texto_rect6)
                texto_renderizado7 = self.font.render("AMARILLO", True, (0, 0, 0))
                texto_rect7 = texto_renderizado7.get_rect(center=(x_pos - self.ancho_boton // 2, 125))
                screen.blit(texto_renderizado7, texto_rect7)
                texto_renderizado8 = self.font.render("AZUL", True, (0, 0, 0))
                texto_rect8 = texto_renderizado8.get_rect(center=(x_pos - self.ancho_boton // 2, 153))
                screen.blit(texto_renderizado8, texto_rect8)
                texto_renderizado9 = self.font.render("MORADO", True, (0, 0, 0))
                texto_rect9 = texto_renderizado9.get_rect(center=(x_pos - self.ancho_boton // 2, 180))
                screen.blit(texto_renderizado9, texto_rect9)

            texto_renderizado = self.font.render(textos[i], True, (0, 0, 0))  # Color negro para el texto
            # Posicionar el texto en el centro de cada división
            texto_rect = texto_renderizado.get_rect(center=(x_pos - self.ancho_boton // 2, self.y - 20))
            screen.blit(texto_renderizado, texto_rect)
    def pantalla_secundaria(self,screen):
        screen.fill("white")
        texto_edicion = "Opción de edición"
        font = pygame.font.Font(None, 20)
        
        texto_edicion_surface = font.render(texto_edicion,True,"black") # Renderizado del texto
        texto_edicion_rect = texto_edicion_surface.get_rect(center=(200,310)) # Obtener la superficie en la pantalla del texto 
        screen.blit(texto_edicion_surface,texto_edicion_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_edicion = "Primero elige la opcion de edición y luego el componente a editar"
        opcion_edicion_surface = font.render(opcion_edicion,True,"black") # Renderizado del texto
        opcion_edicion_rect = opcion_edicion_surface.get_rect(center=(240,330)) # Obtener la superficie en la pantalla del texto
        screen.blit(opcion_edicion_surface,opcion_edicion_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_cables_resistencia = "Para los cables o resistencias, primero selecciona ambos puntos"
        opcion_cables_resistencia_surface = font.render(opcion_cables_resistencia,True,"black") # Renderizado del texto
        opcion_cables_resistencia_rect = opcion_cables_resistencia_surface.get_rect(center=(240,350)) # Obtener la superficie en la pantalla del texto
        screen.blit(opcion_cables_resistencia_surface,opcion_cables_resistencia_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_cables_resistencia_2 = "y luego escoge 2 nuevos puntos en la protoboard."
        opcion_cables_resistencia_surface_2 = font.render(opcion_cables_resistencia_2,True,"black") # Renderizado del texto
        opcion_cables_resistencia_rect_2 = opcion_cables_resistencia_surface_2.get_rect(center=(210,370)) # Obtener la superficie en la pantalla del texto
        screen.blit(opcion_cables_resistencia_surface_2,opcion_cables_resistencia_rect_2) # Dibujar el texto en la pantalla en la posición deseada
        opcion_led = "Para el led, primero selecciona su parte central"
        opcion_led_surface = font.render(opcion_led,True,"black") # Renderizado del texto
        opcion_led_rect = opcion_led_surface.get_rect(center=(205,390)) # Obtener la superficie en la pantalla del texto
        screen.blit(opcion_led_surface,opcion_led_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_led_2 = "y luego escoge 2 nuevos puntos en la protoboard."
        opcion_led_surface_2 = font.render(opcion_led_2,True,"black") # Renderizado del texto
        opcion_led_rect_2 = opcion_led_surface_2.get_rect(center=(210,410)) # Obtener la superficie en la pantalla del texto
        screen.blit(opcion_led_surface_2,opcion_led_rect_2) # Dibujar el texto en la pantalla en la posición deseada
        opciones_restantes = "Para el resto, escoge su esquina superior derecha"
        resto = "y luego escoge un punto en la protoboard."
        resto_surface = font.render(resto,True,"black") # Renderizado del texto
        resto_surface_2 = font.render(opciones_restantes,True,"black") # Renderizado del texto
        resto_rect = resto_surface.get_rect(center=(185,450)) # Obtener la superficie en la pantalla del texto
        opciones_rect = resto_surface_2.get_rect(center=(210,430)) 
        screen.blit(resto_surface,resto_rect) # Dibujar el texto en la pantalla en la posición deseada
        screen.blit(resto_surface_2,opciones_rect) # Dibujar el texto en la pantalla en la posición deseada

        texto_borrado = "Opción de borrado"
        font = pygame.font.Font(None, 20)
        texto_borrado_surface = font.render(texto_borrado,True,"black") # Renderizado del texto
        texto_borrado_rect = texto_borrado_surface.get_rect(center=(800,310)) # Obtener la superficie en la pantalla del texto 
        screen.blit(texto_borrado_surface,texto_borrado_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_borrado = "Primero elige la opcion de borrado y luego el componente a eliminar"
        opcion_borrado_2 = "Luego elige su origen o la esquina superior izquierda para eliminarlo"
        opcion_borrado_surface = font.render(opcion_borrado,True,"black") # Renderizado del texto
        opcion_borrado_rect = opcion_borrado_surface.get_rect(center=(820,330)) # Obtener la superficie en la pantalla del texto 
        screen.blit(opcion_borrado_surface,opcion_borrado_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_borrado_surface_2 = font.render(opcion_borrado_2,True,"black") # Renderizado del texto
        opcion_borrado_rect_2 = opcion_borrado_surface_2.get_rect(center=(825,350)) # Obtener la superficie en la pantalla del texto
        screen.blit(opcion_borrado_surface_2,opcion_borrado_rect_2) # Dibujar el texto en la pantalla en la posición deseada

        texto_cables = "Opción de cables"
        font = pygame.font.Font(None, 20)
        texto_cables_surface = font.render(texto_cables,True,"black") # Renderizado del texto
        texto_cables_rect = texto_cables_surface.get_rect(center=(200,50)) # Obtener la superficie en la pantalla del texto
        screen.blit(texto_cables_surface,texto_cables_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_cables = "Elige dos puntos para colocar un cable"
        opcion_cables_surface = font.render(opcion_cables,True,"black") # Renderizado del texto
        texto_opcion_cables = texto_cables_surface.get_rect(center=(140,70))
        screen.blit(opcion_cables_surface, texto_opcion_cables) # Dibujar el texto en la pantalla en la posición deseada

        texto_led = "Opción de led"
        font = pygame.font.Font(None, 20)
        texto_led_surface = font.render(texto_led,True,"black") # Renderizado del texto
        texto_led_rect = texto_led_surface.get_rect(center=(800,50)) # Obtener la superficie en la pantalla del texto
        screen.blit(texto_led_surface,texto_led_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_led = "Elige dos puntos en la protoboard para colocar un led"
        opcion_led_surface = font.render(opcion_led,True,"black") # Renderizado del texto
        texto_opcion_led = texto_led_surface.get_rect(center=(700,70))
        screen.blit(opcion_led_surface, texto_opcion_led) # Dibujar el texto en la pantalla en la posición deseada

        texto_switch = "Opción de switch"
        font = pygame.font.Font(None, 20)
        texto_switch_surface = font.render(texto_switch,True,"black") # Renderizado del texto
        texto_switch_rect = texto_switch_surface.get_rect(center=(200,110)) # Obtener la superficie en la pantalla del texto
        screen.blit(texto_switch_surface,texto_switch_rect) # Dibujar el texto en la pantalla en la posición deseada
        variantes_switch = "Primero elige el tipo de switch a colocar" 
        variantes_switch_surface = font.render(variantes_switch,True,"black") # Renderizado del texto
        variantes_switch_rect = variantes_switch_surface.get_rect(center=(220,130))
        screen.blit(variantes_switch_surface, variantes_switch_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_switch = "Luego elige un punto en la protoboard para colocar un switch"
        opcion_switch_surface = font.render(opcion_switch,True,"black") # Renderizado del texto
        texto_opcion_switch = texto_switch_surface.get_rect(center=(100,150))
        screen.blit(opcion_switch_surface, texto_opcion_switch) # Dibujar el texto en la pantalla en la posición deseada
        opcion_switch_2 = "(Teniendo como referencia la parte superior izquierda como punto inicial)"
        opcion_switch_surface_2 = font.render(opcion_switch_2,True,"black") # Renderizado del texto
        opcion_switch_rect_2 = opcion_switch_surface_2.get_rect(center=(240,170))
        screen.blit(opcion_switch_surface_2, opcion_switch_rect_2) # Dibujar el texto en la pantalla en la posición deseada

        texto_resistencia = "Opción de resistencia"
        font = pygame.font.Font(None, 20)
        texto_resistencia_surface = font.render(texto_resistencia,True,"black") # Renderizado del texto
        texto_resistencia_rect = texto_resistencia_surface.get_rect(center=(800,110)) # Obtener la superficie en la pantalla del texto
        screen.blit(texto_resistencia_surface,texto_resistencia_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_resistencia = "Elige dos puntos en la protoboard para colocar una resistencia"
        opcion_resistencia_surface = font.render(opcion_resistencia,True,"black") # Renderizado del texto
        texto_opcion_resistencia = texto_resistencia_surface.get_rect(center=(700,130))
        screen.blit(opcion_resistencia_surface, texto_opcion_resistencia) # Dibujar el texto en la pantalla en la posición deseada

        texto_chip = "Opción de chip"
        font = pygame.font.Font(None, 20)
        texto_chip_surface = font.render(texto_chip,True,"black") # Renderizado del texto
        texto_chip_rect = texto_chip_surface.get_rect(center=(200,210)) # Obtener la superficie en la pantalla del texto
        screen.blit(texto_chip_surface, texto_chip_rect) # Dibujar el texto en la pantalla en la posición deseada
        variantes_chip = "Primero elige el tipo de chip a colocar"
        variantes_chip_surface = font.render(variantes_chip,True,"black") # Renderizado del texto
        variantes_chip_rect = variantes_chip_surface.get_rect(center=(210,230))
        screen.blit(variantes_chip_surface, variantes_chip_rect) # Dibujar el texto en la pantalla en la posición deseada
        opcion_chip = "Luego elige un punto en la protoboard para colocar un chip"
        opcion_chip_surface = font.render(opcion_chip,True,"black") # Renderizado del texto
        texto_opcion_chip = texto_chip_surface.get_rect(center=(90,250))
        screen.blit(opcion_chip_surface, texto_opcion_chip) # Dibujar el texto en la pantalla en la posición deseada
        opcion_chip_2 = "(Teniendo como referencia la parte superior izquierda como punto inicial)"
        opcion_chip_surface_2 = font.render(opcion_chip_2,True,"black") # Renderizado del texto
        opcion_chip_rect_2 = opcion_chip_surface_2.get_rect(center=(240,270))
        screen.blit(opcion_chip_surface_2, opcion_chip_rect_2) # Dibujar el texto en la pantalla en la posición deseada

        texto_display = "Opción de display"
        font = pygame.font.Font(None, 20)
        texto_display_surface = font.render(texto_display,True,"black") # Renderizado del texto
        texto_display_rect = texto_display_surface.get_rect(center=(800,210)) # Obtener la superficie en la pantalla del texto
        screen.blit(texto_display_surface, texto_display_rect) # Dibujar el texto en la pantalla en la posición deseada   
        opcion_display = "Elige un punto en la protoboard para colocar un display"   
        opcion_display_surface = font.render(opcion_display,True,"black") # Renderizado del texto
        texto_opcion_display = texto_display_surface.get_rect(center=(700,230))
        screen.blit(opcion_display_surface, texto_opcion_display) # Dibujar el texto en la pantalla en la posición deseada

        barra_espaciadora = "Presiona la barra espaciadora para volver a la pantalla inicial"
        font = pygame.font.Font(None, 24)
        barra_espaciadora_surface = font.render(barra_espaciadora,True,"black") # Renderizado del texto
        barra_espaciadora_rect = barra_espaciadora_surface.get_rect(center=(500,500))
        screen.blit(barra_espaciadora_surface, barra_espaciadora_rect) # Dibujar el texto en la pantalla en la posición deseada
    def manejar_eventos(self, event):
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
                    self.color_cable = self.color_pulsar

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
                    self.color_led = self.color_pulsar

            # Coordenadas y dimensiones del área del botón led1
            boton_led1_x = self.ancho_boton
            boton_led1_y = 35
            boton_led1_ancho = self.ancho_boton
            boton_led1_alto = 45
            if boton_led1_x <= mouse_x <= boton_led1_x + boton_led1_ancho and boton_led1_y <= mouse_y <= boton_led1_y + boton_led1_alto:
                if self.led1_pulsado:
                    self.led1_pulsado = False
                    self.color_led1 = self.color  # Regresar al color original
                else:
                    self.led1_pulsado = True
                    self.color_led1= self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón led2
            boton_led2_x = self.ancho_boton
            boton_led2_y = 81
            boton_led2_ancho = self.ancho_boton
            boton_led2_alto = 25
            if boton_led2_x <= mouse_x <= boton_led2_x + boton_led2_ancho and boton_led2_y <= mouse_y <= boton_led2_y + boton_led2_alto:
                if self.led2_pulsado:
                    self.led2_pulsado = False
                    self.color_led2 = self.color  # Regresar al color original
                else:
                    self.led2_pulsado = True
                    self.color_led2 = self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón led3
            boton_led3_x = self.ancho_boton
            boton_led3_y = 110
            boton_led3_ancho = self.ancho_boton
            boton_led3_alto = 25
            if boton_led3_x <= mouse_x <= boton_led3_x + boton_led3_ancho and boton_led3_y <= mouse_y <= boton_led3_y + boton_led3_alto:
                if self.led3_pulsado:
                    self.led3_pulsado = False
                    self.color_led3 = self.color  # Regresar al color original
                else:
                    self.led3_pulsado = True
                    self.color_led3 = self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón led4
            boton_led4_x = self.ancho_boton
            boton_led4_y = 137
            boton_led4_ancho = self.ancho_boton
            boton_led4_alto = 25
            if boton_led4_x <= mouse_x <= boton_led4_x + boton_led4_ancho and boton_led4_y <= mouse_y <= boton_led4_y + boton_led4_alto:
                if self.led4_pulsado:
                    self.led4_pulsado = False
                    self.color_led4 = self.color  # Regresar al color original
                else:
                    self.led4_pulsado = True
                    self.color_led4 = self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón led5
            boton_led5_x = self.ancho_boton
            boton_led5_y = 164
            boton_led5_ancho = self.ancho_boton
            boton_led5_alto = 25
            if boton_led5_x <= mouse_x <= boton_led5_x + boton_led5_ancho and boton_led5_y <= mouse_y <= boton_led5_y + boton_led5_alto:
                if self.led5_pulsado:
                    self.led5_pulsado = False
                    self.color_led5 = self.color  # Regresar al color original
                else:
                    self.led5_pulsado = True
                    self.color_led5 = self.color_pulsar  # Cambiar al color pulsado
            # Coordenadas y dimensiones del área del botón SWITCH
            boton_switch_x = 2 * self.ancho_boton
            boton_switch_y = 2
            boton_switch_ancho = self.ancho_boton
            boton_switch_alto = 45
            if boton_switch_x <= mouse_x <= boton_switch_x + boton_switch_ancho and boton_switch_y <= mouse_y <= boton_switch_y + boton_switch_alto:
                # Cambiar el color del botón SWITCH
                if (self.switch_pulsado == True):
                    self.switch_pulsado = False
                    self.color_switch = self.color
                else:
                    self.switch_pulsado = True
                    self.color_switch = self.color_pulsar

            # Coordenadas y dimensiones del área del botón SWITCH de 4 pines
            boton_switch4_x = 2 * self.ancho_boton
            boton_switch4_y = 47
            boton_switch4_ancho = self.ancho_boton
            boton_switch4_alto = 43
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
            switch16_y = 93
            switch16_ancho = self.ancho_boton
            switch16_alto = 43
            if self.switch_pulsado and boton_switch_x <= mouse_x <= switch16_x + switch16_ancho and switch16_y <= mouse_y <= switch16_y +switch16_alto:
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
            if boton_resistencia_x <= mouse_x <= boton_resistencia_x + boton_resistencia_ancho and boton_resistencia_y <= mouse_y <= boton_resistencia_y + boton_resistencia_alto:
                # Cambiar el color del botón RESISTENCIA
                if (self.res_pulsado == True):
                    self.res_pulsado = False
                    self.color_res = self.color
                else:
                    self.res_pulsado = True
                    self.color_res = self.color_pulsar

            # Coordenadas y dimensiones del área del botón CHiP
            boton_shp_x = 4 * self.ancho_boton
            boton_shp_y = 3
            boton_shp_ancho = self.ancho_boton
            boton_shp_alto = 45
            if boton_shp_x <= mouse_x <= boton_shp_x + boton_shp_ancho and boton_shp_y <= mouse_y <= boton_shp_y + boton_shp_alto:
                # Cambiar el color del botón SHP
                if (self.chip_pulsado == True):
                    self.chip_pulsado = False
                    self.color_ship = self.color
                else:
                    self.chip_pulsado = True
                    self.color_ship = self.color_pulsar

            # Coordenadas y dimensiones del área del botón chip AND
            boton_and_x = 4 * self.ancho_boton
            boton_and_y = 50
            boton_and_ancho = self.ancho_boton
            boton_and_alto = 40
            if boton_and_x <= mouse_x <= boton_and_x + boton_and_ancho and boton_and_y <= mouse_y <= boton_and_y + boton_and_alto:
                if self.and_pulsado:
                    self.and_pulsado = False
                    self.color_shipAND = self.color  # Regresar al color original
                else:
                    self.and_pulsado = True
                    self.color_shipAND = self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón chip OR
            boton_or_x = 4 * self.ancho_boton
            boton_or_y = 92
            boton_or_ancho = self.ancho_boton
            boton_or_alto = 35
            if boton_or_x <= mouse_x <= boton_or_x + boton_or_ancho and boton_or_y <= mouse_y <= boton_or_y + boton_or_alto:
                if self.or_pulsado:
                    self.or_pulsado = False
                    self.color_shipOR = self.color  # Regresar al color original
                else:
                    self.or_pulsado = True
                    self.color_shipOR = self.color_pulsar  # Cambiar al color pulsado

            # Coordenadas y dimensiones del área del botón chip NOT
            boton_not_x = 4 * self.ancho_boton
            boton_not_y = 129
            boton_not_ancho = self.ancho_boton
            boton_not_alto = 35
            if boton_not_x <= mouse_x <= boton_not_x + boton_not_ancho and boton_not_y <= mouse_y <= boton_not_y + boton_not_alto:
                if self.not_pulsado:
                    self.not_pulsado = False
                    self.color_shipNOT = self.color  # Regresar al color original
                else:
                    self.not_pulsado = True
                    self.color_shipNOT = self.color_pulsar  # Cambiar al color pulsado

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
                    self.color_motor = self.color_pulsar

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
                    self.color_proto = self.color_pulsar
            #elif self.proto_pulsado and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #    x, y = event.pos
            #    print(f"Clic en: ({x}, {y})")               

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
                    self.color_editar = self.color_pulsar

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
                    self.color_borrar = self.color_pulsar

            