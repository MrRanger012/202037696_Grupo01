"""Programa principal: integra control y diccionarios de datos."""
from control.control_nivel import alarma, control_nivel
from diccionarios.datos_sensores import DATOS_SENSORES, UNIDADES_SENSORES


def main():
    nivel = DATOS_SENSORES["nivel_tanque"]
    temperatura = DATOS_SENSORES["temp_tanque"]
    print("Nivel:", nivel, UNIDADES_SENSORES["nivel_tanque"],
          "->", control_nivel(nivel))
    print("Temperatura:", temperatura, UNIDADES_SENSORES["temp_tanque"],
          "->", alarma(temperatura))


if __name__ == "__main__":
    main()
