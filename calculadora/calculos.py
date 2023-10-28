def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a,b):
    return a * b


def division(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)


def cuadrado(a):
    return a ** 2