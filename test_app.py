from app import add, divide, subtract, multiply, power, square


def test_add():
    assert add(2, 3) == 5

def test_power():
    assert power(2, 3) == 8

def test_subtract():
    assert subtract(5, 3) == 2

def test_square():
    assert square(4) == 16

def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5