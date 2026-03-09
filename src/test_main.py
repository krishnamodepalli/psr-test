import pytest
from .main import add, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(6, 0)

if __name__ == "__main__":
    test_add()
    test_multiply()
    test_divide()
    print("All tests passed!")
