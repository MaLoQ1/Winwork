"""Модуль показателей числовой последовательности."""

import math

MAX_COUNT = 20
MAX_ABS_VALUE = 10000


class StatsError(ValueError):
    """Ошибка в исходных данных команды stats."""
    pass


def check_numbers(values):
    """Проверяет список чисел на соответствие ограничениям."""
    if not values:
        raise StatsError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise StatsError("слишком много чисел (не более 20)")
    for value in values:
        if not math.isfinite(value):
            raise StatsError(f"значение {value} не является конечным числом")
        if abs(value) > MAX_ABS_VALUE:
            raise StatsError(f"значение {value} выходит за диапазон")


def total(values):
    """Сумма чисел."""
    result = 0
    for value in values:
        result += value
    return result


def mean(values):
    """Среднее арифметическое."""
    return total(values) / len(values)


def sum_squares(values):
    """Сумма квадратов."""
    result = 0
    for value in values:
        result += value ** 2
    return result


def rms(values):
    """Среднее квадратическое."""
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    """Сумма квадратов отклонений от среднего (в два прохода)."""
    avg = mean(values)
    result = 0
    for value in values:
        result += (value - avg) ** 2
    return result


def variance(values):
    """Дисперсия (по N)."""
    return sum_squared_deviations(values) / len(values)


def std_deviation(values):
    """СКО — корень из дисперсии."""
    return math.sqrt(variance(values))


def sample_std_deviation(values):
    """Стандартное отклонение (по N-1). None при N < 2."""
    if len(values) < 2:
        return None
    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    """Наименьшее значение."""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    """Наибольшее значение."""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def count_positive(values):
    """Количество положительных."""
    return sum(1 for v in values if v > 0)


def count_negative(values):
    """Количество отрицательных."""
    return sum(1 for v in values if v < 0)


# Таблица показателей: (подпись, функция, формат)
REPORT = [
    ("Количество",    len,                    "d"),
    ("Сумма",         total,                  ".3f"),
    ("Ср. арифм.",    mean,                   ".3f"),
    ("Сумма кв.",     sum_squares,            ".3f"),
    ("Ср. кв.",       rms,                    ".3f"),
    ("Дисперсия",     variance,               ".3f"),
    ("СКО",           std_deviation,          ".3f"),
    ("Станд. откл.",  sample_std_deviation,   ".3f"),
    ("Наименьшее",    minimum,                ".3f"),
    ("Наибольшее",    maximum,                ".3f"),
    ("Положительных", count_positive,         "d"),
    ("Отрицательных", count_negative,         "d"),
]