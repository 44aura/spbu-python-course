def rgba_gen():
    """
    A generator of rgba vectors.
    r - red
    g - green
    b - blue
    a - alpha

    Values r, g, b are in interval (0, 255).
    Value a is even and in interval (0, 100).

    Return:
       Generator
    """
    return (
        (r, g, b, a)
        for r in range(256)
        for g in range(256)
        for b in range(256)
        for a in range(101)
        if a % 2 == 0
    )


def get_rgba_vector(i: int = 0):
    """
    Calculate i-th rgba vector.

    Return:
        Tuple of four integers

    Raises:
        ValueError: if i less or greater possible value of rgba vector's index
    """
    if i < 0 or i > 256 * 256 * 256 * 51:
        raise ValueError("Wrong value of i")
    gen = rgba_gen()
    for _ in range(i):
        next(gen)
    return next(gen)
