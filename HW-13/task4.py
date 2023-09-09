

def cached_func(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print('Return cached value')
            return cache[args]
        result = func(*args)
        cache[args] = result
        print('Return casual value')
        return result
    return wrapper


@cached_func
def add(a, b):
    return a + b


print(add(3, 4))
print(add(3, 4))
