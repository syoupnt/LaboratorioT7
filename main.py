"""Programa de consola: análisis de entregas digitales con recursividad.

Uso:
    python main.py            menú interactivo
    python main.py --demo     recorrido completo sin entradas interactivas
"""

import argparse
import sys

from datos import ENTREGAS
from recursividad import (
    buscar_codigo,
    buscar_codigo_iterativo,
    contar_palabra_clave,
    contar_palabra_clave_iterativo,
    factorial,
    potencia,
    sumatoria_puntajes,
    sumatoria_puntajes_iterativa,
)


def titulo(texto: str) -> None:
    print(f"\n{'=' * 64}\n{texto}\n{'=' * 64}")


def mostrar_entregas() -> None:
    titulo("ENTREGAS REGISTRADAS (8 simuladas)")
    print(f"{'Índice':<7}{'Código':<9}{'Archivo':<22}{'Intentos':<9}{'Puntaje':<8}Observaciones")
    print("-" * 88)
    for indice, entrega in enumerate(ENTREGAS):
        print(
            f"{indice:<7}{entrega.codigo:<9}{entrega.archivo:<22}"
            f"{entrega.intentos:<9}{entrega.puntaje:<8}{entrega.observaciones}"
        )


def comparar_sumatoria() -> None:
    titulo("1) SUMATORIA DE PUNTAJES: RECURSIVA vs ITERATIVA")
    recursivo = sumatoria_puntajes(ENTREGAS)
    iterativo = sumatoria_puntajes_iterativa(ENTREGAS)
    print(f"Recursiva : sumatoria_puntajes(entregas)          = {recursivo}")
    print(f"Iterativa : sumatoria_puntajes_iterativa(entregas) = {iterativo}")
    print(f"¿Coinciden? {'SÍ' if recursivo == iterativo else 'NO'}")


def comparar_busqueda(codigo: str) -> None:
    titulo(f"2) BÚSQUEDA DE CÓDIGO: '{codigo}'")
    recursivo = buscar_codigo(ENTREGAS, codigo)
    iterativo = buscar_codigo_iterativo(ENTREGAS, codigo)
    mensaje = "no encontrado (-1)" if recursivo == -1 else f"índice {recursivo}"
    print(f"Recursiva : {mensaje}")
    print(f"Iterativa : {'no encontrado (-1)' if iterativo == -1 else f'índice {iterativo}'}")
    print(f"¿Coinciden? {'SÍ' if recursivo == iterativo else 'NO'}")


def comparar_conteo(clave: str) -> None:
    titulo(f"3) CONTEO DE ARCHIVOS CON LA PALABRA '{clave}'")
    recursivo = contar_palabra_clave(ENTREGAS, clave)
    iterativo = contar_palabra_clave_iterativo(ENTREGAS, clave)
    print(f"Recursiva : {recursivo} archivo(s)")
    print(f"Iterativa : {iterativo} archivo(s)")
    print(f"¿Coinciden? {'SÍ' if recursivo == iterativo else 'NO'}")


def mostrar_funciones_simples() -> None:
    titulo("4) FUNCIONES RECURSIVAS SIMPLES ADICIONALES")
    print(f"factorial(0)  = {factorial(0)}   <- caso base")
    print(f"factorial(5)  = {factorial(5)}")
    print(f"potencia(2,0) = {potencia(2, 0)}   <- caso base")
    print(f"potencia(2,10)= {potencia(2, 10)}")


def mostrar_validaciones() -> None:
    titulo("5) VALIDACIÓN DE ENTRADAS INVÁLIDAS")
    casos = (
        ("factorial(-3)", lambda: factorial(-3)),
        ("potencia(2, -1)", lambda: potencia(2, -1)),
        ("buscar_codigo(entregas, '')", lambda: buscar_codigo(ENTREGAS, "")),
        ("contar_palabra_clave(entregas, '   ')", lambda: contar_palabra_clave(ENTREGAS, "   ")),
        ("sumatoria_puntajes(entregas, -1)", lambda: sumatoria_puntajes(ENTREGAS, -1)),
    )
    for descripcion, operacion in casos:
        try:
            operacion()
            print(f"{descripcion:<46} -> ERROR: no se detectó la entrada inválida")
        except (ValueError, TypeError) as error:
            print(f"{descripcion:<46} -> {type(error).__name__}: {error}")


def demo() -> None:
    """Recorrido completo y determinista, útil como evidencia de ejecución."""
    print("SISTEMA DE ANÁLISIS DE ENTREGAS DIGITALES - TEMA 7 (modo demostración)")
    mostrar_entregas()
    comparar_sumatoria()
    comparar_busqueda("C003")
    comparar_busqueda("Z999")
    comparar_conteo("final")
    comparar_conteo("v2")
    mostrar_funciones_simples()
    mostrar_validaciones()
    print("\nFin de la demostración.")


def leer_cadena(mensaje: str) -> str:
    return input(mensaje).strip()


def menu() -> None:
    opciones = {
        "1": mostrar_entregas,
        "2": comparar_sumatoria,
        "3": lambda: comparar_busqueda(leer_cadena("Código a buscar: ")),
        "4": lambda: comparar_conteo(leer_cadena("Palabra clave a contar: ")),
        "5": mostrar_funciones_simples,
        "6": mostrar_validaciones,
    }
    while True:
        titulo("MENÚ PRINCIPAL")
        print("1. Ver entregas registradas")
        print("2. Comparar sumatoria recursiva e iterativa")
        print("3. Buscar código de estudiante")
        print("4. Contar archivos con una palabra clave")
        print("5. Funciones recursivas simples (factorial y potencia)")
        print("6. Probar validaciones de entradas inválidas")
        print("0. Salir")
        opcion = leer_cadena("\nSeleccione una opción: ")
        if opcion == "0":
            print("Hasta luego.")
            break
        accion = opciones.get(opcion)
        if accion is None:
            print("Opción no válida. Intente de nuevo.")
            continue
        try:
            accion()
        except (ValueError, TypeError) as error:
            print(f"Entrada inválida: {error}")


def main() -> int:
    # La consola de Windows usa una codificación regional por defecto; forzar
    # UTF-8 evita que los acentos se muestren como caracteres extraños.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--demo",
        action="store_true",
        help="ejecuta todas las operaciones sin solicitar datos por teclado",
    )
    args = parser.parse_args()
    if args.demo:
        demo()
    else:
        menu()
    return 0


if __name__ == "__main__":
    sys.exit(main())
