import pytest
from project.decorators.curry_uncurry import curry_explicit


def test_curry():
    f = lambda a, b, c: a + b + c
    f_curried = curry_explicit(f, 3)
    assert f_curried(1)(2)(9) == 12
    with pytest.raises(TypeError):
        f_curried(1, 2)(9)
    with pytest.raises(TypeError):
        f_curried(1)(2, 9)
    with pytest.raises(TypeError):
        f_curried(1, 2, 9)


def test_negative_arity():
    f = lambda a, b: a * b
    with pytest.raises(ValueError):
        curry_explicit(f, -2)(1)(2)


def test_zero_arity():
    f = lambda: 777
    assert curry_explicit(f, 0) == 777


def test_wrong_arity():
    f = lambda x, y: x**y
    f_curried = curry_explicit(f, 2)
    with pytest.raises(TypeError):
        f_curried(2)(3)(8)


def test_optional_arity():
    f = curry_explicit(min, 4)
    assert f(3)(5)(9)(19) == 3
