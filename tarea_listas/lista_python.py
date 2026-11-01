from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):
        # Mejora: no permitir números repetidos
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- Operaciones de la tabla 3.2 ----------------
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print(f"  ⚠ Posición inválida (debe estar entre 0 y {len(self.pasajeros)})")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        coincidencias = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        return coincidencias[0] if coincidencias else -1

    def buscar_binaria(self, numero):
        # Requiere la lista ordenada por numero
        numeros = [p.numero for p in self.pasajeros]
        i = bisect_left(numeros, numero)
        if i < len(numeros) and numeros[i] == numero:
            return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print(f"  ⚠ Posición inválida (debe estar entre 0 y {len(self.pasajeros) - 1})")
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        antes = len(self.pasajeros)
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    def mayores_de_edad(self):                        # solo Lista 2
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]
