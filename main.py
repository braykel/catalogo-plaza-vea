

from persistencia import cargar_catalogo, guardar_catalogo
from operaciones import (
    registrar_producto,
    actualizar_producto,
    buscar_producto,
    listar_catalogo
)

ARCHIVO = "catalogo.txt"

def mostrar_menu():
    """Muestra el menú de opciones en pantalla."""
    print("\n===== CATÁLOGO PLAZA VEA =====")
    print("1. Registrar producto")
    print("2. Actualizar producto")
    print("3. Buscar producto")
    print("4. Listar catálogo")
    print("5. Guardar cambios")
    print("6. Salir")

def main():
    """Función principal del programa."""
    catalogo = cargar_catalogo(ARCHIVO)

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar_producto(catalogo)
        elif opcion == "2":
            actualizar_producto(catalogo)
        elif opcion == "3":
            buscar_producto(catalogo)
        elif opcion == "4":
            listar_catalogo(catalogo)
        elif opcion == "5":
            guardar_catalogo(catalogo, ARCHIVO)
        elif opcion == "6":
            guardar_catalogo(catalogo, ARCHIVO)
            print("Saliendo del sistema...")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()