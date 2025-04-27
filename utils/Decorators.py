"""-------------------------------------------------------
PROJECT-NAME: Decorators
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    time
Version:  1.0.9
__updated__ = Sat Apr 26 2025
-------------------------------------------------------
"""
import time


def time_function(func):
    """
    -------------------------------------------------------
    Decorator that times and prints the execution duration of any function.
    The decorated function will print its name and runtime in seconds
    with 2 decimal places when called.
    Use: @time_function
    -------------------------------------------------------
    Parameters:
        func - the function to be timed (function)
    Returns:
        wrapper - the decorated function which includes timing (function)
    -------------------------------------------------------
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {(end - start):.2f}")
        return result

    return wrapper
