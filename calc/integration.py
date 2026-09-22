"""Модуль численного интегрирования методом левых прямоугольников."""

import math

MAX_STEPS = 100000
DIGITS = 4


class IntegrationError(ValueError):
    """Ошибка в исходных данных команды integrate."""
    pass


def f_ratio(x):
    """F(x) = x / (x + 1)."""
    return x / (x + 1)


def f_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)


# Таблица функций: имя → (функция, формула, low, high, границы_включены)
FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root":  (f_root,  "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


def integrate(f, a, b, steps):
    """Интеграл методом левых прямоугольников."""
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        result += f(a + i * dx) * dx
    return result


def check_params(a, b, steps, low, high, boundaries_included):
    """Проверяет пределы и число шагов."""
    if not math.isfinite(a) or not math.isfinite(b):
        raise IntegrationError("пределы должны быть конечными числами")
    if a >= b:
        raise IntegrationError("начальный предел не меньше конечного")
    if not (1 <= steps <= MAX_STEPS):
        raise IntegrationError("количество шагов вне диапазона")

    if boundaries_included:
        ok = (low <= a <= high) and (low <= b <= high)
    else:
        ok = (low < a < high) and (low < b < high)
    if not ok:
        raise IntegrationError("предел вне промежутка функции")