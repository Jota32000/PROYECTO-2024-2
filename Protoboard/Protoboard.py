import pygame
from Conector import Conector
class Protoboard:
    def __init__(self, x, y,conectores,longitud):
        self.x = x
        self.y = y
        self.largo = 940
        self.ancho = 430
        self.color = (222, 222, 222)
        self.conectores_creados = False
        self.conectores=conectores
        self.longitud = longitud

    def crear(self, screen):
        # Línea superior
        pygame.draw.line(screen, ("black"), (self.x, self.y), (self.x + self.largo, self.y), 3)
        # Línea izquerda
        pygame.draw.line(screen, ("black"), (self.x, self.y), (self.x, self.y + self.ancho), 3)
        # Línea derecha
        pygame.draw.line(screen, ("black"), (self.x + self.largo, self.y), (self.x + self.largo, self.y + self.ancho),3)
        # Línea inferior
        pygame.draw.line(screen, ("black"), (self.x, self.y + self.ancho), (self.x + self.largo, self.y + self.ancho),3)

        for i in range(self.ancho):
            pygame.draw.line(screen, self.color, (self.x, self.y + i), (self.x + self.largo, self.y + i))

        alto = 10
        pygame.draw.line(screen, (17, 17, 222), (self.x + alto, self.y + alto), (self.x + self.largo - 10, self.y + alto),1)
        pygame.draw.line(screen, (222, 17, 17), (self.x + alto, self.y + 56), (self.x + self.largo - 10, self.y + 56),1)
        pygame.draw.line(screen, (222, 17, 17), (self.x + alto, self.y + self.ancho-10), (self.x + self.largo - 10, self.y + self.ancho-10),1)
        pygame.draw.line(screen, (17, 17, 222), (self.x + alto, self.y + self.ancho - 55),(self.x + self.largo - 10, self.y + self.ancho - 55), 1)

        # crear CANAL Central
        mitad_largo = self.ancho // 2
        pygame.draw.line(screen, (207, 207, 207), (self.x, self.y + mitad_largo),(self.x + self.largo, self.y + mitad_largo), 10)

        # Llamar al metodo para dibujar conectores
        self.dibujar_conectores(screen)

    def dibujar_conectores(self, screen):
        # Coordenadas iniciales para conectores
        inicio_x = self.x + 35
        inicio_y = self.y + 20
        
        separacion_columnas = 30  # Espacio entre las columnas de conectores (ajustar según tu diseño)

        # Configurar la fuente para los números
        fuente = pygame.font.SysFont(None, 22)

        # Dibujar números sobre las columnas (ejemplo: 12 columnas)
        for i in range(30):
            numero = str(i + 1)
            texto = fuente.render(numero, True, (84, 84, 84))  # Color gris para los números
            posicion_x = self.x + 30 + (i * separacion_columnas)  # Alinear el número con la columna correspondiente
            screen.blit(texto, (posicion_x, self.y + 60)) # (x,y) ambos dinámicos
            screen.blit(texto, (posicion_x, self.y + 360 )) # (x,y) ambos dinámicos
        
        dibujar_mas(screen,inicio_x-20,inicio_y+390,10,(222,17,17))
        dibujar_menos(screen,inicio_x-20,inicio_y+362,(17,17,222))
        dibujar_a(screen,inicio_x-20,inicio_y+325,10,10,(84 , 84, 84))
        dibujar_b(screen, inicio_x-20, inicio_y+295, 10,  (84, 84, 84))
        dibujar_c(screen, inicio_x-20 , inicio_y+265, 10, 10, (84, 84, 84))
        dibujar_d(screen, inicio_x-20 , inicio_y+235, 10, 10, (84, 84, 84))
        dibujar_e(screen, inicio_x-20 , inicio_y+205, 10, 10, (84, 84, 84))
        dibujar_f(screen, inicio_x-20 , inicio_y+175, 10, 10, (84, 84, 84))
        dibujar_g(screen, inicio_x-20 , inicio_y+145, 10, 10, (84, 84, 84))
        dibujar_h(screen, inicio_x-20 , inicio_y+115, 10, 10, (84, 84, 84))
        dibujar_i(screen, inicio_x-20 , inicio_y+85, 10, 10, (84, 84, 84))
        dibujar_j(screen, inicio_x-20, inicio_y+55, 10, 10, (84, 84, 84))
        dibujar_mas(screen, inicio_x - 20, inicio_y+30, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x - 20, inicio_y , (17, 17, 222))

        dibujar_mas(screen, inicio_x +self.largo-55, inicio_y + 390, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x +self.largo-55, inicio_y + 362, (17, 17, 222))
        dibujar_a(screen, inicio_x+self.largo-55, inicio_y + 325, 10, 10, (84, 84, 84))
        dibujar_b(screen, inicio_x+self.largo-55, inicio_y + 295, 10, (84, 84, 84))
        dibujar_c(screen, inicio_x +self.largo-55, inicio_y + 265, 10, 10, (84, 84, 84))
        dibujar_d(screen, inicio_x +self.largo-55, inicio_y + 235, 10, 10, (84, 84, 84))
        dibujar_e(screen, inicio_x +self.largo-55, inicio_y + 205, 10, 10, (84, 84, 84))
        dibujar_f(screen, inicio_x +self.largo-55, inicio_y + 175, 10, 10, (84, 84, 84))
        dibujar_g(screen, inicio_x +self.largo-55, inicio_y + 145, 10, 10, (84, 84, 84))
        dibujar_h(screen, inicio_x +self.largo-55, inicio_y + 115, 10, 10, (84, 84, 84))
        dibujar_i(screen, inicio_x +self.largo-55, inicio_y + 85, 10, 10, (84, 84, 84))
        dibujar_j(screen, inicio_x +self.largo-55, inicio_y + 55, 10, 10, (84, 84, 84))
        dibujar_mas(screen, inicio_x + self.largo - 55, inicio_y + 30, 10, (222, 17, 17))
        dibujar_menos(screen, inicio_x + self.largo - 55, inicio_y , (17, 17, 222))
        #fors
        if not self.conectores_creados:
            for i in range(2):
                primer_conector_fila = None  # guarda el primer conector de cada fila
                for j in range(30):
                    x_pos = inicio_x + j * 30
                    y_pos = inicio_y + i * 30
                    nombre_c1 = f"1_{i}_{j}_{self.longitud}" # añadir version
                    conector_existente = None
                    for conector in self.conectores:
                        if conector.nombre == nombre_c1:
                            conector_existente = conector
                            break
                    if conector_existente:
                        conector_existente.x = x_pos
                        conector_existente.y = y_pos
                        conector = conector_existente
                    else:
                        conector = Conector(nombre_c1, x_pos, y_pos, self.conectores)
                        self.conectores.append(conector)
                    if j == 0:
                        primer_conector_fila = conector
                    else:
                        if conector not in primer_conector_fila.conexiones:
                            primer_conector_fila.agregar_conexion(conector)  # si no existe, la agrega
            for i in range(2):
                primer_conector_fila = None
                for j in range(30):
                    x_pos = inicio_x + j * 30
                    y_pos = inicio_y + i * 30
                    nombre_c2 = f"2_{i}_{j}_{self.longitud}"
                    conector_existente = None
                    for conector in self.conectores:
                        if conector.nombre == nombre_c2:
                            conector_existente = conector
                            break
                    if conector_existente:
                        conector_existente.x = x_pos
                        conector_existente.y = y_pos + 360
                        conector = conector_existente
                    else:
                        conector = Conector(nombre_c2, x_pos, y_pos + 360, self.conectores)
                        self.conectores.append(conector)
                    if j == 0:
                        primer_conector_fila = conector
                    else:
                        if conector not in primer_conector_fila.conexiones:
                            primer_conector_fila.agregar_conexion(conector)
            for j in range(30):
                primer_conector_columna = None  # guarda el primer nodo de cada columna
                for i in range(5):
                    y_pos = inicio_y + i * 30
                    x_pos = inicio_x + j * 30
                    nombre_c3 = f"3_{i}_{j}_{self.longitud}"
                    conector_existente = None
                    for conector in self.conectores:
                        if conector.nombre == nombre_c3:
                            conector_existente = conector
                            break
                    if conector_existente:
                        conector_existente.x = x_pos
                        conector_existente.y = y_pos + 60
                        conector = conector_existente
                    else:
                        conector = Conector(nombre_c3, x_pos, y_pos + 60,self.conectores)
                        self.conectores.append(conector)
                    # asigna el primer conector de la columna
                    if i == 0:
                        primer_conector_columna = conector
                    else:
                        # verifica si la conexion ya existe y evita code duplicado
                        if conector not in primer_conector_columna.conexiones:
                            primer_conector_columna.agregar_conexion(conector)  # si no la agrega

                # solo repito el proceso
            for j in range(30):
                primer_conector_columna = None
                for i in range(5):
                    x_pos = inicio_x + j * 30
                    y_pos = inicio_y + i * 30
                    nombre_c4 = f"4_{i}_{j}_{self.longitud}"
                    conector_existente = None
                    for conector in self.conectores:
                        if conector.nombre == nombre_c4:
                            conector_existente = conector
                            break
                    if conector_existente:
                        conector_existente.x = x_pos
                        conector_existente.y = y_pos + 210
                        conector = conector_existente
                    else:
                        conector = Conector(nombre_c4, x_pos, y_pos + 210,self.conectores)
                        self.conectores.append(conector)
                    if i == 0:
                        primer_conector_columna = conector
                    else:
                        if conector not in primer_conector_columna.conexiones:
                            primer_conector_columna.agregar_conexion(conector)
            
            self.conectores_creados = True

