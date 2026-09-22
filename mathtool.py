"""Точка входа приложения mathtool."""

import sys

from cli import build_parser
from calc import equation


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


def main(argv):
    """Точка входа: разбор параметров, вызов обработчика."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    handlers = {
        'solve': handle_solve,
        # stats, series, integrate добавим позже
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