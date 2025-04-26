from copy import deepcopy
import inspect


class Evaluated:
    """
    If it is passed as default value of parameter then after applying smart_args
    decorator given function is evaluated every time. Requiers callable function with no arguments.
    """

    def __init__(self, func):
        if not callable(func) or inspect.signature(func).parameters:
            raise ValueError("Requiers callable function with no arguments.")
        self.func = func

    def evaluate(self):
        return self.func()


class Isolated:
    """
    Class-flag
    """

    pass


def smart_args(func):
    """
    Decorator function that wraps the original function to handle
    'Evaluated' and 'Isolated' argument defaults.

    Args:
        func (callable): The function to be wrapped.

    Returns:
        callable: A wrapper function that processes the arguments before
                calling the original function.
    """

    signature = inspect.signature(func)
    params = signature.parameters

    def wrapper(*args, **kwargs):
        """
        Wrapper function that processes arguments for the decorated function,
        handling special cases for 'Evaluated' and 'Isolated' argument defaults.

        Args:
            *args: Positional arguments passed to the original function.
            **kwargs: Keyword arguments passed to the original function.

        Returns:
            The result of the original function after processing the arguments.
        """

        # check if Evaluated or Isolated is passed as argument
        assert all(not isinstance(arg, (Evaluated, Isolated)) for arg in args)
        assert all(not isinstance(kwargs[key], (Evaluated, Isolated)) for key in kwargs)

        new_kwargs = {}
        for name, param in params.items():
            if name in kwargs and not isinstance(param.default, (Isolated, Evaluated)):
                new_kwargs[name] = kwargs[name]

            else:
                if isinstance(param.default, Evaluated):
                    d_value = param.default.func
                    if d_value == Isolated:
                        raise ValueError(
                            "Isolated was passed as argument to Evaluated."
                        )

                    if name in kwargs:
                        new_kwargs[name] = kwargs[name]
                    else:
                        new_kwargs[name] = d_value()
                if isinstance(param.default, Isolated):
                    if name in kwargs:
                        new_kwargs[name] = deepcopy(kwargs[name])
                    else:
                        raise ValueError(f"Argument '{name}' must be provided")
        return func(*args, **new_kwargs)

    return wrapper
