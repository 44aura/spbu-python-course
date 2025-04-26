from collections import OrderedDict
from functools import wraps


def cacher(size=0):
    def decorator(func):

        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                return cache[key]
            else:
                result = func(*args, **kwargs)
                cache[key] = result

            if len(cache) > size and size > 0:
                cache.popitem(last=False)
            print(cache)
            return result

        return wrapper

    return decorator
