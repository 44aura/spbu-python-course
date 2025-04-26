import pytest
from project.generators.prime_nums import get_kth_prime, prime_gen


@pytest.mark.parametrize(
    "k, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 7),
        (5, 11),
    ],
)
def test_get_kth_prime(k, expected):
    assert get_kth_prime(k) == expected


@pytest.mark.parametrize("k", [-1, 0])
def test_get_kth_prime_invalid_k(k):
    with pytest.raises(ValueError, match="k must be greater than or equal to 1"):
        get_kth_prime(k)


def test_prime_generator_first_primes():
    """Test if the first few prime numbers are generated correctly."""
    p_gen = prime_gen()
    assert next(p_gen) == 2
    assert next(p_gen) == 3
    assert next(p_gen) == 5
    assert next(p_gen) == 7
    assert next(p_gen) == 11
    assert next(p_gen) == 13
