from .main import add, multiply

def test_add():
    assert add(1, 2) == 3

def test_multiply():
    assert multiply(2, 3) == 6


if __name__ == "__main__":
    test_add()
    print("Test passed!")
