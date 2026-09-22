"""Модуль решения уравнения A*x^2 + B*x + C = 0."""

import math

MAX_VALUE = 10000


class EquationError(ValueError):
    """Ошибка в исходных данных уравнения."""
    pass


def check_value(name, value):
    """Проверяет значение коэффициента на допустимость."""
    if abs(value) > MAX_VALUE:
        raise EquationError(f"коэффициент {name} вне допустимого диапазона")


def check_coefficients(coefficients):
    """Проверяет все коэффициенты из словаря."""
    for name, value in coefficients.items():
        check_value(name, value)


def solve_linear(b, c):
    """Решает линейное уравнение B*x + C = 0."""
    if b == 0:
        raise EquationError("это не уравнение, неизвестное отсутствует")
    return -c / b


def solve_quadratic(a, b, c):
    """Решает квадратное уравнение, возвращает словарь с D и корнями."""
    d = b * b - 4 * a * c
    if d > 0:
        sqrt_d = math.sqrt(d)
        roots = [(-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)]
    elif d == 0:
        roots = [-b / (2 * a)]
    else:
        roots = []
    return {'kind': 'квадратное', 'discriminant': d, 'roots': roots}


def solve(a, b, c):
    """Решает уравнение. Возбуждает EquationError при ошибке в данных."""
    check_coefficients({'A': a, 'B': b, 'C': c})
    if a == 0:
        x = solve_linear(b, c)
        return {'kind': 'линейное', 'roots': [x]}
    return solve_quadratic(a, b, c)