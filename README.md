# Laboratorio Tema 7 — Recursividad

**Curso:** Fundamentos de Programación · **Tema N° 7:** Recursividad
**Experiencia:** *Resolver dividiendo: recursividad, pruebas y comparación con iteración*

Programa de consola en Python que aplica recursividad de forma controlada a un caso
práctico: el análisis de entregas digitales de un curso universitario.

## Contenido del repositorio

| Archivo | Descripción |
| --- | --- |
| `datos.py` | Modelo `Entrega` y 8 entregas simuladas. |
| `recursividad.py` | Funciones recursivas e iterativas, con caso base, caso recursivo y validaciones. |
| `main.py` | Programa de consola (menú interactivo y modo `--demo`). |
| `tests/test_recursividad.py` | 18 pruebas unitarias con resultado esperado y obtenido. |
| `pseudocodigo.md` | Pseudocódigo de las cuatro operaciones principales. |
| `evidencia/salida_ejecucion.txt` | Salida real del modo demostración (entradas válidas e inválidas). |
| `evidencia/salida_pruebas.txt` | Salida real de la suite de pruebas. |
| `evidencia/verificacion_ia.md` | Registro de la revisión de IA y su validación manual. |

## Ejecución

Requiere Python 3.10 o superior (probado con Python 3.14).

```bash
python main.py            # menú interactivo
python main.py --demo     # recorrido completo sin entradas interactivas
python -m unittest discover -s tests -v
```

## Decisiones de diseño

- Cada función recursiva reduce el problema mediante un índice (`indice + 1`), de modo
  que la condición de parada siempre se alcanza: `indice == len(entregas)`.
- Las búsquedas devuelven el índice de la primera coincidencia o `-1` si no existe.
- Se validan entradas negativas, índices negativos y cadenas vacías antes de recurrir.
- Se incluye una versión iterativa de la sumatoria, la búsqueda y el conteo para
  comparar claridad, riesgo de error y facilidad de prueba.
- La IA se usó únicamente como revisora de casos base y sugerencia de pruebas; cada
  sugerencia se validó ejecutando el código y las pruebas (ver la declaración final
  del informe).
