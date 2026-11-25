# Verificación de sugerencias de IA (Paso 6 de la guía)

La IA fue utilizada **solo como revisora**, sin reemplazar el código ni el
razonamiento. Se le solicitó: *"Revisa si cada función recursiva tiene caso base
correcto, si reduce el problema en cada llamada y si puede entrar en recursión
infinita. No reemplaces el código."*

| Función | Revisión recibida | Validación manual realizada | Resultado |
| --- | --- | --- | --- |
| `sumatoria_puntajes` | Confirmar `i = len(entregas)` como caso base; vigilar índice negativo. | Prueba `test_sumatoria_recursiva` (668) y `test_indice_negativo`. | Sugerencia aceptada; la validación ya existía. |
| `buscar_codigo` | Sugerir devolver `-1` al agotar la lista y validar cadena vacía. | Pruebas con `C003` → 4, `Z999` → -1 y `test_busqueda_vacia`. | Sugerencia aceptada y cubierta por pruebas. |
| `contar_palabra_clave` | Normalizar mayúsculas y validar clave vacía. | Pruebas `final`, `FINAL`, `v2` y `test_clave_vacia`. | Sugerencia aceptada. |
| `factorial` | El caso base `n <= 1` evita recursión infinita; rechazar negativos. | `factorial(0)=1`, `factorial(5)=120`, `factorial(-3)` lanza error. | Sugerencia aceptada. |
| `potencia` | El caso base debe ser `exponente = 0`; revisar exponentes negativos. | `potencia(2,0)=1`, `potencia(2,10)=1024`, `potencia(2,-1)` lanza error. | Sugerencia aceptada. |

**Conclusión de la revisión:** no se detectó recursión infinita en las funciones
implementadas. Todas las sugerencias se comprobaron ejecutando el programa
(`salida_ejecucion.txt`) y la suite de 18 pruebas (`salida_pruebas.txt`).
