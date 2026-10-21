import sys
import random

# Константы из задания
MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000


def read_array(path=None):
    """Чтение массива из файла или с клавиатуры."""
    if path:
        try:
            # utf-8-sig нужен, чтобы корректно читать файлы с BOM (например, созданные в Блокноте)
            with open(path, encoding="utf-8-sig") as f:
                text = f.read()
        except Exception as e:
            print(f"Ошибка чтения файла: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = []
        print("Введите массив (пустая строка для завершения):", file=sys.stderr)
        while True:
            try:
                line = input()
                if not line.strip():
                    break
                lines.append(line)
            except EOFError:
                break
        text = " ".join(lines)

    # Заменяем запятые на пробелы и разбиваем
    text = text.replace(",", " ")
    words = text.split()

    if not words:
        print("Ошибка: массив пуст", file=sys.stderr)
        sys.exit(1)

    try:
        values = [int(w) for w in words]
    except ValueError:
        print("Ошибка: массив должен содержать только целые числа", file=sys.stderr)
        sys.exit(1)

    # Проверка количества и диапазона
    if not (1 <= len(values) <= MAX_COUNT):
        print(f"Ошибка: количество элементов вне диапазона 1..{MAX_COUNT}", file=sys.stderr)
        sys.exit(1)

    for v in values:
        if not (MIN_VALUE <= v <= MAX_VALUE):
            print(f"Ошибка: значение {v} выходит за пределы {MIN_VALUE}..{MAX_VALUE}", file=sys.stderr)
            sys.exit(1)

    return values


def write_array(values, path=None):
    """Запись массива в файл или вывод на экран."""
    if path:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(" ".join(str(x) for x in values) + "\n")
            print(f"Записано элементов: {len(values)} в файл {path}")
        except Exception as e:
            print(f"Ошибка записи файла: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(" ".join(str(x) for x in values))


def fill_array(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Генерация случайного массива."""
    if not (1 <= count <= MAX_COUNT):
        print(f"Ошибка: количество элементов вне диапазона 1..{MAX_COUNT}", file=sys.stderr)
        sys.exit(1)
    if not (MIN_VALUE <= low <= MAX_VALUE) or not (MIN_VALUE <= high <= MAX_VALUE):
        print(f"Ошибка: границы должны быть в диапазоне {MIN_VALUE}..{MAX_VALUE}", file=sys.stderr)
        sys.exit(1)
    if low > high:
        print("Ошибка: min не может быть больше max", file=sys.stderr)
        sys.exit(1)

    random.seed(seed)
    return [random.randint(low, high) for _ in range(count)]


def binary_search(arr, target):
    """Двоичный поиск. Возвращает индекс или None."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
