
from validaciones import (
    codigo_valido,
    cantidad_valida,
    precio_valido,
    existe_codigo
)

def registrar_producto(catalogo):
    """Registra un nuevo producto en el catálogo."""
    codigo = input("Código: ").strip()
    if not codigo_valido(codigo):
        print("Código inválido.")
        return
    if existe_codigo(catalogo, codigo):
        print("El código ya existe.")
        return

    descripcion = input("Descripción: ").strip()
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
    except ValueError:
        print("Datos numéricos inválidos.")
        return

    if not cantidad_valida(cantidad) or not precio_valido(precio):
        print("Cantidad y precio deben ser positivos.")
        return

    catalogo.append({
        "codigo": codigo,
        "descripcion": descripcion,
        "cantidad": cantidad,
        "precio": precio
    })
    print(" Producto registrado.")

def actualizar_producto(catalogo):
    """Actualiza cantidad y precio de un producto existente."""
    codigo = input("Código a actualizar: ").strip()
    for p in catalogo:
        if p["codigo"] == codigo:
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
                nuevo_precio = float(input("Nuevo precio: "))
            except ValueError:
                print("Datos inválidos.")
                return
            if not cantidad_valida(nueva_cantidad) or not precio_valido(nuevo_precio):
                print("Cantidad y precio deben ser positivos.")
                return
            p["cantidad"] = nueva_cantidad
            p["precio"] = nuevo_precio
            print("✔ Producto actualizado.")
            return
    print("Producto no encontrado.")

def buscar_producto(catalogo):
    """Busca un producto por código y muestra sus datos."""
    codigo = input("Código a buscar: ").strip()
    for p in catalogo:
        if p["codigo"] == codigo:
            print(f"\nCódigo: {p['codigo']}")
            print(f"Descripción: {p['descripcion']}")
            print(f"Cantidad: {p['cantidad']}")
            print(f"Precio: S/ {p['precio']:.2f}\n")
            return
    print("Producto no encontrado.")

def listar_catalogo(catalogo):
    """Lista todos los productos del catálogo en formato tabla."""
    if not catalogo:
        print("Catálogo vacío.")
        return
    print(f"\n{'CÓDIGO':<10}{'DESCRIPCIÓN':<25}{'CANT.':<10}{'PRECIO':<10}")
    print("-" * 55)
    for p in catalogo:
        print(f"{p['codigo']:<10}{p['descripcion']:<25}{p['cantidad']:<10}{p['precio']:<10.2f}")
    print(f"\nTotal de productos: {len(catalogo)}\n")