import pygame

class Resistencia:
    def __init__(self):
        self.dibujando_resistencia = False
        self.inicio_resistencia = None

    def dibujar_resistencia(self,screen,resistencias):
        color = (251, 179, 92)
        for resistencia in resistencias:  # cables = Resistencia
            pygame.draw.line(screen, "dark gray", (resistencia[0].x, resistencia[0].y),
                             (resistencia[1].x, resistencia[1].y), 3)
            x_medio = (resistencia[0].x + resistencia[1].x) // 2
            y_medio = (resistencia[0].y + resistencia[1].y) // 2
            if resistencia[0].x - resistencia[1].x == 0:
                # Dibujo concreto de resistencia de forma vertical
                pygame.draw.line(screen, color, (x_medio + 10, y_medio + 15), (x_medio + 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio + 10), (x_medio + 5, y_medio + 5), 3)
                pygame.draw.line(screen, color, (x_medio + 5, y_medio + 5), (x_medio + 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio + 5, y_medio - 5), (x_medio + 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio - 10), (x_medio + 10, y_medio - 15), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio - 15), (x_medio - 10, y_medio - 15), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio - 15), (x_medio - 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio - 10), (x_medio - 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio - 5), (x_medio - 5, y_medio + 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio + 5), (x_medio - 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio + 10), (x_medio - 10, y_medio + 15), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio + 15), (x_medio + 10, y_medio + 15), 3)

                # Ciclos para rellenar interior
                for i in range(10):
                    pygame.draw.line(screen, color, (x_medio - 5 + i, y_medio - 15), (x_medio - 5 + i, y_medio + 15), 3)
                for i in range(5):
                    pygame.draw.line(screen, color, (x_medio - 10 + i, y_medio - 15 + i),
                                     (x_medio - 10 + i, y_medio - 15 + 2 * i), 3)
                    pygame.draw.line(screen, color, (x_medio - 10 + i, y_medio + 15 - i),
                                     (x_medio - 10 + i, y_medio + 15 - 2 * i), 3)
                    pygame.draw.line(screen, color, (x_medio + 10 - i, y_medio + 15 - i),
                                     (x_medio + 10 - i, y_medio + 15 - 2 * i), 3)
                    pygame.draw.line(screen, color, (x_medio + 10 - i, y_medio - 15 + i),
                                     (x_medio + 10 - i, y_medio - 15 + 2 * i), 3)

                # Lineas para determinar niveles de ohm
                pygame.draw.line(screen, "red", (x_medio - 5, y_medio - 3), (x_medio + 5, y_medio - 3), 3)
                pygame.draw.line(screen, "dark green", (x_medio - 5, y_medio + 4), (x_medio + 5, y_medio + 4), 3)
                pygame.draw.line(screen, "blue", (x_medio - 10, y_medio - 10), (x_medio + 10, y_medio - 10), 3)
                pygame.draw.line(screen, "yellow", (x_medio - 10, y_medio + 10), (x_medio + 10, y_medio + 10), 1)

            else:
                pygame.draw.line(screen, color, (x_medio + 5, y_medio + 5), (x_medio - 5, y_medio + 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio + 5), (x_medio - 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio + 10), (x_medio - 15, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio - 15, y_medio + 10), (x_medio - 15, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio - 15, y_medio - 10), (x_medio - 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio - 10, y_medio - 10), (x_medio - 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio - 5, y_medio - 5), (x_medio + 5, y_medio - 5), 3)
                pygame.draw.line(screen, color, (x_medio + 5, y_medio - 5), (x_medio + 10, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio - 10), (x_medio + 15, y_medio - 10), 3)
                pygame.draw.line(screen, color, (x_medio + 15, y_medio - 10), (x_medio + 15, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio + 15, y_medio + 10), (x_medio + 10, y_medio + 10), 3)
                pygame.draw.line(screen, color, (x_medio + 10, y_medio + 10), (x_medio + 5, y_medio + 5), 3)

                # Ciclos para rellenar interior
                for i in range(10):
                    pygame.draw.line(screen, color, (x_medio - 15, y_medio - 5 + i), (x_medio + 15, y_medio - 5 + i), 3)
                for i in range(5):
                    pygame.draw.line(screen, color, (x_medio - 15 + i, y_medio - 10 + i),
                                     (x_medio - 15 + 2 * i, y_medio - 10 + i), 3)
                    pygame.draw.line(screen, color, (x_medio + 15 - i, y_medio - 10 + i),
                                     (x_medio + 15 - 2 * i, y_medio - 10 + i), 3)
                    pygame.draw.line(screen, color, (x_medio + 15 - i, y_medio + 10 - i),
                                     (x_medio + 15 - 2 * i, y_medio + 10 - i), 3)
                    pygame.draw.line(screen, color, (x_medio - 15 + i, y_medio + 10 - i),
                                     (x_medio - 15 + 2 * i, y_medio + 10 - i), 3)

                # Lineas para determinar niveles de ohm
                pygame.draw.line(screen, "red", (x_medio + 4, y_medio - 5), (x_medio + 4, y_medio + 5), 3)
                pygame.draw.line(screen, "dark green", (x_medio - 3, y_medio - 5), (x_medio - 3, y_medio + 5), 3)
                pygame.draw.line(screen, "blue", (x_medio - 10, y_medio - 10), (x_medio - 10, y_medio + 10), 3)
                pygame.draw.line(screen, "yellow", (x_medio + 10, y_medio - 10), (x_medio + 10, y_medio + 10), 1)

    def comienzo_resistencia(self, conector_origen):
        self.inicio_resistencia = conector_origen
        self.dibujando_resistencia = True

    def energy_protoboard(self, pila_turno,conectores):
        for nodo in conectores:  # ve los padres de p+ y p- segun eso da energy o no
            if pila_turno.nombre == "pila+":
                if nodo.padre.nombre == pila_turno.padre.nombre:
                    nodo.fase = True
                    nodo.neutro = False
                else:
                    nodo.fase = False
            elif pila_turno.nombre == "pila-":
                if nodo.padre.nombre == pila_turno.padre.nombre:
                    nodo.fase = False
                    nodo.neutro = True
                else:
                    nodo.neutro = False

    def finalizar_resistencia(self, conector_siguiente,conectores,resistencias):
        if self.inicio_resistencia.nombre == conector_siguiente.nombre:
            print("----------------------------")
            print("Selecciono un punto")
            print("Eso no es valido")
            print("----------------------------")
            self.dibujando_resistencia = False
            self.inicio_resistencia = None
            return

        if ((self.inicio_resistencia.fase and conector_siguiente.neutro) or (
                self.inicio_resistencia.neutro and conector_siguiente.fase)):
            print("----------------------------------")
            print("Corto de pixar")
            print("No puede conectar neutro y fase")
            print("----------------------------------")
            self.activar_explosion()
            self.dibujando_resistencia = False
            self.inicio_resistencia = None
            return

        if "pila" in self.inicio_resistencia.nombre and conector_siguiente.nombre.startswith(
                ("conector3_", "conector4_")):
            print("-------------------------------------------")
            print("La resistencia de la pila solo van en los buses")
            print("-------------------------------------------")
            self.dibujando_resistencia = False
            self.inicio_resistencia = None
            return

        for resistencia in resistencias:
            if self.inicio_resistencia in resistencia or conector_siguiente in resistencia:
                print("-------------------------------------------")
                print("Ya hay una resistencia en este nodo")
                print("-------------------------------------------")
                self.dibujando_resistencia = False
                self.inicio_resistencia = None
                return

        if (
                self.inicio_resistencia.x - conector_siguiente.x == 60 or conector_siguiente.x - self.inicio_resistencia.x == 60) or (
                self.inicio_resistencia.y - conector_siguiente.y == 60 or conector_siguiente.y - self.inicio_resistencia.y == 60):
            # print("Origen: ",self.inicio_resistencia.x,self.inicio_resistencia.y)
            # print("Destino: ",conector_siguiente.x,conector_siguiente.y)
            resistencias.append((self.inicio_resistencia, conector_siguiente))
        else:
            print("Lo siento, sus dimensiones no son las recomendadas")
            self.dibujando_resistencia = False
            self.inicio_resistencia = None
            return

        # ------------------ Fin Validaciones de resistencia ------------------- #
        # si coloco de c3/c4 a c1 o c2 se pase la energia de fila a columna
        if (self.inicio_resistencia.nombre.startswith(("conector3_", "conector4_")) and
                conector_siguiente.nombre.startswith(("conector1_", "conector2_"))):

            for nodo in conectores:
                if nodo.y == conector_siguiente.y:
                    self.inicio_resistencia.agregar_conexion(nodo)

            # ---------------- Fin validacion fila columna -------------------

        elif self.inicio_resistencia.nombre in ["pila+", "pila-"]:
            for nodo in conectores:
                if nodo.y == conector_siguiente.y:  # misma fila (solo c1 y c2)
                    self.inicio_resistencia.agregar_conexion(nodo)

        elif self.inicio_resistencia.nombre.startswith(
                ("conector1_", "conector2_")) and conector_siguiente.nombre.startswith(("pila")):
            for nodo in conectores:
                if nodo.y == self.inicio_resistencia.y:  # misma fila (solo c1 y c2)
                    conector_siguiente.agregar_conexion(nodo)

        else:
            for nodo in conectores:
                if nodo.x == conector_siguiente.x:  # ver si estan en la misma columna | se limita el alcance
                    if conector_siguiente.nombre.startswith("conector3_"):
                        if nodo.nombre.startswith("conector3_") and nodo.nombre != self.inicio_resistencia.nombre:
                            self.inicio_resistencia.agregar_conexion(nodo)
                    elif conector_siguiente.nombre.startswith("conector4_"):  # limita el rango de add solo a c4_
                        if nodo.nombre.startswith("conector4_") and nodo.nombre != self.inicio_resistencia.nombre:
                            self.inicio_resistencia.agregar_conexion(nodo)

        self.dibujando_resistencia = False
        self.inicio_resistencia = None

    def dibujar_resistencia_actual(self,screen):
        if self.dibujando_resistencia and self.inicio_resistencia:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, "dark gray", (self.inicio_resistencia.x, self.inicio_resistencia.y), current_pos,
                             3)

    def actualizarbosque(self, origen, destino,conectores):
        if origen.padre != destino.padre:
            coincidencia_origen = 0
            for nodo in conectores:
                if nodo.padre == origen.padre:
                    coincidencia_origen += 1

            coincidencia_destino = 0
            for nodo in conectores:
                if nodo.padre == destino.padre:
                    coincidencia_destino += 1

            if coincidencia_origen >= coincidencia_destino:
                nuevo_padre = origen.padre
                viejo_padre = destino.padre
            else:
                nuevo_padre = destino.padre
                viejo_padre = origen.padre

            self.actualizar_padre_subarbol(viejo_padre, nuevo_padre)

    def actualizar_padre_subarbol(self, viejo_padre, nuevo_padre,conectores):
        for nodo in conectores:
            if nodo.padre == viejo_padre:
                nodo.padre = nuevo_padre

    def buscar_conexiones(self, nodo, nodo_objetivo):
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

    def activar_explosion(self,screen,conectores,cables,guardar_led,guardar_switch):
        print("ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ")
        print("                   NUKE")
        print("∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨ʌ∨")
        global boton_cable
        boton_cable = False
        screen.fill((243, 190, 49))
        pygame.display.flip()
        pygame.time.delay(100)

        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.delay(100)
        # ----- QUITAR OBJETOS -----
        for nodo in conectores:
            if not nodo.nombre.startswith("pila"):
                nodo.fase = False
                nodo.neutro = False
            nodo.padre = nodo

        cables.clear()
        guardar_led.clear()
        guardar_switch.clear()
        # --------- FIN ---------
        return