"""Modulo de control del tanque de proceso (Tarea 2)."""


def calcular_promedio(lista_lecturas):
    """Retorna el promedio de una lista de lecturas."""
    total = 0
    for i in range(len(lista_lecturas)):
        total = total + lista_lecturas[i]
    return total / len(lista_lecturas)


def control_nivel(nivel_actual, set_point=70):
    """Decide si se debe llenar o vaciar el tanque."""
    if nivel_actual > set_point:
        return "VACIAR"
    return "LLENAR"


def alarma(temp_actual):
    """Retorna el estado de alarma segun la temperatura."""
    if temp_actual > 90:
        return "ALARMA: revisar enfriamiento"
    return "OK"