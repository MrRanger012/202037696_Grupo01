# 202037696_Grupo01

Proyecto de la Tarea 5 - Lenguajes Interpretados (UNAD, código 202037696).

## Descripción

Sistema en Python para el monitoreo y control de un tanque de proceso en una
planta industrial: lee variables de los sensores (nivel, temperatura y
presión de línea), decide si se debe llenar o vaciar el tanque, activa una
alarma por temperatura y mide la eficiencia de CPU del procesamiento de datos.

## Estructura

| Carpeta / archivo | Contenido |
|---|---|
| `control/` | Scripts de control del tanque (Tarea 2) |
| `diccionarios/` | Diccionarios de datos de los sensores (Tarea 3) |
| `optimización/` | Medición y optimización de CPU (Tarea 4) |
| `main.py` | Programa principal que integra los módulos |

## Ejecución

Requiere Python 3.10 o superior.

```
python main.py
python optimización/benchmark_cpu.py
```

Salida esperada de `main.py`:

```
Nivel: 72.5 % -> VACIAR
Temperatura: 85.2 grados C -> OK
```

## Resultados de CPU

Mediana de 5 ejecuciones sobre 1 000 000 de lecturas simuladas.

| Métrica | Base | Optimizada | Mejora |
|---|---|---|---|
| perf_counter | 0,1035 s | 0,0582 s | 43,7 % |
| process_time (CPU) | 0,1094 s | 0,0625 s | 42,9 % |

## Estándar de estilo

Código normalizado bajo PEP 8: 4 espacios de indentación, nombres en
`snake_case` y líneas de máximo 79 caracteres. Verificado con `pycodestyle`.

## Autor

Vairon Hurtado Pino - Ingeniería de Telecomunicaciones, UNAD.
