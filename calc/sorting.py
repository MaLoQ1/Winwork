from calc.arrays import MIN_VALUE, MAX_VALUE

# Словарь методов сортировки (пустой, заполняется в конце файла)
METHODS = {}

def _out_of_order(a, b, descending):
    """Проверка, стоят ли элементы не по порядку."""
    if descending:
        return a < b
    return a > b


def bubble_sort(arr, descending=False):
    """Сортировка пузырьком."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if _out_of_order(arr[j], arr[j + 1], descending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr, descending=False):
    """Сортировка выбором."""
    n = len(arr)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if _out_of_order(arr[best], arr[j], descending):
                best = j
        arr[i], arr[best] = arr[best], arr[i]


def insertion_sort(arr, descending=False):
    """Сортировка вставками."""
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i
        while j > 0 and _out_of_order(arr[j - 1], current, descending):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = current


def counting_sort(arr, descending=False):
    """Сортировка подсчётом."""
    size = MAX_VALUE - MIN_VALUE + 1
    counters = [0] * size
    
    for value in arr:
        counters[value - MIN_VALUE] += 1
        
    k = 0
    indices = range(size)
    if descending:
        indices = reversed(indices)
        
    for idx in indices:
        for _ in range(counters[idx]):
            arr[k] = idx + MIN_VALUE
            k += 1


# Регистрируем методы в словаре
METHODS["bubble"] = bubble_sort
METHODS["selection"] = selection_sort
METHODS["insertion"] = insertion_sort
METHODS["counting"] = counting_sort