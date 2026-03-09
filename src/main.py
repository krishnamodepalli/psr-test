"""
Main entry point for the application.
"""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def main():
    """Prints a greeting message and sum."""
    print("Hello, world!")
    print(f"1 + 2 = {add(1, 2)}")

if __name__ == "__main__":
    main()
