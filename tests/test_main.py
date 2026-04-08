from python_boilerplate import ADD, divide, greet, returns_none


def test_add():
    assert ADD(1, 2) == 3


def test_divide_returns_int():
    result = divide(10, 2)
    assert isinstance(result, int)


def test_greet_excited():
    assert greet("Pierre", True) == "Hello Pierre!!!"


def test_returns_none_always_int():
    assert returns_none(False) == 0