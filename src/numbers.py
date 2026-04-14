"""
Numeric utility functions for common number operations.
"""


def clamp(value, min_value, max_value):
    """Clamps a value between min_value and max_value (inclusive)."""
    return max(min_value, min(value, max_value))
