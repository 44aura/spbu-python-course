from typing import Callable, Any


def curry_explicit(func: Callable, arity: int) -> Callable:
    """
    Convert a function of several arguments into a sequance of functions of one argument

    Args:
    func: Callable - The function being converted (curried)
    arity: int - The number of arguments

    Return:
    Callable - The version of curried function

    """
    if arity < 0:
        raise ValueError("Arity can't be negative!")
    if arity == 0:
        return func()

    def curry(args: tuple[Any, ...]) -> Callable:
        if len(args) == arity:
            return func(*args)
        return lambda new_arg: curry(args + (new_arg,))

    return curry(())


def uncurry_explicit(func: Callable, arity: int) -> Callable:
    """
    Convert a sequance of functions of one argument into a function of several arguments

    Args:
    func: Callable - The function being converted (uncurried)
    arity: int - The number of arguments

    Return:
    Callable - The version of uncurried function

    """
    if arity < 0:
        raise ValueError("Arity can't be negative!")
    if arity == 0:
        return func

    def uncurried(*args: Any) -> Any:
        if len(args) != arity:
            raise ValueError("Wrong arguments amount")
        result: Callable = func
        for arg in args:
            result = result(arg)
        return result

    return uncurried


f = curry_explicit(sum, 4)
