def check_types(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for arg_name, expected_type in annotations.items():
            if arg_name != 'return':
                if arg_name in kwargs:
                    arg_value = kwargs[arg_name]
                    if not isinstance(arg_value, expected_type):
                        raise TypeError(f"Argument {arg_name} must be {expected_type.__name__}, not {type(arg_value).__name__}")
                else:
                    arg_position = list(annotations.keys()).index(arg_name)
                    if not isinstance(args[arg_position], expected_type):
                        raise TypeError(f"Argument {arg_name} must be {expected_type.__name__}, not {type(args[arg_position]).__name__}")
        result = func(*args, **kwargs)
        if 'return' in annotations:
            expected_return_type = annotations['return']
            if not isinstance(result, expected_return_type):
                raise TypeError(f"Return value must be {expected_return_type.__name__}, not {type(result).__name__}")
        return result
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))
try:
    add("1", "2")
except TypeError as e:
    print(e)
