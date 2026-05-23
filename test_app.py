from app import add, divide, subtract, multiply, power, root, square,modulus
import pytest

def test_add():
    assert add(2, 3) == 5

def test_power():
    assert power(2, 3) == 8

def test_subtract():
    assert subtract(5, 3) == 2

def test_modulus():
    assert modulus(10, 3) == 1

def test_root():
    assert root(27, 3) == 3

def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_square():
    assert square(4) == 16

#     git checkout main
# git pull origin main
# git checkout -b feature/add-modulo

def test_native_add():
    with pytest.raises(ValueError):
        add(-1, 5)
def test_native_modulus():
    with pytest.raises(ValueError):
        modulus(-1, 5)
def test_native_subtract():
    with pytest.raises(ValueError):
        subtract(-1, 5)
def test_native_power():
    with pytest.raises(ValueError):
        power(-1, 5)
def test_native_multiply():
    with pytest.raises(ValueError):
        multiply(-1, 5)
def test_native_root():
    with pytest.raises(ValueError):
        root(-1, 5)
def test_native_square():
    with pytest.raises(ValueError):
        square(-1)