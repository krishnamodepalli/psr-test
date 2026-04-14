"""
Numeric utility functions for common number operations.
"""


def clamp(value, min_value, max_value):
    """Clamps a value between min_value and max_value (inclusive)."""
    return max(min_value, min(value, max_value))


def is_even(n):
    """Returns True if n is even, False otherwise."""
    return n % 2 == 0


def is_odd(n):
    """Returns True if n is odd, False otherwise."""
    return n % 2 != 0
