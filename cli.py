"""Модуль разбора параметров командной строки (argparse)."""

import argparse


def build_parser():
    """Создаёт и возвращает разборщик параметров."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    subs = parser.add_subparsers(dest="command")

    # --- solve ---
    p = subs.add_parser("solve", help="решение уравнения",
                        description="Решение уравнения A*x^2 + B*x + C = 0.",
                        allow_abbrev=False)
    p.add_argument("-a", type=int, help="коэффициент A")
    p.add_argument("-b", type=int, help="коэффициент B")
    p.add_argument("-c", type=int, help="коэффициент C")

    # --- stats ---
    p = subs.add_parser("stats", help="показатели последовательности",
                        description="Показатели числовой последовательности.",
                        allow_abbrev=False)
    p.add_argument("--input", help="имя файла с числами")

    # --- series ---
    p = subs.add_parser("series", help="сумма ряда",
                        description="Сумма знакочередующегося ряда.",
                        allow_abbrev=False)
    p.add_argument("--func", required=True, help="имя ряда (sqplus, third)")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="число слагаемых (1..10000)")
    group.add_argument("--eps", type=float, help="точность (не грубее 0.0001)")

    # --- integrate ---
    p = subs.add_parser("integrate", help="численное интегрирование",
                        description="Интеграл методом левых прямоугольников.",
                        allow_abbrev=False)
    p.add_argument("--func", required=True, help="имя функции (ratio, root)")
    p.add_argument("--from", dest="start", type=float, required=True,
                   help="нижний предел")
    p.add_argument("--to", dest="end", type=float, required=True,
                   help="верхний предел")
    p.add_argument("--steps", type=int, required=True,
                   help="число шагов (1..100000)")

    return parser