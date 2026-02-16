import pytest

from notebooks.helloworld import calculadora


# 1. Test unitario básico
def test_suma_simple():
    assert calculadora(2, 3, "suma") == 5


# 2. Test parametrizado (lo que pediste: variar parámetros)
@pytest.mark.parametrize(
    "a, b, operacion, esperado",
    [
        (10, 5, "suma", 15),
        (10, 5, "resta", 5),
        (3, 4, "multiplicacion", 12),
        (20, 2, "division", 10),
        (-1, 1, "suma", 0),
        (
            0.1,
            0.2,
            "suma",
            0.30000000000000004,
        ),  # Flotantes suelen necesitar un assert específico
    ],
)
def test_calculadora_varios_casos(a, b, operacion, esperado):
    assert calculadora(a, b, operacion) == esperado


# 3. Test para verificar excepciones (errores esperados)
def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        calculadora(10, 0, "division")


def test_operacion_invalida():
    with pytest.raises(ValueError, match="Operacion desconocida"):
        calculadora(10, 5, "potencia")
