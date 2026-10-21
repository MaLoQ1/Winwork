import subprocess

sizes = [1000, 3000, 10000]
methods = ["bubble", "selection", "insertion", "counting"]

print("| Размер | Метод | Замер 1 | Замер 2 | Замер 3 | Среднее |")
print("|---|---|---|---|---|---|")

for size in sizes:
    input_file = f"arr_{size}.txt"
    for method in methods:
        times = []
        for _ in range(3):
            # Убрали encoding="utf-8", чтобы Python сам определил кодировку Windows
            result = subprocess.run(
                ["python", "mathtool.py", "sort", "-m", method, "-i", input_file, "-o", f"out_{size}_{method}.txt"],
                capture_output=True,
                text=True
            )
            
            # Если stderr пустой (ошибка), пропускаем
            if result.stderr is None:
                print(f"Ошибка запуска для {size} {method}")
                continue

            for line in result.stderr.splitlines():
                if "Время операции" in line:
                    # Берем последнее слово (число) и заменяем запятую на точку, если вдруг она есть
                    time_str = line.split(":")[-1].replace("с", "").strip().replace(",", ".")
                    try:
                        time_val = float(time_str)
                        times.append(time_val)
                    except ValueError:
                        pass
                    break
        
        if times:
            avg_time = sum(times) / len(times)
            t1, t2, t3 = [f"{t:.6f}" for t in times]
            print(f"| {size} | {method} | {t1} | {t2} | {t3} | {avg_time:.6f} |")
        else:
            print(f"| {size} | {method} | Ошибка | Ошибка | Ошибка | Ошибка |")