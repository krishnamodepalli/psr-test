"""
Main entry point for the application.
"""

from src.strings import capitalize_words, reverse_string, truncate, slugify


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Prints a greeting message and basic math operations."""
    print("Hello, world!")
    print(f"1 + 2 = {add(1, 2)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    try:
        print(f"6 / 2 = {divide(6, 2)}")
    except ValueError as e:
        print(f"Error: {e}")

    print(capitalize_words("hello world"))
    print(reverse_string("python"))
    print(truncate("a very long description that should be cut short", 20))
    print(slugify("My Feature Page"))

if __name__ == "__main__":
    main()
