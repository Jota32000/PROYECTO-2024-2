import pygame
class Conector:
    def __init__(self, nombre, x, y,conectores):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.fase = None
        self.neutro = None
        self.block= False
        self.largo = 5
        self.color = (84, 84, 84)
        self.conexiones = []
        self.padre = self
        self.conectores=conectores
        self.ocupado=False

    def dibujar(self,screen):
        #dibuja los puntos de la protoboard
        for conector in self.conectores:
            if not conector.nombre.startswith("pila"):
                if conector.fase and not conector.block:
                    pygame.draw.line(screen, "red", (conector.x, conector.y), (conector.x + conector.largo, conector.y),
                                     6)
                elif conector.neutro and not conector.block:
                    pygame.draw.line(screen, "blue", (conector.x, conector.y),
                                     (conector.x + conector.largo, conector.y), 6)
                elif conector.block:
                    conector.padre = conector

                    pygame.draw.line(screen, "orange", (conector.x, conector.y),
                                     (conector.x + conector.largo, conector.y), 6)
                else:
                    # dibuja con el color normal del conector
                    pygame.draw.line(screen, conector.color, (conector.x, conector.y),
                                     (conector.x + conector.largo, conector.y),6)
    def agregar_conexion(self, nodo):
        if (self.fase or self.neutro) and (nodo.fase or nodo.neutro):
            end = nodo
            if end.nombre.startswith(("1_", "2_")):
                for nodo in self.conectores:
                    if nodo.y == end.y:
                        nodo.block = True
                        nodo.eliminar_conexion(nodo, end)
                        for i in end.conexiones:
                            end.eliminar_conexion(end, i)
                self.conectores[0].padre = self.conectores[0]
                self.conectores[0].fase = True
                self.conectores[1].padre = self.conectores[1]
                self.conectores[1].neutro = True
            # -------------------- elimina columnas ------------------------
            else:
                for nodo in self.conectores:
                    if nodo.x == end.x:
                        if end.nombre.startswith("3_"):
                            if nodo.nombre.startswith("3_"):
                                nodo.block = True
                                nodo.eliminar_conexion(nodo, end)
                                for i in end.conexiones:
                                    if i.nombre.startswith("3_"):
                                        end.eliminar_conexion(end, i)
                        elif end.nombre.startswith("4_"):
                            if nodo.nombre.startswith("4_"):
                                nodo.block = True
                                nodo.eliminar_conexion(nodo, end)
                                for i in end.conexiones:
                                    if i.nombre.startswith("4_"):
                                        end.eliminar_conexion(end, i)
                self.conectores[0].padre = self.conectores[0]
                self.conectores[0].fase = True
                self.conectores[1].padre = self.conectores[1]
                self.conectores[1].neutro = True
        else:
            self.conexiones.append(nodo)  # conexion bidireccional A->B | B->A
            nodo.conexiones.append(self)
            self.actualizarbosque(self, nodo)
    def eliminar_conexion(self,nodo, nodo_objetivo):
        if (nodo_objetivo in self.conexiones) : # ve que no se haya eliminado ya la conexion con ese nodo
            nodo.conexiones.remove(nodo_objetivo)
            nodo_objetivo.conexiones.remove(nodo)
            self.buscar_conexiones(nodo, nodo_objetivo)
    def actualizarbosque(self, origen, destino):
        if origen.padre != destino.padre:
            if origen.padre.nombre.startswith("pila"):
                nuevo_padre = origen.padre
                viejo_padre = destino.padre
            elif destino.padre.nombre.startswith("pila"):
                nuevo_padre = destino.padre
                viejo_padre = origen.padre
            else:
                coincidencia_origen = 0
                for nodo in self.conectores:
                    if nodo.padre == origen.padre:
                        coincidencia_origen += 1

                coincidencia_destino = 0
                for nodo in self.conectores:
                    if nodo.padre == destino.padre:
                        coincidencia_destino += 1

                if coincidencia_origen >= coincidencia_destino:
                    nuevo_padre = origen.padre
                    viejo_padre = destino.padre
                else:
                    nuevo_padre = destino.padre
                    viejo_padre = origen.padre
            self.actualizar_padre_subarbol(viejo_padre, nuevo_padre)

    def actualizar_padre_subarbol(self, viejo_padre, nuevo_padre):
        for nodo in self.conectores:
            if nodo.padre == viejo_padre:
                nodo.padre = nuevo_padre
                if not nodo.block:
                    print(nodo.nombre)
                    nodo.fase = nuevo_padre.fase
                    nodo.neutro = nuevo_padre.neutro
    def buscar_conexiones(self,nodo, nodo_objetivo):
        visitados = []
        conneciones = []
        conneciones.append(nodo)
        existe_conexion_alternativa = False
        while (len(conneciones) > 0):
            actual = conneciones.pop(0)
            for i in actual.conexiones:
                if i not in visitados:
                    conneciones.append(i)
            visitados.append(actual)
            if nodo_objetivo in nodo.conexiones:
                existe_conexion_alternativa = True
        if existe_conexion_alternativa:
            for i in visitados:
                i.padre = nodo_objetivo
        else:
            nodo.padre = nodo
            nodo.fase = None
            nodo.neutro = None
            for i in visitados:
                i.padre = nodo
                i.fase = None
                i.neutro = None
