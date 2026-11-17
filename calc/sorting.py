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


def _earlier(a, b, descending):
    """Сравнение: должно ли a стоять раньше b (по псевдокоду работы №4)."""
    if descending:
        return a > b
    return a < b


def quick_sort(arr, descending=False):
    """Быстрая сортировка Хоара (in-place, возвращает None)."""
    def _sort(left, right):
        while left < right:
            pivot = arr[(left + right) // 2]
            i, j = left, right
            while i <= j:
                while _earlier(arr[i], pivot, descending):
                    i += 1
                while _earlier(pivot, arr[j], descending):
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            # Рекурсивно обрабатываем меньшую часть, большую — в цикле
            if j - left < right - i:
                _sort(left, j)
                left = i
            else:
                _sort(i, right)
                right = j

    _sort(0, len(arr) - 1)


def merge_sort(arr, descending=False):
    """Сортировка слиянием (in-place, возвращает None)."""
    def _merge(left, mid, right):
        result = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if _earlier(arr[j], arr[i], descending):
                result.append(arr[j])
                j += 1
            else:
                result.append(arr[i])
                i += 1
        result.extend(arr[i:mid + 1])
        result.extend(arr[j:right + 1])
        arr[left:right + 1] = result

    def _sort(left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        _sort(left, mid)
        _sort(mid + 1, right)
        _merge(left, mid, right)

    _sort(0, len(arr) - 1)


def heap_sort(arr, descending=False):
    """Пирамидальная сортировка (in-place, возвращает None)."""
    def _sift(i, size):
        while True:
            chosen = i
            for c in (2 * i + 1, 2 * i + 2):
                if c < size and _earlier(arr[chosen], arr[c], descending):
                    chosen = c
            if chosen == i:
                return
            arr[i], arr[chosen] = arr[chosen], arr[i]
            i = chosen

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _sift(i, n)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift(0, end)

# Регистрируем методы в словаре
METHODS["bubble"] = bubble_sort
METHODS["selection"] = selection_sort
METHODS["insertion"] = insertion_sort
METHODS["counting"] = counting_sort
METHODS["quick"] = quick_sort
METHODS["merge"] = merge_sort
METHODS["heap"] = heap_sort