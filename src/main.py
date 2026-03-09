"""
Main entry point for the application.
"""

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

if __name__ == "__main__":
    main()
