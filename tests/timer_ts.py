from utils.timer import time_function
from time import sleep


@time_function
def time_for_seconds(n: int) -> None:
    sleep(n)
    print(f"\ntesting timer: this function should run for {n}s")


time_for_seconds(1)
time_for_seconds(2)
