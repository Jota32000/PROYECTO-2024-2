import pygame

class Chip:
    def __init__(self,conector):
        self.x=conector.x
        self.y=conector.y
        self.ancho=27
        self.largo=190
        self.color_cuerpo=(53, 46, 46 )
        self.dis=10
        self.lado=30
        self.pin1 = conector
        self.pin2 = None
        self.pin3 = None
        self.pin4 = None
        self.pin5 = None
        self.pin6 = None
        self.pin7 = None
        self.pin8 = None
        self.pin9 = None
        self.pin10 = None
        self.pin11 = None
        self.pin12 = None
        self.pin13 = None
        self.pin14 = None
    def dibujar(self, screen):
        # Patas superiores
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.dis), 2)  # pin 1 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y), (self.x + self.lado, self.y + self.dis),
                         2)  # pin 2 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 2), self.y),
                         (self.x + (self.lado * 2), self.y + self.dis), 2)  # pin 3 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 3), self.y),
                         (self.x + (self.lado * 3), self.y + self.dis), 2)  # pin 4 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 4), self.y),
                         (self.x + (self.lado * 4), self.y + self.dis), 2)  # pin 5 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 5), self.y),
                         (self.x + (self.lado * 5), self.y + self.dis), 2)  # pin 6 arriba
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 6), self.y),
                         (self.x + (self.lado * 6), self.y + self.dis), 2)  # pin 7 arriba

        # Patas inferiores
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + 30), (self.x, self.y + 20), 2)  # pin 1 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.lado, self.y + 30), (self.x + self.lado, self.y + 20),
                         2)  # pin 2 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 2), self.y + 30),
                         (self.x + (self.lado * 2), self.y + 20), 2)  # pin 3 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 3), self.y + 30),
                         (self.x + (self.lado * 3), self.y + 20), 2)  # pin 4 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 4), self.y + 30),
                         (self.x + (self.lado * 4), self.y + 20), 2)  # pin 5 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 5), self.y + 30),
                         (self.x + (self.lado * 5), self.y + 20), 2)  # pin 6 abajo
        pygame.draw.line(screen, (0, 0, 0), (self.x + (self.lado * 6), self.y + 30),
                         (self.x + (self.lado * 6), self.y + 20), 2)  # pin 7 abajo

        # Dibujo del cuerpo del objeto con líneas
        for i in range(self.y + 5, self.y + self.ancho):
            pygame.draw.line(screen, self.color_cuerpo, (self.x - 5, i), (self.x + self.largo, i))

    def chip_not(self):
        #dar energia a los pines 3,5,7,9,11 y13
        if (self.pin1.fase==True) and (self.pin2.fase==None) and (self.pin14.neutro==True) and (self.pin3.fase==None):
            self.pin1.agregar_conexion(self.pin3)
        if (self.pin1.fase==True) and (self.pin4.fase==None) and (self.pin14.neutro==True) and (self.pin5.fase==None):
            self.pin1.agregar_conexion(self.pin5)
        if (self.pin1.fase==True) and (self.pin6.fase==None) and (self.pin14.neutro==True) and (self.pin7.fase==None):
            self.pin1.agregar_conexion(self.pin7)
        if (self.pin1.fase==True) and (self.pin8.fase==None ) and (self.pin14.neutro==True) and (self.pin9.fase==None):
            self.pin1.agregar_conexion(self.pin9)
        if (self.pin1.fase==True) and (self.pin10.fase==None ) and (self.pin14.neutro==True) and (self.pin11.fase==None):
            self.pin1.agregar_conexion(self.pin11)
        if (self.pin1.fase==True) and (self.pin12.fase==None ) and (self.pin14.neutro==True) and (self.pin13.fase==None):
            self.pin1.agregar_conexion(self.pin13)
        # quitar energia a los pines 3,5,7,9,11 y13
        if (self.pin1.fase==True) and (self.pin2.fase==True) and (self.pin14.neutro==True) and (self.pin3.fase != None):
            self.pin3.eliminar_conexion(self.pin3,self.pin1)
        if (self.pin1.fase==True) and (self.pin4.fase==True) and (self.pin14.neutro==True) and (self.pin5.fase != None):
            self.pin5.eliminar_conexion(self.pin5,self.pin1)
        if (self.pin1.fase==True) and (self.pin6.fase==True) and (self.pin14.neutro==True) and (self.pin7.fase != None):
            self.pin7.eliminar_conexion(self.pin7,self.pin1)
        if (self.pin1.fase==True) and (self.pin8.fase==True ) and (self.pin14.neutro==True) and (self.pin9.fase != None):
            self.pin9.eliminar_conexion(self.pin9,self.pin1)
        if (self.pin1.fase==True) and (self.pin10.fase==True ) and (self.pin14.neutro==True) and (self.pin11.fase != None):
            self.pin11.eliminar_conexion(self.pin11,self.pin1)
        if (self.pin1.fase==True) and (self.pin12.fase==True ) and (self.pin14.neutro==True) and (self.pin13.fase != None):
            self.pin13.eliminar_conexion(self.pin13,self.pin1)

    def chip_and(self):
        if (self.pin1.fase==True) and (self.pin2.fase==True and self.pin3.fase==True) and (self.pin14.neutro==True) and (self.pin4.fase==None):
            self.pin1.agregar_conexion(self.pin4)
        if (self.pin1.fase==True) and (self.pin5.fase==True and self.pin6.fase==True) and (self.pin14.neutro==True) and (self.pin7.fase==None):
            self.pin1.agregar_conexion(self.pin7)
        if (self.pin1.fase==True) and (self.pin8.fase==True and self.pin9.fase==True) and (self.pin14.neutro==True) and (self.pin10.fase==None):
            self.pin1.agregar_conexion(self.pin10)
        if (self.pin1.fase==True) and (self.pin11.fase==True and self.pin12.fase==True) and (self.pin14.neutro==True) and (self.pin13.fase==None):
            self.pin1.agregar_conexion(self.pin13)
        #eliminar coneccion
        if (self.pin1.fase==True) and (self.pin2.fase==None or self.pin3.fase==None) and (self.pin14.neutro==True) :
            self.pin4.eliminar_conexion(self.pin4, self.pin1)
        if (self.pin1.fase==True) and (self.pin5.fase==None or self.pin6.fase==None) and (self.pin14.neutro==True) :
            self.pin7.eliminar_conexion(self.pin7, self.pin1)
        if (self.pin1.fase==True) and (self.pin8.fase==None or self.pin9.fase==None) and (self.pin14.neutro==True) :
            self.pin10.eliminar_conexion(self.pin10, self.pin1)
        if (self.pin1.fase==True) and (self.pin11.fase==None or self.pin12.fase==None) and (self.pin14.neutro==True) :
            self.pin13.eliminar_conexion(self.pin13, self.pin1)

    def chip_or(self):
        if (self.pin1.fase==True) and (self.pin2.fase==True or self.pin3.fase==True) and (self.pin14.neutro==True) and (self.pin4.fase==None):
            self.pin1.agregar_conexion(self.pin4)
        if (self.pin1.fase==True) and (self.pin5.fase==True or self.pin6.fase==True) and (self.pin14.neutro==True) and (self.pin7.fase==None):
            self.pin1.agregar_conexion(self.pin7)
        if (self.pin1.fase==True) and (self.pin8.fase==True or self.pin9.fase==True) and (self.pin14.neutro==True) and (self.pin10.fase==None):
            self.pin1.agregar_conexion(self.pin10)
        if (self.pin1.fase==True) and (self.pin11.fase==True or self.pin12.fase==True) and (self.pin14.neutro==True) and (self.pin13.fase==None):
            self.pin1.agregar_conexion(self.pin13)
        # eliminar coneccion
        if (self.pin1.fase==True) and (self.pin2.fase==None and self.pin3.fase==None) and (self.pin14.neutro==True) :
            self.pin4.eliminar_conexion(self.pin4, self.pin1)
        if (self.pin1.fase==True) and (self.pin5.fase==None and self.pin6.fase==None) and (self.pin14.neutro==True) :
            self.pin7.eliminar_conexion(self.pin7, self.pin1)
        if (self.pin1.fase==True) and (self.pin8.fase==None and self.pin9.fase==None) and (self.pin14.neutro==True) :
            self.pin10.eliminar_conexion(self.pin10, self.pin1)
        if (self.pin1.fase==True) and (self.pin11.fase==None and self.pin12.fase==None) and (self.pin14.neutro==True) :
            self.pin13.eliminar_conexion(self.pin13, self.pin1)

