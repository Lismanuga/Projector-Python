import time


def limiter(func):
    call_times = []

    def wrapper(*args, **kwargs):
        limit = 3
        current_time = time.time()

        call_times[:] = [t for t in call_times if current_time - t <= 60]

        if len(call_times) < limit:
            call_times.append(current_time)
            return func(*args, **kwargs)
        else:
            raise Exception('Too many calls, wait a little bit')

    return wrapper


@limiter
def add(a, b):
    return a + b


try:
    for _ in range(4):
        print(add(3, 4))
except Exception as e:
    print(e)
