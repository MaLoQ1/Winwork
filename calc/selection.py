import random

def partition(arr, left, right, rng):
    """Разбиение Ломуто. Возвращает индекс опорного элемента."""
    q = rng.randint(left, right)
    arr[q], arr[right] = arr[right], arr[q]
    
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[right] = arr[right], arr[i]
    return i

def statistic(values, k, seed=None):
    """Поиск k-й порядковой статистики (quickselect)."""
    # Проверки k (не bool, 1 <= k <= len)
    if not isinstance(k, int) or isinstance(k, bool) or k < 1 or k > len(values):
        raise ValueError("Недопустимый номер статистики k")
    
    if not values:
        raise ValueError("Пустой список")
        
    rng = random.Random(seed)
    target = k - 1
    left = 0
    right = len(values) - 1
    
    while left < right:
        p = partition(values, left, right, rng)
        if target == p:
            return values[p]
        if target < p:
            right = p - 1
        else:
            left = p + 1
            
    return values[left]