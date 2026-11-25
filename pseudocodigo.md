# Pseudocódigo de la solución — Tema 7

Notación: `E` = lista de entregas, `n = longitud(E)`, `i` = índice actual.
En todas las funciones recursivas la reducción es `i → i + 1`, por lo que se
garantiza alcanzar el caso base `i = n`.

## 1. Sumatoria recursiva de puntajes

```
FUNCIÓN sumatoria_puntajes(E, i = 0):
    SI i < 0 → ERROR "índice negativo"
    SI i = longitud(E) ENTONCES
        RETORNAR 0                         // caso base
    SINO
        RETORNAR E[i].puntaje + sumatoria_puntajes(E, i + 1)   // caso recursivo
    FIN SI
FIN FUNCIÓN
```

Equivalente iterativo: `total ← 0; PARA CADA e EN E: total ← total + e.puntaje;
RETORNAR total`.

## 2. Búsqueda recursiva de código

```
FUNCIÓN buscar_codigo(E, código, i = 0):
    SI código está vacío → ERROR "búsqueda vacía"
    SI i < 0 → ERROR "índice negativo"
    SI i = longitud(E) ENTONCES
        RETORNAR -1                        // caso base: no encontrado
    SI E[i].codigo = código ENTONCES
        RETORNAR i                         // caso base: encontrado
    RETORNAR buscar_codigo(E, código, i + 1)                    // caso recursivo
FIN FUNCIÓN
```

## 3. Conteo recursivo de palabra clave en nombres de archivo

```
FUNCIÓN contar_palabra_clave(E, clave, i = 0):
    SI clave está vacía → ERROR "clave vacía"
    SI i = longitud(E) ENTONCES
        RETORNAR 0                         // caso base
    coincide ← 1 SI clave (en minúsculas) está en E[i].archivo (en minúsculas),
               0 EN OTRO CASO
    RETORNAR coincides + contar_palabra_clave(E, clave, i + 1)  // caso recursivo
FIN FUNCIÓN
```

## 4. Funciones simples adicionales

```
FUNCIÓN factorial(n):
    SI n < 0 → ERROR "n negativo"
    SI n <= 1 → RETORNAR 1                 // caso base
    RETORNAR n * factorial(n - 1)          // caso recursivo
FIN FUNCIÓN

FUNCIÓN potencia(base, exponente):
    SI exponente < 0 → ERROR "exponente negativo"
    SI exponente = 0 → RETORNAR 1          // caso base
    RETORNAR base * potencia(base, exponente - 1)               // caso recursivo
FIN FUNCIÓN
```

## 5. Programa principal (consola)

```
INICIO
    cargar 8 entregas simuladas
    MOSTRAR menú
    REPETIR
        LEER opción
        SEGÚN opción:
            1 → mostrar entregas
            2 → sumatoria recursiva e iterativa
            3 → buscar código (recursiva e iterativa)
            4 → contar palabra clave (recursiva e iterativa)
            5 → factorial y potencia
            6 → probar entradas inválidas
            0 → SALIR
    FIN REPETIR
FIN
```

## Criterios de parada y reducción

| Función | Caso base | Reducción | Riesgo evitado |
| --- | --- | --- | --- |
| `sumatoria_puntajes` | `i = n` → 0 | `i + 1` | índice negativo validado |
| `buscar_codigo` | `i = n` → -1 o coincidencia → `i` | `i + 1` | cadena vacía validada |
| `contar_palabra_clave` | `i = n` → 0 | `i + 1` | clave vacía validada |
| `factorial` | `n <= 1` → 1 | `n - 1` | `n` negativo validado |
| `potencia` | `exponente = 0` → 1 | `exponente - 1` | exponente negativo validado |