def dibujar_a(screen, x, y,ancho,alto,color):
    pygame.draw.line(screen, color, (x, y + alto), (x + ancho // 2, y), 2)  # Línea diagonal izquierda
    pygame.draw.line(screen, color, (x + ancho // 2, y), (x + ancho, y + alto), 2)  # Línea diagonal derecha
    pygame.draw.line(screen, color, (x + ancho // 4, y + alto // 2), (x + ancho - ancho // 4, y + alto // 2),2)  # Barra horizontal
def dibujar_b(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), ((x + alto // 2), y), 2)
    pygame.draw.line(screen, color, ((x + alto // 2), y), ((x + alto // 2), (y + ((alto // 2)-3))), 2)
    pygame.draw.line(screen, color, (x+alto//2, (y + ((alto // 2)-3))), ((x), (y + ((alto // 2)-3))), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + alto//2), (y + alto)), 2)
    pygame.draw.line(screen, color, ((x + alto//2), (y+alto)), ((x + alto//2), (y+(alto//2))), 2)
    pygame.draw.line(screen,color,((x + alto//2), (y+(alto//2))),(x,y+alto//2),2)
def dibujar_c(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x,( y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x+ancho), y), 2)
    pygame.draw.line(screen, color, ((x+ancho), y), ((x +ancho), (y+(alto//3))), 2)
    pygame.draw.line(screen, color, (x, (y+alto)), ((x+ancho), (y+alto)), 2)
    pygame.draw.line(screen, color, ((x+ancho), (y+alto)), ((x +ancho), (y+alto-(alto//3))), 2)
def dibujar_d(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), (x+alto//5,y), 2)
    pygame.draw.line(screen, color, (x+alto//5 , y), (x + ancho, y + alto), 2)
    pygame.draw.line(screen, color, (x,(y+alto)), (x + ancho, y + alto), 2)
def dibujar_e(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x,(y+(alto//2))), ((x + ancho), (y + alto//2)), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
def dibujar_f(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x,(y+alto//2)), ((x + ancho), (y + alto//2)), 2)
def dibujar_g(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x,( y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x+ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y+alto)), ((x+ancho), (y+alto)), 2)
    pygame.draw.line(screen, color, ((x+ancho), (y+alto)), ((x +ancho), (y+alto-alto//3)), 2)
    pygame.draw.line(screen,color,((x+ancho),(y+alto//2)),(x+alto//3,(y+alto//2)),2)
def dibujar_h(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, (x, y), (x, (y + alto)), 2)
    pygame.draw.line(screen, color, (x,(y+alto//2)), ((x + ancho), (y + alto//2)), 2)
    pygame.draw.line(screen, color, (x+ancho, y), (x+ancho, (y + alto)), 2)
def dibujar_i(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, ((x+(ancho//2)), y), ((x+(ancho//2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho), (y + alto)), 2)
def dibujar_j(screen,x,y,alto,ancho,color):
    pygame.draw.line(screen, color, ((x+(ancho//2)), y), ((x+(ancho//2)), (y + alto)), 2)
    pygame.draw.line(screen, color, (x, y), ((x + ancho), y), 2)
    pygame.draw.line(screen, color, (x, (y + alto)), ((x + ancho//2), (y + alto)), 2)
def dibujar_mas(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+alto,y),2)
    pygame.draw.line(screen,color,(x+5,y-5),(x+5,y+5),2)
def dibujar_menos(screen,x,y,color):
    pygame.draw.line(screen, color, (x + 5, y - 5), (x + 5, y + 5), 2)
def dibujar_1(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x+5,y+10),2)
    pygame.draw.line(screen,color,(x,y),(x+alto,y),2)
def dibujar_2(screen,x,y,alto,color):
    pygame.draw.line(screen,color,(x,y),(x,y+alto),2)
    pygame.draw.line(screen,color,(x,y),(x+5,y),2)
    pygame.draw.line(screen, color, (x+5, y), (x + 5, y+alto), 2)
    pygame.draw.line(screen, color, (x+5, y+alto), (x +alto, y+alto), 2)
    pygame.draw.line(screen, color, (x+alto, y+alto), (x+alto,y), 2)
def dibujar_3(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x +alto, y), 2)
    pygame.draw.line(screen, color, (x, y), (x,y+alto), 2)
    pygame.draw.line(screen, color, (x+5, y), (x + 5, y+alto), 2)
    pygame.draw.line(screen, color, (x+alto, y+alto), (x+alto, y), 2)
def dibujar_4(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x + alto, y), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x, y), (x + 5, y+alto), 2)
def dibujar_5(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y+alto), (x+5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x + 5, y + alto), 2)
    pygame.draw.line(screen, color, (x + 5, y), (x +alto, y ), 2)
    pygame.draw.line(screen, color, (x + alto, y + alto), (x + alto, y), 2)
def dibujar_0(screen,x,y,alto,color):
    pygame.draw.line(screen, color, (x, y), (x, y + alto), 2)
    pygame.draw.line(screen, color, (x, y + alto), (x + alto, y + alto), 2)
    pygame.draw.line(screen, color, (x + alto, y+alto), (x + alto, y ), 2)
    pygame.draw.line(screen, color, (x, y), (x+alto, y), 2)
