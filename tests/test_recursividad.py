"""Pruebas unitarias de las funciones recursivas e iterativas.

Cada prueba documenta el valor esperado; el valor obtenido se compara con
``assertEqual`` o se muestra en el informe mediante la salida de ``unittest``.
"""

import unittest

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


class TestSumatoria(unittest.TestCase):
    def test_sumatoria_recursiva(self):
        """Esperado: 668 = 85+92+78+88+95+70+100+60."""
        self.assertEqual(sumatoria_puntajes(ENTREGAS), 668)

    def test_sumatoria_iterativa_coincide(self):
        recursivo = sumatoria_puntajes(ENTREGAS)
        iterativo = sumatoria_puntajes_iterativa(ENTREGAS)
        self.assertEqual(recursivo, iterativo)

    def test_sumatoria_lista_vacia(self):
        """Caso base con colección vacía: esperado 0."""
        self.assertEqual(sumatoria_puntajes(()), 0)
        self.assertEqual(sumatoria_puntajes_iterativa(()), 0)


class TestBusqueda(unittest.TestCase):
    def test_buscar_codigo_existente(self):
        """Esperado: 'C003' está en el índice 4."""
        self.assertEqual(buscar_codigo(ENTREGAS, "C003"), 4)

    def test_buscar_codigo_inexistente(self):
        """Esperado: -1 cuando el código no aparece."""
        self.assertEqual(buscar_codigo(ENTREGAS, "Z999"), -1)

    def test_busqueda_iterativa_coincide_con_recursiva(self):
        for codigo, esperado in (("A001", 0), ("D010", 6), ("Z999", -1)):
            with self.subTest(codigo=codigo):
                self.assertEqual(buscar_codigo(ENTREGAS, codigo), esperado)
                self.assertEqual(
                    buscar_codigo_iterativo(ENTREGAS, codigo),
                    buscar_codigo(ENTREGAS, codigo),
                )


class TestConteo(unittest.TestCase):
    def test_contar_palabra_final(self):
        """Esperado: 3 archivos contienen 'final'."""
        self.assertEqual(contar_palabra_clave(ENTREGAS, "final"), 3)

    def test_contar_palabra_v2(self):
        """Esperado: 3 archivos contienen 'v2'."""
        self.assertEqual(contar_palabra_clave(ENTREGAS, "v2"), 3)

    def test_conteo_respeta_mayusculas_y_coincide_con_iterativo(self):
        self.assertEqual(contar_palabra_clave(ENTREGAS, "FINAL"), 3)
        self.assertEqual(
            contar_palabra_clave(ENTREGAS, "final"),
            contar_palabra_clave_iterativo(ENTREGAS, "final"),
        )

    def test_contar_clave_ausente(self):
        """Esperado: 0 si ningún archivo contiene la clave."""
        self.assertEqual(contar_palabra_clave(ENTREGAS, "borrador"), 0)


class TestFuncionesSimples(unittest.TestCase):
    def test_factorial(self):
        for n, esperado in ((0, 1), (1, 1), (5, 120), (10, 3628800)):
            with self.subTest(n=n):
                self.assertEqual(factorial(n), esperado)

    def test_potencia(self):
        for base, exponente, esperado in (
            (2, 0, 1),
            (2, 10, 1024),
            (5, 3, 125),
            (-2, 3, -8),
        ):
            with self.subTest(base=base, exponente=exponente):
                self.assertEqual(potencia(base, exponente), esperado)


class TestValidaciones(unittest.TestCase):
    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_potencia_exponente_negativo(self):
        with self.assertRaises(ValueError):
            potencia(2, -1)

    def test_busqueda_vacia(self):
        with self.assertRaises(ValueError):
            buscar_codigo(ENTREGAS, "")

    def test_clave_vacia(self):
        with self.assertRaises(ValueError):
            contar_palabra_clave(ENTREGAS, "   ")

    def test_indice_negativo(self):
        with self.assertRaises(ValueError):
            sumatoria_puntajes(ENTREGAS, -1)

    def test_tipo_incorrecto(self):
        with self.assertRaises(TypeError):
            factorial("5")


if __name__ == "__main__":
    unittest.main()
