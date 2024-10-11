import pygame

from Conector import *


class Cableado:
    def __init__(self,conectores,cables):
        self.dibujando_cable = False
        self.inicio_cable = None
        self.conectores=conectores
        self.cables=cables

    def dibujar_cables(self,screen,cable):
        # verificar fase y neutro sino da problemas
        conector_inicio, conector_fin = cable
        if conector_inicio.fase or conector_inicio.neutro or conector_fin.fase or conector_fin.neutro:
            if conector_inicio.fase and conector_fin.fase:
                color = (234, 79, 235) # morado
            elif conector_inicio.neutro and conector_fin.neutro:
                color = (61, 205, 234) # azul cielo dark
            else:
                color = "black"
        else:
            color = "black"
        pygame.draw.line(screen, color, (cable[0].x, cable[0].y), (cable[1].x, cable[1].y), 3)

    def comienzo_cable(self, conector_origen):
        self.inicio_cable = conector_origen
        self.dibujando_cable = True


    def finalizar_cable(self, screen,conector_siguiente):
        if self.inicio_cable.nombre == conector_siguiente.nombre:
            print("----------------------------")
            print("Selecciono un punto")
            print("Eso no es valido")
            print("----------------------------")
            self.dibujando_cable = False
            self.inicio_cable = None
            return

        if "pila" in self.inicio_cable.nombre and conector_siguiente.nombre.startswith(("conector3_", "conector4_")):
            print("-------------------------------------------")
            print("Los cables de la pila solo van en los buses")
            print("-------------------------------------------")
            self.dibujando_cable = False
            self.inicio_cable = None
            return

        if not self.quitar_cable(self.inicio_cable, conector_siguiente):
            for cable in self.cables:
                if self.inicio_cable in cable or conector_siguiente in cable:
                    print("-------------------------------------------")
                    print("Ya hay un cable en este nodo")
                    print("-------------------------------------------")
                    self.dibujando_cable = False
                    self.inicio_cable = None
                    return

                if ((self.inicio_cable.fase and conector_siguiente.neutro) or
                        (self.inicio_cable.neutro and conector_siguiente.fase) or
                        (self.inicio_cable.fase and conector_siguiente.fase) or
                        (self.inicio_cable.neutro and conector_siguiente.neutro)):
                    print("----------------------------------")
                    print("Corto de pixar")
                    print("No puede conectar neutro y fase")
                    print("posible error aqui")
                    print("----------------------------------")
                    Conector.activar_explosion(self,screen,self.inicio_cable, conector_siguiente)
                    self.dibujando_cable = False
                    self.inicio_cable = None
                    return
            # ------------------ Fin Validaciones de cables -------------------

            self.cables.append((self.inicio_cable, conector_siguiente))

            for nodo in self.conectores:
                # si se conecta de c3/c4 a c1/c2 se transfiere la energia de la fila a la columna
                if (self.inicio_cable.nombre.startswith(("conector3_", "conector4_")) and
                        conector_siguiente.nombre.startswith(("conector1_", "conector2_"))):
                    if nodo.y == conector_siguiente.y:
                        self.inicio_cable.agregar_conexion(nodo)

                # si se conecta desde una pila
                elif self.inicio_cable.nombre in ["pila+", "pila-"]:
                    if nodo.y == conector_siguiente.y:  # misma fila (solo c1 y c2)
                        self.inicio_cable.agregar_conexion(nodo)

                # conectar desde conector1 o conector2 hacia una pila
                elif self.inicio_cable.nombre.startswith(("conector1_", "conector2_")) and conector_siguiente.nombre.startswith("pila"):
                    if nodo.y == self.inicio_cable.y:  # misma fila (solo c1 y c2)
                        conector_siguiente.agregar_conexion(nodo)

                # validar conexiones entre columnas en conector3 o conector4
                elif nodo.x == conector_siguiente.x:  # misma columna
                    if conector_siguiente.nombre.startswith("conector3_") and nodo.nombre.startswith(
                            "conector3_") and nodo.nombre != self.inicio_cable.nombre:
                        self.inicio_cable.agregar_conexion(nodo)
                    elif conector_siguiente.nombre.startswith("conector4_") and nodo.nombre.startswith(
                            "conector4_") and nodo.nombre != self.inicio_cable.nombre:
                        self.inicio_cable.agregar_conexion(nodo)
        self.dibujando_cable = False
        self.inicio_cable = None

    def quitar_cable(self, start,end):
        for cable in self.cables:
            if (cable[0] == start and cable[1] == end) or (cable[0] == end and cable[1] == start):
                self.cables.remove(cable)
                if start and end:
                    # elimina la conexión entre start y end
                    start.eliminar_conexion(start, end)
                    end.eliminar_conexion(end, start)

                    if self.inicio_cable.nombre.startswith("pila"):
                        end.padre = end
                        self.inicio_cable.padre = self.inicio_cable

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
                return True
        return False

    def dibujar_cable_actual(self,screen,conector_mas,conector_menos):
        if self.dibujando_cable and self.inicio_cable:
            current_pos = pygame.mouse.get_pos()
            if self.inicio_cable.fase:
                color = (234, 79, 235)
            elif self.inicio_cable.neutro:
                color = (61, 205, 234)
            else:
                color = "black"
            pygame.draw.line(screen, color, (self.inicio_cable.x, self.inicio_cable.y), current_pos, 3)

        for c in self.conectores:  # busca las pilas y las envia a cambiar o no estado fase / neutro
            if c.nombre == "pila+":
                if not c.conexiones:
                    c.padre = c
                Conector.energy_protoboard(self,conector_mas)

            if c.nombre == "pila-":
                if not c.conexiones:
                    c.padre = c
                Conector.energy_protoboard(self,conector_menos)