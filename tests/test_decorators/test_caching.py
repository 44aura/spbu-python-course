from project.decorators.caching import cacher
from typing import List


def test_cache():
    @cacher(2)
    def add(x: int, y: int):
        return x + y

    assert add(3, 6) == 9
    assert add(2, 9) == 11
    assert add(8, 4) == 12


def test_cache_with_count():
    count = 0

    @cacher(2)
    def add_with_count(x: int, y: int):
        nonlocal count
        count += 1
        return x + y

    f = add_with_count
    assert f(1, 2) == 3
    assert count == 1  # calculate

    assert f(3, 4) == 7
    assert count == 2  # calculate

    assert f(1, 2) == 3
    assert count == 2  # take from cache

    assert f(5, 7) == 12
    assert count == 3  # calculate

    assert f(3, 4) == 7
    assert count == 3  # take from cache


def test_cache_built_in():
    divmod_cache = cacher(1)(divmod)

    assert divmod_cache(7, 3) == (2, 1)
    assert divmod_cache(8, 2) == (4, 0)
    assert divmod_cache(8, 2) == (4, 0)
