from typing import Callable


def prime_gen():
    """
    A generator of prime numbers.
    """
    n = 2
    while True:
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            yield n
        n += 1


p_gen = prime_gen()


def prime_decorator(func: Callable) -> Callable:
    """
    A decorator that wraps a function to return the k-th prime number.

    Args:
        func (Callable): A prime numbers generator.

    Return:
        Callable: A wrapped function that returns the k-th prime number.

    Raises:
        ValueError: If k is less than 1.
    """
    current_prime_index = 0  # Track the index of the next prime to be generated

    def wrapper(k: int) -> int:
        nonlocal current_prime_index

        if k < 1:
            raise ValueError("k must be greater than or equal to 1")

        if k > current_prime_index:
            for _ in range(k - current_prime_index):
                prime = next(p_gen)
            current_prime_index = k  # Update the current prime index

        return func(prime)

    return wrapper


@prime_decorator
def get_kth_prime(prime: int) -> int:
    """
    Function to return the k-th prime number.

    Args:
        prime (int): The k-th prime number, provided by the decorator.

    Return:
        int: The k-th prime number.
    """
    return prime
