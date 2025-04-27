from time import sleep
from utils.Decorators import time_function


@time_function
def pipeline():
    sleep(3)


pipeline()
