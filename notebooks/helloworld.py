def mi_funcion():
    x = 10
    y = 5

    resultado = x + y
    print("El resultado es:", resultado)


def calculadora(a, b, operacion):
    """
    Función simple para demostrar tests parametrizados.
    """
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    else:
        raise ValueError(f"Operacion desconocida: {operacion}")


if __name__ == "__main__":
    mi_funcion()
