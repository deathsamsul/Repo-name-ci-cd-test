from app import add, divide, subtract, multiply, modulus


def test_add():
    assert add(2, 3) == 5

def test_modulus():
    assert modulus(10, 3) == 1

def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5