# src/utils/timer.py

import time
from functools import wraps


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()

        print(
            f"{func.__name__} "
            f"executed in "
            f"{end-start:.2f} sec"
        )

        return result

    return wrapper