"""Simple multiply module with a small CLI.

This module provides:
- multiply(a, b): return product as float
- parse_args(argv): parse and validate CLI arguments
- main(argv=None): entry point (keeps behavior compatible with existing tests)
"""

from __future__ import annotations

from typing import List, Optional, Tuple
import sys


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers as a float."""
    return a * b


def parse_args(argv: Optional[List[str]] = None) -> Tuple[float, float]:
    """Parse and validate arguments.

    Accepts argv (including program name at index 0). Expects exactly two numeric
    arguments after the program name. Raises ValueError on invalid input.
    """
    if argv is None:
        argv = sys.argv  # pragma: no cover

    if len(argv) != 3:
        raise ValueError("Expected two numeric arguments")

    try:
        a = float(argv[1])
        b = float(argv[2])
    except (ValueError, TypeError):
        raise ValueError("Arguments must be numbers")

    return a, b


def main(argv: Optional[List[str]] = None) -> None:
    """Command-line entry point.

    Keeps the same observable behavior: prints result on success and exits with
    code 1 on error to remain compatible with existing tests and CLI usage.
    """
    if argv is None:
        argv = sys.argv

    try:
        a, b = parse_args(argv)
    except ValueError:
        print("エラー: 引数を2つの数値で指定してください")
        sys.exit(1)

    print(f"{a} × {b} = {multiply(a, b)}")


if __name__ == "__main__":  # pragma: no cover
    main()
