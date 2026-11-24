"""Medicion de tiempos de CPU: version base vs optimizada (Tarea 4)."""
import random
import statistics
import time

TOTAL_LECTURAS = 1_000_000
EJECUCIONES = 5


def procesar_base(lecturas):
    """Version base: bucles con indices y doble recorrido."""
    total = 0
    for i in range(len(lecturas)):
        total = total + lecturas[i]
    promedio = total / len(lecturas)
    alarmas = []
    for i in range(len(lecturas)):
        if lecturas[i] > 90:
            alarmas.append(lecturas[i])
    return promedio, len(alarmas)


def procesar_optimizado(lecturas):
    """Version optimizada: sum() y comprension de listas."""
    promedio = sum(lecturas) / len(lecturas)
    alarmas = [valor for valor in lecturas if valor > 90]
    return promedio, len(alarmas)


def medir(funcion, lecturas):
    """Retorna la mediana de tiempo de pared y de CPU."""
    pared = []
    cpu = []
    for _ in range(EJECUCIONES):
        inicio_pared = time.perf_counter()
        inicio_cpu = time.process_time()
        funcion(lecturas)
        pared.append(time.perf_counter() - inicio_pared)
        cpu.append(time.process_time() - inicio_cpu)
    return statistics.median(pared), statistics.median(cpu)


def main():
    random.seed(7)
    lecturas = [random.uniform(60, 95) for _ in range(TOTAL_LECTURAS)]
    assert procesar_base(lecturas)[1] == procesar_optimizado(lecturas)[1]
    base = medir(procesar_base, lecturas)
    optimizado = medir(procesar_optimizado, lecturas)
    print("Base       perf_counter: %.4f s | process_time: %.4f s" % base)
    print("Optimizada perf_counter: %.4f s | process_time: %.4f s"
          % optimizado)
    mejora = (1 - optimizado[0] / base[0]) * 100
    print("Mejora: %.1f %% | Aceleracion: %.2fx"
          % (mejora, base[0] / optimizado[0]))


if __name__ == "__main__":
    
    main()
