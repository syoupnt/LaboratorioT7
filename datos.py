"""Datos simulados del caso práctico.

Cada entrega registra: código de estudiante, nombre de archivo, número de
intentos de envío, puntaje obtenido y observaciones breves.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Entrega:
    """Registro inmutable de una entrega digital."""

    codigo: str
    archivo: str
    intentos: int
    puntaje: int
    observaciones: str


ENTREGAS: tuple[Entrega, ...] = (
    Entrega("A001", "tarea1_final.py", 2, 85, "Entrega en plazo"),
    Entrega("A002", "tarea1_v2.py", 3, 92, "Corrección tras observación"),
    Entrega("B014", "practica_final.pdf", 1, 78, "Sin observaciones"),
    Entrega("B021", "ensayo_v2.docx", 4, 88, "Error de formato corregido"),
    Entrega("C003", "laboratorio7.py", 2, 95, "Casos límite cubiertos"),
    Entrega("C007", "informe_final.docx", 1, 70, "Faltan conclusiones"),
    Entrega("D010", "script_v2.py", 2, 100, "Solución completa"),
    Entrega("D015", "notas.txt", 3, 60, "Observaciones breves"),
)
