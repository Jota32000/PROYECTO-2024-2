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

                    pygame.draw.line(screen, "green", (conector.x, conector.y),
                                     (conector.x + conector.largo, conector.y), 6)
                else:
                    # dibuja con el color normal del conector
                    pygame.draw.line(screen, conector.color, (conector.x, conector.y),
                                     (conector.x + conector.largo, conector.y),6)

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo) # conexion bidireccional A->B | B->A
        nodo.conexiones.append(self)
        self.actualizarbosque(self, nodo)

    def eliminar_conexion(self,nodo, nodo_objetivo):
        if nodo_objetivo in self.conexiones: # ve que no se haya eliminado ya la conexion con ese nodo
            nodo.conexiones.remove(nodo_objetivo)
            nodo_objetivo.conexiones.remove(nodo)
            self.buscar_conexiones(nodo, nodo_objetivo)

    def activar_explosion(self,screen,inicio_cable,conector_siguiente,conectores):
        print("ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ")
        print("                   NUKE")
        print("∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨")
        screen.fill((243, 190, 49))
        pygame.display.flip()
        pygame.time.delay(100)

        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.delay(100)
        #----- QUITAR OBJETOS -----

        for nodo in conectores:
            if inicio_cable.nombre.startswith("pila") and conector_siguiente.nombre.startswith("pila"):
                # bloquea conector de pila
                if nodo == conector_siguiente:
                    nodo.block = True

            elif conector_siguiente.nombre.startswith(("conector1_", "conector2_")):
                # block pistas
                if nodo.y == conector_siguiente.y:
                    if inicio_cable.nombre.startswith(("conector1_", "conector2_")) or self.inicio_cable.nombre.startswith(("conector3_", "conector4_")):
                        nodo.block = True

            elif conector_siguiente.nombre.startswith(("conector3_", "conector4_")):
                # Block columna 3 o 4
                if nodo.x == conector_siguiente.x:
                    if conector_siguiente.nombre.startswith("conector3_") and nodo.nombre.startswith("conector3_"):
                        nodo.block = True
                    elif conector_siguiente.nombre.startswith("conector4_") and nodo.nombre.startswith("conector4_"):
                        nodo.block = True
        #--------- FIN ---------
        return

    def actualizarbosque(self, origen, destino):
        if origen.padre != destino.padre:
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
            for i in visitados:
                i.padre = nodo

    def energy_protoboard(self, pila_turno):
        for nodo in self.conectores: # ve los padres de p+ y p- segun eso da energy o no
            if pila_turno.nombre == "pila+":
                if nodo.padre.nombre == pila_turno.padre.nombre:
                    nodo.fase = True
                    nodo.neutro = False
                else:
                    nodo.fase = False
            if pila_turno.nombre == "pila-":
                if nodo.padre.nombre == pila_turno.padre.nombre:
                    nodo.fase = False
                    nodo.neutro = True
                else:
                    nodo.neutro = False