from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  ✓ Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")


def mostrar_busqueda(lista, posicion):
    """Muestra el resultado de una búsqueda (lineal o binaria)."""
    if posicion == -1:
        print("  No existe")
    elif hasattr(lista, "datos"):
        print(f"  Encontrado en [{posicion}]: {lista.datos[posicion].nombre}")
    else:
        print(f"  Encontrado en [{posicion}]: {lista.pasajeros[posicion].nombre}")


# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                          # 1. LEER
            if lista1.añadir(pasajero):                         # 2. LLAMAR
                print("  ✓ Pasajero añadido")                   # 3. MOSTRAR

        elif op == "2":
            lista1.listar()

        elif op == "3":
            posicion = leer_entero("  Posición: ")
            pasajero = leer_pasajero()
            if lista1.insertar(posicion, pasajero):
                print(f"  ✓ Pasajero insertado en [{posicion}]")

        elif op == "4":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = lista1.buscar(numero)
            mostrar_busqueda(lista1, posicion)

        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = lista1.buscar_binaria(numero)
            mostrar_busqueda(lista1, posicion)
            print("  (la búsqueda binaria requiere la lista ordenada: usa antes la opción 9)")

        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista1.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            eliminado = lista1.eliminar_por_posicion(posicion)
            if eliminado is not None:
                print(f"  ✓ Eliminado: {eliminado.nombre}; quedan {lista1.longitud()}")

        elif op == "8":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if lista1.eliminar_por_valor(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe")

        elif op == "9":
            lista1.ordenar_asc()
            print("  ✓ Ordenada de menor a mayor")
            lista1.listar()

        elif op == "10":
            lista1.ordenar_desc()
            print("  ✓ Ordenada de mayor a menor")
            lista1.listar()

        elif op == "11":
            lista1.reversar()
            print("  ✓ Lista reversada")
            lista1.listar()

        elif op == "12":
            copia = lista1.copiar()
            copia.reversar()
            print("  Copia (reversada):")
            copia.listar()
            print("  Original (sin cambios):")
            lista1.listar()

        elif op == "13":
            print(f"  Longitud: {lista1.longitud()}")

        elif op == "C":
            cargar_datos_prueba(lista1)

        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                          # 1. LEER
            if lista2.añadir(pasajero):                         # 2. LLAMAR
                print("  ✓ Pasajero añadido")                   # 3. MOSTRAR

        elif op == "2":
            lista2.listar()

        elif op == "3":
            posicion = leer_entero("  Posición: ")
            pasajero = leer_pasajero()
            if lista2.insertar(posicion, pasajero):
                print(f"  ✓ Pasajero insertado en [{posicion}]")

        elif op == "4":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = lista2.buscar(numero)
            mostrar_busqueda(lista2, posicion)

        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = lista2.buscar_binaria(numero)
            mostrar_busqueda(lista2, posicion)
            print("  (la búsqueda binaria requiere la lista ordenada: usa antes la opción 9)")

        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if lista2.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            eliminado = lista2.eliminar_por_posicion(posicion)
            if eliminado is not None:
                print(f"  ✓ Eliminado: {eliminado.nombre}; quedan {lista2.longitud()}")

        elif op == "8":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if lista2.eliminar_por_valor(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe")

        elif op == "9":
            lista2.ordenar_asc()
            print("  ✓ Ordenada de menor a mayor")
            lista2.listar()

        elif op == "10":
            lista2.ordenar_desc()
            print("  ✓ Ordenada de mayor a menor")
            lista2.listar()

        elif op == "11":
            lista2.reversar()
            print("  ✓ Lista reversada")
            lista2.listar()

        elif op == "12":
            copia = lista2.copiar()
            copia.reversar()
            print("  Copia (reversada):")
            copia.listar()
            print("  Original (sin cambios):")
            lista2.listar()

        elif op == "13":
            print(f"  Longitud: {lista2.longitud()}")

        elif op == "14":
            destino = input("  Destino a filtrar: ").strip()
            resultado = lista2.filtrar_por_destino(destino)
            if resultado:
                for p in resultado:
                    print(f"  {p}")
            else:
                print("  Ningún pasajero con ese destino")

        elif op == "15":
            resultado = lista2.mayores_de_edad()
            if resultado:
                for p in resultado:
                    print(f"  {p}")
            else:
                print("  No hay mayores de edad")

        elif op == "C":
            cargar_datos_prueba(lista2)

        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
