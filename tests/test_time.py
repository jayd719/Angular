"""-------------------------------------------------------
PROJECT-NAME: Module Description Here
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    OpenCV
Version:  1.0.9
__updated__ = Sat Apr 26 2025
-------------------------------------------------------
"""

from utils.Decorators import time_function
from time import sleep


@time_function
def test_time_for_seconds() -> None:
    n =0
    sleep(n)
    print(f"\ntesting timer: this function should run for {n}s")


