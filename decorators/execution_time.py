import time
from datetime import datetime


def execution_time(foo):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        result = foo(*args, **kwargs)
        execution_time = datetime.now() - initial_time
        print(execution_time)
        return result

    return wrapper

@execution_time
def sum(x, y):
    time.sleep(2)
    return x + y

res = sum(1, 3)
print(res)

