import pytest
from .main import add, multiply, divide

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    """Test addition with various inputs."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
    (10, 10, 100),
])
def test_multiply(a, b, expected):
    """Test multiplication with various inputs."""
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (10, 5, 2),
    (5, 2, 2.5),
    (-10, 2, -5),
])
def test_divide(a, b, expected):
    """Test division with various inputs."""
    assert divide(a, b) == expected

def test_divide_by_zero():
    """Verify that division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
