

def cached_func(func):
    __cached__ = {}

    def wrapper(*args):
        if args in __cached__:
            print('Return cached value')
            return __cached__[args]
        result = func(*args)
        __cached__[args] = result
        print('Return casual')
        return result
    return wrapper


@cached_func
def add(a, b):
    return a + b


print(add(3, 4))
print(add(3, 4))
