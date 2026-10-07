

def cargar_catalogo(ruta):
    """Carga los productos desde el archivo de texto."""
    catalogo = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) == 4:
                    catalogo.append({
                        "codigo": partes[0],
                        "descripcion": partes[1],
                        "cantidad": int(partes[2]),
                        "precio": float(partes[3])
                    })
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
    return catalogo

def guardar_catalogo(catalogo, ruta):
    """Guarda los productos en el archivo de texto."""
    with open(ruta, "w", encoding="utf-8") as f:
        for p in catalogo:
            f.write(f"{p['codigo']};{p['descripcion']};{p['cantidad']};{p['precio']}\n")
    print("✔ Catálogo guardado correctamente.")