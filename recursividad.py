"""Funciones recursivas e iterativas del Laboratorio Tema 7.

Convención usada en todas las funciones sobre entregas:
    * caso base   -> el índice alcanza ``len(entregas)`` (no quedan elementos);
    * caso recursivo -> se procesa el elemento actual y se llama a la función
      con ``indice + 1``, por lo que el problema se reduce en cada llamada.

Las validaciones se ejecutan antes de recursar para evitar índices negativos,
valores negativos y búsquedas vacías.
"""

from collections.abc import Sequence

from datos import Entrega


# ---------------------------------------------------------------- validaciones
def _validar_entero_no_negativo(valor: int, nombre: str) -> None:
    """Rechaza valores que no sean enteros o que sean negativos."""
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise TypeError(f"{nombre} debe ser un entero.")
    if valor < 0:
        raise ValueError(f"{nombre} no puede ser negativo (se recibió {valor}).")


def _validar_texto(valor: str, nombre: str) -> None:
    """Rechaza cadenas vacías o que solo contengan espacios."""
    if not isinstance(valor, str):
        raise TypeError(f"{nombre} debe ser una cadena de texto.")
    if not valor.strip():
        raise ValueError(f"{nombre} no puede estar vacío.")


# ------------------------------------------------------------- 1. sumatorias
def sumatoria_puntajes(entregas: Sequence[Entrega], indice: int = 0) -> int:
    """Suma los puntajes de forma recursiva.

    Caso base:      ``indice == len(entregas)`` -> 0 (no hay más puntajes).
    Caso recursivo: ``puntaje[indice] + sumatoria_puntajes(..., indice + 1)``.
    """
    _validar_entero_no_negativo(indice, "indice")
    if indice == len(entregas):
        return 0
    return entregas[indice].puntaje + sumatoria_puntajes(entregas, indice + 1)


def sumatoria_puntajes_iterativa(entregas: Sequence[Entrega]) -> int:
    """Suma los puntajes con un ciclo ``for`` (versión de comparación)."""
    total = 0
    for entrega in entregas:
        total += entrega.puntaje
    return total


# --------------------------------------------------------------- 2. búsqueda
def buscar_codigo(entregas: Sequence[Entrega], codigo: str, indice: int = 0) -> int:
    """Busca un código y devuelve su índice, o -1 si no se encuentra.

    Caso base:      ``indice == len(entregas)`` -> -1 (recorrido agotado);
                    también se detiene al encontrar ``codigo``.
    Caso recursivo: avanza con ``indice + 1`` si el elemento actual no coincide.
    """
    _validar_texto(codigo, "codigo")
    _validar_entero_no_negativo(indice, "indice")
    if indice == len(entregas):
        return -1
    if entregas[indice].codigo == codigo:
        return indice
    return buscar_codigo(entregas, codigo, indice + 1)


def buscar_codigo_iterativo(entregas: Sequence[Entrega], codigo: str) -> int:
    """Búsqueda lineal con ``for`` (versión de comparación)."""
    _validar_texto(codigo, "codigo")
    for indice, entrega in enumerate(entregas):
        if entrega.codigo == codigo:
            return indice
    return -1


# ---------------------------------------------------------- 3. conteo de texto
def contar_palabra_clave(
    entregas: Sequence[Entrega], clave: str, indice: int = 0
) -> int:
    """Cuenta cuántos nombres de archivo contienen ``clave`` (sin distinción
    de mayúsculas).

    Caso base:      ``indice == len(entregas)`` -> 0.
    Caso recursivo: ``(1 si coincide el archivo actual else 0)
                      + contar_palabra_clave(..., indice + 1)``.
    """
    _validar_texto(clave, "clave")
    _validar_entero_no_negativo(indice, "indice")
    if indice == len(entregas):
        return 0
    coincide = 1 if clave.lower() in entregas[indice].archivo.lower() else 0
    return coincide + contar_palabra_clave(entregas, clave, indice + 1)


def contar_palabra_clave_iterativo(entregas: Sequence[Entrega], clave: str) -> int:
    """Conteo con ``for`` (versión de comparación)."""
    _validar_texto(clave, "clave")
    return sum(1 for entrega in entregas if clave.lower() in entrega.archivo.lower())


# ------------------------------------------------- 4. funciones simples extras
def factorial(n: int) -> int:
    """Factorial de ``n`` de forma recursiva.

    Caso base:      ``n <= 1`` -> 1 (además evita llamadas infinitas con negativos).
    Caso recursivo: ``n * factorial(n - 1)``.
    """
    _validar_entero_no_negativo(n, "n")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def potencia(base: int | float, exponente: int) -> int | float:
    """``base`` elevada a ``exponente`` de forma recursiva.

    Caso base:      ``exponente == 0`` -> 1 (incluye ``0 ** 0`` por convención).
    Caso recursivo: ``base * potencia(base, exponente - 1)``.
    """
    if isinstance(base, bool) or not isinstance(base, (int, float)):
        raise TypeError("base debe ser un número.")
    _validar_entero_no_negativo(exponente, "exponente")
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
