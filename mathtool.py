# mathtool.py
import sys
import math

MAX_VALUE = 10000

def print_help():
    """Выводит справочную информацию о программе."""
    help_text = """mathtool --- решение уравнений вида A*x^2 + B*x + C = 0

Использование:
  python mathtool.py                 вывод справки
  python mathtool.py --help          вывод справки
  python mathtool.py solve           ввод коэффициентов с клавиатуры
  python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C --- целые числа, по модулю не превышающие 10000."""
    print(help_text)

def solve_equation(a, b, c):
    """Решает уравнение A*x^2 + B*x + C = 0 и выводит результат."""
    if a == 0:
        if b != 0:
            print("Уравнение линейное")
            x = -c / b
            print(f"x = {x:.3f}")
        else:
            print("ОШИБКА: это не уравнение, неизвестное отсутствует.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Уравнение квадратное")
        d = b*b - 4*a*c
        print(f"D = {d}")

        if d > 0:
            sqrt_d = math.sqrt(d)
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")
        elif d == 0:
            x = -b / (2*a)
            print(f"x = {x:.3f}")
        else:
            print("Действительных корней нет")

def main():
    args = sys.argv

    if len(args) == 1 or (len(args) == 2 and args[1] == "--help"):
        print_help()
        sys.exit(0)

    if args[1] != "solve":
        print("ОШИБКА: неизвестная команда.", file=sys.stderr)
        sys.exit(1)

    a = b = c = None

    if len(args) == 2:
        try:
            print("Введите коэффициенты:")
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом.", file=sys.stderr)
            sys.exit(1)
    elif len(args) == 8:
        if (args[2] != "-a") or (args[4] != "-b") or (args[6] != "-c"):
            print("ОШИБКА: неизвестный параметр. Используйте -a, -b, -c.", file=sys.stderr)
            sys.exit(1)
        try:
            a = int(args[3])
            b = int(args[5])
            c = int(args[7])
        except ValueError:
            print("ОШИБКА: коэффициент не является целым числом.", file=sys.stderr)
            sys.exit(1)
    else:
        print("ОШИБКА: неверный набор параметров.", file=sys.stderr)
        sys.exit(1)

    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        print("ОШИБКА: значение коэффициента вне допустимого диапазона (±10000).", file=sys.stderr)
        sys.exit(1)

    solve_equation(a, b, c)

if __name__ == "__main__":
    main()