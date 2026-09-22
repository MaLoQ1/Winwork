"""Модуль суммирования знакочередующихся рядов."""

import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000
DIGITS = math.ceil(-math.log10(MAX_EPS))


class SeriesError(ValueError):
    """Ошибка в исходных данных команды series."""
    pass


def sign(n):
    """Знак слагаемого: +1 для нечётного n, -1 для чётного."""
    return 1 if n % 2 == 1 else -1


def term_sqplus(n):
    """Слагаемое ряда sqplus: (-1)^(n+1) / (n^2 + 1)."""
    return sign(n) / (n * n + 1)


def term_third(n):
    """Слагаемое ряда third: (-1)^(n+1) / (3n)."""
    return sign(n) / (3 * n)


# Таблица рядов: имя → (функция слагаемого, формула)
FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}


def sum_by_count(term, count):
    """Сумма первых count слагаемых."""
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result


def sum_by_eps(term, eps):
    """Сумма с остановкой по точности. Возвращает (сумма, число слагаемых)."""
    result = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise SeriesError("точность не достигнута")


def check_params(terms, eps):
    """Проверяет параметры --terms / --eps."""
    if (terms is None) == (eps is None):
        raise SeriesError("укажите ровно один из --terms или --eps")
    if terms is not None and not (1 <= terms <= MAX_TERMS):
        raise SeriesError("количество слагаемых вне диапазона")
    if eps is not None:
        if not math.isfinite(eps) or not (0 < eps <= MAX_EPS):
            raise SeriesError("точность вне диапазона")