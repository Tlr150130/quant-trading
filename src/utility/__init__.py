import time
import tracemalloc
import os
import inspect
import threading
import psutil
import functools
import gc

def add_diagnostics():
    """
    Decorator to report execution time, memory usage, CPU usage, I/O, call count, GC events, and exceptions.
    """
    def decorator(func):
        call_count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count
            call_count += 1

            # Get path and function name
            caller_file = inspect.stack()[1].filename
            path = os.path.dirname(os.path.abspath(caller_file))
            func_name = func.__name__

            # Take Start Snapshots
            tracemalloc.start()
            process = psutil.Process(os.getpid())
            start_time = time.perf_counter()
            start_cpu = process.cpu_times()
            start_io = process.io_counters()
            gc_start = gc.get_count()
            exception_raised = None

            # Attempt function execution
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                exception_raised = e
                result = None

            # Take End Snapshots
            end_time = time.perf_counter()
            end_cpu = process.cpu_times()
            end_io = process.io_counters()
            gc_end = gc.get_count()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            # Report metrics
            print(f"Diagnostics for '{func_name}':")
            print(f" - Path: '{path}'")
            print(f" - Call count: {call_count}")
            print(f" - Processing time: {end_time - start_time:.6f} seconds")
            print(f" - Memory usage: current={current / 1024:.2f} KB, peak={peak / 1024:.2f} KB")
            print(f" - CPU (user/system) time: {end_cpu.user - start_cpu.user:.6f}s / {end_cpu.system - start_cpu.system:.6f}s")
            print(f" - I/O (read/write): {end_io.read_bytes - start_io.read_bytes} / {end_io.write_bytes - start_io.write_bytes} bytes")
            print(f" - Garbage Collection events: {tuple(e - s for s, e in zip(gc_start, gc_end))}")
            
            # Report and raise error if needed
            if exception_raised:
                print(f" - Exception raised: {exception_raised}")
                raise exception_raised

            # Return result
            return result
        return wrapper
    return decorator