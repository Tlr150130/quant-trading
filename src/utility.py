import time
import tracemalloc
from functools import wraps


def profile(path=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if path:
                print(f"Profile path: {path}")
            tracemalloc.start()
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
            print(f"Memory usage: current={current / 1024:.2f} KB, peak={peak / 1024:.2f} KB")
            return result
        return wrapper
    return decorator

