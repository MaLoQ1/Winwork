"""Точка входа приложения mathtool."""

import sys

from cli import build_parser
from calc import equation
from calc import stats
from calc import series
from calc import integration


def handle_solve(args):
    """Обработчик команды solve."""
    # Коэффициенты: либо все три параметра, либо все три с клавиатуры
    if args.a is None and args.b is None and args.c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом",
                  file=sys.stderr)
            return 1
    elif args.a is not None and args.b is not None and args.c is not None:
        a, b, c = args.a, args.b, args.c
    else:
        print("ОШИБКА: укажите все три коэффициента либо ни одного",
              file=sys.stderr)
        return 1

    # Расчёт
    try:
        result = equation.solve(a, b, c)
    except equation.EquationError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

    # Вывод
    if result['kind'] == 'линейное':
        print("Уравнение линейное")
        print(f"x = {result['roots'][0]:.3f}")
    else:
        print("Уравнение квадратное")
        print(f"Дискриминант: {result['discriminant']}")
        roots = result['roots']
        if len(roots) == 2:
            print(f"x1 = {roots[0]:.3f}")
            print(f"x2 = {roots[1]:.3f}")
        elif len(roots) == 1:
            print(f"x = {roots[0]:.3f}")
        else:
            print("Действительных корней нет")
    return 0

def read_numbers(input_file):
    """Читает числа из файла или stdin. Возбуждает ValueError/OSError."""
    if input_file is not None:
        source = open(input_file, encoding="utf-8-sig")
    else:
        source = sys.stdin

    try:
        values = []
        for line in source:
            for word in line.split():
                try:
                    values.append(float(word))
                except ValueError:
                    raise ValueError(f"{word} не является числом")
        return values
    finally:
        if input_file is not None:
            source.close()


def handle_stats(args):
    """Обработчик команды stats."""
    try:
        values = read_numbers(args.input)
    except OSError:
        print("ОШИБКА: файл не открывается", file=sys.stderr)
        return 1
    except ValueError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

    try:
        stats.check_numbers(values)
    except stats.StatsError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return 0

def handle_series(args):
    """Обработчик команды series."""
    try:
        series.check_params(args.terms, args.eps)
    except series.SeriesError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

    if args.func not in series.FORMULAS:
        print(f"ОШИБКА: неизвестный ряд '{args.func}'", file=sys.stderr)
        return 1
    term, formula = series.FORMULAS[args.func]

    print(formula)

    try:
        if args.terms is not None:
            result = series.sum_by_count(term, args.terms)
            count = args.terms
        else:
            result, count = series.sum_by_eps(term, args.eps)
    except series.SeriesError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")
    return 0

def handle_integrate(args):
    """Обработчик команды integrate."""
    if args.func not in integration.FUNCTIONS:
        print(f"ОШИБКА: неизвестная функция '{args.func}'", file=sys.stderr)
        return 1
    f, formula, low, high, incl = integration.FUNCTIONS[args.func]

    # Проверка ДО вывода формулы
    try:
        integration.check_params(args.start, args.end, args.steps,
                                 low, high, incl)
    except integration.IntegrationError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1

    print(formula)
    result = integration.integrate(f, args.start, args.end, args.steps)
    print(f"Значение интеграла: {result:.{integration.DIGITS}f}")
    return 0

def main(argv):
    """Точка входа: разбор параметров, вызов обработчика."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handlers = {
        'solve': handle_solve,
        'stats': handle_stats,
        'series': handle_series,
        'integrate': handle_integrate,
    }

    handler = handlers.get(args.command)
    if handler is None:
        print(f"ОШИБКА: команда '{args.command}' ещё не реализована",
              file=sys.stderr)
        return 1

    try:
        return handler(args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))