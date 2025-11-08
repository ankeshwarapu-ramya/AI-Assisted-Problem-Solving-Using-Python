import argparse
import sys
from typing import Iterable, List


def sum_of_squares(numbers: Iterable[float]) -> float:
    """Return the sum of squares for the given iterable of numbers."""
    return sum((x * x) for x in numbers)


def sum_of_squares_range(n: int) -> int:
    """Return sum_{i=1..n} i^2 using closed-form formula.
    Formula: n(n+1)(2n+1)/6
    """
    return n * (n + 1) * (2 * n + 1) // 6


def _parse_float_list(s: str) -> List[float]:
    """Parse a string of numbers separated by commas or whitespace into a list of floats.
    Raises ValueError on invalid input or if any value is not finite.
    """
    if not s.strip():
        raise ValueError("empty input")