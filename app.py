
def validate_numbers(a, b):
    if a < 0 or b < 0:
        raise ValueError("Negative numbers are not allowed")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def modulus(a, b):
    validate_numbers(a, b)
    return a % b  # This function calculates the remainder of a divided by b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

def power(a, b):
    validate_numbers(a, b)
    return a ** b

def multiply(a, b):
    validate_numbers(a, b)
    return a * b

def root(a, n):
    validate_numbers(a, n)
    return a ** (1/n)

def square(a):
    validate_numbers(a, 0)
    return a ** 2

def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("CI/CD test project")