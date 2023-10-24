from src.main import A


def test_main():
    assert A.x == 1


def test_2():
    assert 2 == 2


def test_sum():
    x = 1
    y = 2
    assert x + y == 3


def test_division():
    x = 1
    y = 2
    assert x / y == 0.5
