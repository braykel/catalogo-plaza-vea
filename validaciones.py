

def codigo_valido(codigo):
    """Verifica que el código no esté vacío."""
    return bool(codigo and codigo.strip())

def cantidad_valida(cantidad):
    """Verifica que la cantidad sea un entero no negativo."""
    return isinstance(cantidad, int) and cantidad >= 0

def precio_valido(precio):
    """Verifica que el precio sea un número positivo."""
    return isinstance(precio, (int, float)) and precio > 0

def existe_codigo(catalogo, codigo):
    """Verifica si un código ya existe en el catálogo."""
    return any(p["codigo"] == codigo for p in catalogo)